# finetuned_VIT_model_for_deepfake_detection
Finetuning google's vit-base-patch16-224-in21k model for detecting deepfake images.

curl command
```
 curl -X POST -H "Content-Type: image/jpeg" --data-binary @fake_2243.jpg <API-Gateway-URL>

```

response received
[{"score": 0.9366282224655151, "label": "Fake"}, {"score": 0.06337182223796844, "label": "Real"}]