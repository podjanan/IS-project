import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

model = tf.keras.models.load_model("intel_nn_model_93_9.h5")

class_names = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']

img_path = "\predict\p1.jpg"  # ใส่ path ภาพที่อยากทำนาย

img = image.load_img(img_path, target_size=(224,224))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)
predicted_class = class_names[np.argmax(prediction)]
confidence = np.max(prediction)

plt.imshow(img)
plt.title(f"Prediction: {predicted_class} ({confidence*100:.2f}%)")
plt.axis("off")
plt.show()