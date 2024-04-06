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

## Usage for Model Training

This project is designed to enable users to train machine learning models to classify chest X-ray images for the detection of pneumonia. Here's how you can train the models yourself:

### Pre-requisites

- Ensure you have Python and Pip installed on your system.
- The project uses TensorFlow, Keras, and Streamlit among other libraries. Install all required libraries using: `pip install -r requirements.txt`
- Clone the repository: `git clone https://github.com/AbdullahHDev/AI-LungClassification.git`

### Training the Models

1. The project includes scripts for training four different models: DenseNet121, VGG16, ResNet50, and InceptionV3.
2. Open the "chest-x-ray-model.ipynb" file in your desired IDE or using Jupyter (if you require a GPU, use Kaggle or Google Cloud and import the notebook)
3. Ensure that the dataset file paths are correct.
4. Run the Jupyter notebook cell by cell

## Contributing

Contributions are welcome and appreciated. Whether it's bug fixes, feature enhancements, or suggestions, feel free to fork the project and create a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AI-LungClassification`)
3. Commit your Changes (`git commit -m 'Add some AI-LungClassification'`)
4. Push to the Branch (`git push origin feature/AI-LungClassification`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Abdullah Hussain - A.A.Hussain1@newcastle.ac.uk

Project Link: [https://github.com/AbdullahHDev/AI-LungClassification](https://github.com/AbdullahHDev/AI-LungClassification)

## Acknowledgments

* [TensorFlow](https://www.tensorflow.org/)
* [Keras](https://keras.io/)
* [Streamlit](https://streamlit.io/)
* [The dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

Data: https://data.mendeley.com/datasets/rscbjbr9sj/2

License: CC BY 4.0

Citation: http://www.cell.com/cell/fulltext/S0092-8674(18)30154-5

[Python-badge]: https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org
[TensorFlow-badge]: https://img.shields.io/badge/TensorFlow-FF6F00.svg?style=for-the-badge&logo=tensorflow&logoColor=white
[TensorFlow-url]: https://www.tensorflow.org/
[Keras-badge]: https://img.shields.io/badge/Keras-D00000.svg?style=for-the-badge&logo=keras&logoColor=white
[Keras-url]: https://keras.io/
[Streamlit-badge]: https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/

