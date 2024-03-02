#1. Setup - import packages
import tensorflow as tf
import numpy as np
import streamlit as st
import json, re, pickle
from keras.preprocessing.sequence import pad_sequences

# Design the page title, icon and content viewing
st.set_page_config(
    page_title = 'Categorify',
    page_icon = 'icon.png'
)

#2. Functions to load the json objects and keras model
def load_json_file(filepath):
    with open(filepath, 'r') as f:
        json_object = json.load(f)
    return json_object

def load_pickle_file(filepath):
    with open(filepath, 'rb') as f:
        pickle_object = pickle.load(f)
    return pickle_object

@st.cache_resource
def load_model(filepath):
    model_object = tf.keras.models.load_model(filepath)
    return model_object


#3. Define the file paths to the resources we want to load
tokenizer_filepath = "tokenizer.pkl"
label_encoder_path = "label_encoder.json"
model_filepath = "models/category_classify.h5"

#4. Load the tokenizer, label encoder and model
tokenizer = load_pickle_file(tokenizer_filepath)
label_encoder = load_json_file(label_encoder_path)
model = load_model(model_filepath)

#5. Build the components of the streamlit app
#(A) A title text to display the app name
st.header('''Welcome to Categorify!''')
st.markdown(
    """
        This app will categorize commercial products into four categories.\n
        The available categories can be seen inside the `Category`
    """
)
#(B) Text box for users to input news article
with st.form("input_form"):
    text_area = st.text_area("Enter your product description here.")
    submitted = st.form_submit_button('Classify the product!')
text_inputs = [text_area]

#(C) Process the input string
# Remove unwanted string
def remove_unwanted_string(text_inputs):
    for index, data in enumerate(text_inputs):
        text_inputs[index] = re.sub('<.*?>', " ", data)
        text_inputs[index] = re.sub("[^a-zA-Z0-9\-, ]"," ", data).lower()
    return text_inputs

#a. Use the function to filter unwanted string
text_filtered = remove_unwanted_string(text_inputs)
#b. Tokenize the string
text_token = tokenizer.texts_to_sequences(text_filtered)
#c. Padding and truncating
text_padded = pad_sequences(text_token,maxlen=200,padding='post',truncating='post')

#(D) Use the model to make prediction
y_score = model.predict(text_padded)
y_pred = np.argmax(y_score,axis=1)

#(E) Display the result
label_map = label_encoder
result = label_map[y_pred[0]]

#(F) Write the prediction onto streamlit
st.subheader("Category")
st.table(label_map)
col1, col2 = st.columns(2)
# Column 1: Prediction Score
col1.subheader("Prediction Score")
col1.write(y_score)
# Column 2: Predicted Category
col2.subheader("Predicted Category")
if result == 'Books':
    icon = '📚'
elif result == 'Clothing & Accessories':
    icon = '🧥'
elif result == 'Electronics':
    icon = '🖥️'
elif result == 'Household':
    icon = '🏠'
else:
    icon = ''
col2.write(f"The product category is {result} {icon}")
