from PIL import Image
import base64
import io
import requests

image_path = "artifacts/Dataset/Test/Fake/fake_2243.jpg"


# Define the API Gateway URL
API_GATEWAY_URL = ""

# Open the image file in binary mode and read its content
with open(image_path, "rb") as file:
    image_data = file.read()

# Set the headers for the request
headers = {"Content-Type": "image/jpeg"}

# Send the image data as binary in the request
response = requests.post(API_GATEWAY_URL, data=image_data, headers=headers)

# Print the response
print(response.text)