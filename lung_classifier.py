import streamlit as st
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

# Set the title of the app
st.title('Pneumonia Detection from Chest X-Ray Images')

# Sidebar for model selection
model_option = st.sidebar.selectbox(
    "Select the model you want to use:",
    ("ResNet50", "VGG16", "DenseNet", "InceptionV3", "All Models")
)

# Sidebar for image upload
uploaded_file = st.sidebar.file_uploader("Choose an X-ray image...", type="jpeg")

# Button to trigger the prediction
test_button = st.sidebar.button('Test')

# Load the selected model(s)
model_paths = {
    "ResNet50": "./models/lung_classifier_rn.keras",
    "VGG16": "./models/lung_classifier_vgg.keras",
    "DenseNet": "./models/lung_classifier_dn.keras",
    "InceptionV3": "./models/lung_classifier_inceptionv3.keras"
}

models = {}
if model_option != "All Models":
    models[model_option] = load_model(model_paths[model_option])
else:
    for name, path in model_paths.items():
        models[name] = load_model(path)

if uploaded_file is not None and test_button:
    # Display the uploaded image in the main screen
    st.image(uploaded_file, caption="Uploaded X-ray image.", use_column_width=True)
    
    # Dynamically set target_size for image preprocessing based on the selected model
    if model_option == "InceptionV3":
        target_size = (299, 299)  # InceptionV3 expects (299, 299)
    else:
        target_size = (224, 224)  # Other models expect (224, 224)
    
    # Prepare the image
    img = image.load_img(uploaded_file, target_size=target_size)
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    
    # Make predictions with the selected model or all models
    if model_option != "All Models":
        prediction = models[model_option].predict(img_tensor)
        probability_pneumonia = prediction[0][0]
        st.write(f'{model_option} prediction:')
        if probability_pneumonia > 0.5:
            st.write(f'Pneumonia detected with a probability of {probability_pneumonia:.2%}.')
        else:
            st.write(f'Normal lungs detected with a probability of {(1 - probability_pneumonia):.2%}.')
    else:
        st.write("Predictions from all models:")
        for name, model in models.items():
            # Adjust target_size for each model when "All Models" is selected
            target_size = (299, 299) if name == "InceptionV3" else (224, 224)
            img = image.load_img(uploaded_file, target_size=target_size)
            img_tensor = image.img_to_array(img)
            img_tensor = np.expand_dims(img_tensor, axis=0)
            img_tensor /= 255.
            
            prediction = model.predict(img_tensor)
            probability_pneumonia = prediction[0][0]
            if probability_pneumonia > 0.5:
                st.write(f'{name}: Pneumonia detected with a probability of {probability_pneumonia:.2%}.')
            else:
                st.write(f'{name}: Normal lungs detected with a probability of {(1 - probability_pneumonia):.2%}.')
