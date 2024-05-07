from PIL import Image
import base64
import io

uploaded_file_path = "artifacts/Dataset/Test/Fake/fake_2243.jpg"

# Open the image file
with open(uploaded_file_path, "rb") as f:
    image_bytes = f.read()

# Convert image bytes to base64 string
uploaded_image = base64.b64encode(image_bytes).decode('utf-8')
print("Base64 string:", uploaded_image)

# Display the uploaded image
img = Image.open(io.BytesIO(base64.b64decode(uploaded_image)))
img.show()