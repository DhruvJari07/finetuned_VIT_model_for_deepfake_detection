import streamlit as st
from PIL import Image
from transformers import pipeline
import base64
import io

@st.cache_resource
def load_predict_pipeline():
    model_name = "DhruvJariwala/deepfake_vs_real_image_detection"
    pipe = pipeline('image-classification', model=model_name, device=-1)
    return pipe

pipe = load_predict_pipeline()

# Define the Streamlit app
def main():
    st.title("Fake or Real Image Predictor")

    uploaded_file = st.file_uploader("Choose a .jpg file", type=["jpg"])

    if 'uploaded_image' not in st.session_state:
        st.session_state.uploaded_image = None

    if uploaded_file is not None:
        uploaded_image_bytes = uploaded_file.read()
        st.session_state.uploaded_image = base64.b64encode(uploaded_image_bytes).decode('utf-8')
        print(st.session_state.uploaded_image)
        # Display the uploaded image
        image = Image.open(io.BytesIO(uploaded_image_bytes))
        st.image(image, caption='Uploaded Image', use_column_width=False)
        #image = Image.open(uploaded_file)
        #st.image(image, caption='Uploaded Image', use_column_width=True)
        
        # Predict whether the image is fake or real
        if st.button("Predict"):
            # Process the image and get prediction
            results = pipe(st.session_state.uploaded_image)

            for result in results:
                if result['score'] >= 0.5:
                    prediction = result['label']
            # Display the prediction
            if prediction == "Fake":
                st.error("Prediction: Fake")
            elif prediction == "Real":
                st.success("Prediction: Real")

# Run the app
if __name__ == "__main__":
    main()
