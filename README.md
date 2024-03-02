# Categorify 
Text classification to classify category of products based on its name/description.

## Overview

This project involves training a machine learning model for [classifying the category]. Below are the details related to the training process, deployment scripts, and other relevant information.

## Training and Deployment

### Training Scripts
- `NAZMI_Assesment3_training.ipynb`: This python notebook file consist the training of the model

### Deployment Scripts
- `NAZMI_Assesment3_deploy.py`: This python notebook file consist the deployment of the model

### Requirements
- `requirements.txt`: List of required packages and versions.

## Model

### Model File
- [Download Model](https://github.com/nazmi08/Text-Classification-using-Deep-Learning-Algorithm/tree/main/models)
### Model Architecture
![Model Architecture](https://github.com/nazmi08/Text-Classification-using-Deep-Learning-Algorithm/blob/main/models/model_architecture.png?raw_true)

## Training Metrics

### Loss and Accuracy Graph
#### Overall Loss and Accuracy
![Loss and Accuracy Graph](https://github.com/nazmi08/Text-Classification-using-Deep-Learning-Algorithm/blob/main/result_images/loss_accuracy.png?raw_true)
#### Tensorboard Accuracy Graph
![Tensorboard Accuracy Graph](https://github.com/nazmi08/Text-Classification-using-Deep-Learning-Algorithm/blob/main/result_images/tensorboard_epoch_accuracy.png?raw_true)
#### Tensorboard Loss Graph
![Tensorboard Loss Graph](https://github.com/nazmi08/Text-Classification-using-Deep-Learning-Algorithm/blob/main/result_images/tensorboard_epoch_loss.png?raw_true)
#### F1-Score
![F1-Score](https://github.com/nazmi08/Text-Classification-using-Deep-Learning-Algorithm/blob/main/result_images/f1_score.png?raw_true)

## Prediction Example

### Example 1
#### Prediction
  ![Prediction 1](https://github.com/nazmi08/Text-Classification-using-Deep-Learning-Algorithm/blob/main/result_images/example_1.png?raw_true)

### Example 2
#### Prediction
  ![Prediction 2](https://github.com/nazmi08/Text-Classification-using-Deep-Learning-Algorithm/blob/main/result_images/example_2.png?raw_true)

### Example 3
#### Prediction
  ![Prediction 3](https://github.com/nazmi08/Text-Classification-using-Deep-Learning-Algorithm/blob/main/result_images/example_3.png?raw_true)

### Example 4
#### Prediction
  ![Prediction 4](https://github.com/nazmi08/Text-Classification-using-Deep-Learning-Algorithm/blob/main/result_images/example_4.png?raw_true)

## How to Use

### Ensure Tokenizer, Label, and Model are Available:
- Before running the deployment script (`NAZMI_Assesment3_deploy.py`), make sure that the tokenizer, label encoder, and the trained model file are available in the designated directories.

### On the Webpage:
1. You'll find a text area where you can input the text of the product description.
2. After entering the text, click the "Classify the Product" button.

### View Results:
- The "Category" table will display the available categories that the model can predict.
- The "Prediction Category" section will show the category predicted by the system based on the input text.

## Data Source

The dataset used for training is sourced from [cite the source of the data](https://www.kaggle.com/datasets/saurabhshahane/ecommerce-text-classification).

