from transformers import ViTForImageClassification

labels_list = ['Real', 'Fake']
MODEL_NAME = "DhruvJariwala/deepfake_vs_real_image_detection"
# Download and save the pre-trained model
model = ViTForImageClassification.from_pretrained(MODEL_NAME, num_labels=len(labels_list))
model.save_pretrained("./artifacts/premodels")

print("Model downloaded successfully!")