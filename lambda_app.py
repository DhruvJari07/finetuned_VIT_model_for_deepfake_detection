import streamlit as st
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Define your API endpoint URL
API_ENDPOINT = os.getenv("LAMBDA_API_ENDPOINT")

# Streamlit app
def main():
    st.title("Deepfake Detection App")
    st.write("upload an image to detect if your image was created using AI or not")
    
    if 'uploaded_image' not in st.session_state:
        st.session_state.uploaded_image = None
    # File uploader for image
    uploaded_image = st.file_uploader("Upload an image", type=['jpg', 'jpeg'])

    if uploaded_image is not None:
        # Display uploaded image
        st.image(uploaded_image, caption='Uploaded Image', width=300)
        st.session_state.uploaded_image = uploaded_image
        
        # Send image to API on button click
        if st.button('Predict'):
            try:
                image_data = st.session_state.uploaded_image.read()

                # Set the headers for the request
                headers = {"Content-Type": "image/jpeg"}

                # Send the image data as binary in the request
                response = requests.post(API_ENDPOINT, data=image_data, headers=headers)
                results = json.loads(response.text)
                # Print the response
                for result in results:
                    if result['score'] >= 0.5:
                        prediction = result['label']
                    # Display response from API
                        st.write(f"Your image is {prediction}")

            except Exception as e:
                st.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()

