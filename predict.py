from transformers import pipeline
from PIL import Image
from matplotlib import pyplot as plt

model_name = "DhruvJariwala/deepfake_vs_real_image_detection"

pipe = pipeline('image-classification', model=model_name, device=-1)

image_path = "artifacts/Dataset/Validation/Fake/fake_4771.jpg"  # Replace this with the path to your image
image = Image.open(image_path)

print(pipe(image))

