import tensorflow as tf
#from keras.preprocessing import image
import numpy as np
import keras.utils as image

model = tf.keras.models.load_model('model.h5')

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

image_path = "D:/Project/capstone/gambar/baru.jpg"

preprocessed_image = preprocess_image(image_path)

predictions = model.predict(preprocessed_image)

class_labels = ['Biru', 'Coklat', 'Hijau', 'Hitam', 'Jingga', 'Kuning', 'Merah', 'Putih']

confidence_score = predictions.max() * 100

predicted_class_index = np.argmax(predictions)
predicted_class_label = class_labels[predicted_class_index]

print(f'The predicted class is: {predicted_class_label}')
print("Confidence score (accuracy): {:.2f}%".format(confidence_score))