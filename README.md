<h3 align="left">AI Lung Classification Project</h3>
</div>

<br>

<img src="https://github.com/AbdullahHDev/AI-LungClassification/blob/main/assets/img1.png" width="900">

## About The Project

This project aims to develop an image classification system for chest X-Rays to differentiate between normal lungs and lungs which have pneumonia. The system uses several CNN architectures, including DenseNet121, VGG16, ResNet50, and InceptionV3. Each model is adapted for binary classification to distinguish between pneumonia-afflicted and healthy lung images. To prevent overfitting and ensure the best model performance, early stopping and model checkpoints are implemented. These methods monitor validation loss across epochs, halting training when no improvement is seen and saving the best model respectively.

### Built With

[![Python][Python-badge]][Python-url]
[![TensorFlow][TensorFlow-badge]][TensorFlow-url]
[![Keras][Keras-badge]][Keras-url]
[![Streamlit][Streamlit-badge]][Streamlit-url]

## Getting Started

This section outlines the steps to set up the AI Lung Classification Project locally, focusing on the model training and web application deployment for pneumonia detection.

### Prerequisites

- Python 3.x
- Pip package manager

### Installation

1. Clone the repository: `git clone https://github.com/AbdullahHDev/AI-LungClassification.git`
2. Run the Streamlit application: `streamlit run lung_classifier.py`

### Usage

1. Select which model you want to use using the sidebar, you can also select all models to see the probabillity results for all models.
2. Upload your X-Ray image (test images are included in the datasets/tests folder).
3. Press the test button and wait for the results to show.
