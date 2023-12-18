# Import necessary libraries
import zipfile
import tensorflow as tf
import matplotlib.pylab as plt
import numpy as np
import joblib
import keras.utils as image
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Define a function to solve
def solution():
    # Download and extract the training and validation datasets
    local_file = 'urine_after_preprocessing.zip'
    with zipfile.ZipFile(local_file, 'r') as zip_ref:
        zip_ref.extractall('data')

    TRAINING_DIR = 'data/urine_after_preprocessing/train'
    VAL_DIR = 'data/urine_after_preprocessing/validation'

    # Create data generators with data augmentation for training
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        horizontal_flip=True,
        shear_range=0.2,
        zoom_range=0.2,
        fill_mode='nearest'
    )

    # Define the image size and create a generator for training data
    train_generator = train_datagen.flow_from_directory(
        TRAINING_DIR,
        class_mode='categorical',
        batch_size=64,
        target_size=(150, 150)
    )

    # Create a data generator for validation data
    test_datagen = ImageDataGenerator(rescale=1./255)
    validation_generator = test_datagen.flow_from_directory(
        VAL_DIR,
        class_mode='categorical',
        batch_size=32,
        target_size=(150, 150)
    )

    # Define a custom callback to monitor and stop training when the desired accuracy is reached
    class myCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs=None):
            if logs.get('accuracy') > 0.95 and logs.get('val_accuracy') > 0.95:
                print("\nAccuracy is more than 95%, stopping...")
                self.model.stop_training = True

    customCallback = myCallback()

    types_dict = train_generator.class_indices
    print(types_dict)

    # Define the neural network model for image classification
    model = tf.keras.models.Sequential([
        Conv2D(16, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        MaxPooling2D(2, 2),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(8, activation='softmax')
    ])

    # Display the model summary
    model.summary()

    # Compile the model with the optimizer, loss function, and metrics
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=["accuracy"]
    )

    # Train the model using the data generators and stop when the custom callback criteria are met
    history = model.fit(
        train_generator,
        epochs=100,
        validation_data=validation_generator,
        callbacks=[customCallback]
    )

    # Plotting Training and Validation Accuracy
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

    # Plotting Training and Validation Loss
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

    return model

def saved(model):
    model.save("model.h5")

    # Save the trained model in pickle format
    pickle_model_file = 'model.pkl'
    joblib.dump(model, pickle_model_file)

    # Save the trained model in SavedModel format and convert it to TensorFlow Lite format
    RPS_SAVED_MODEL = "rps_saved_model"
    tf.saved_model.save(model, RPS_SAVED_MODEL)
    loaded = tf.saved_model.load(RPS_SAVED_MODEL)
    print(list(loaded.signatures.keys()))
    infer = loaded.signatures["serving_default"]
    print(infer.structured_input_signature)
    print(infer.structured_outputs)
    converter = tf.lite.TFLiteConverter.from_saved_model(RPS_SAVED_MODEL)
    converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
    tflite_model = converter.convert()
    tflite_model_file = 'converted_model.tflite'

    with open(tflite_model_file, "wb") as f:
        f.write(tflite_model)

    # Load TFLite model and allocate tensors.

# Function to classify an input image using the trained model
def preprocess_image(image_path):
    # Load and preprocess the input image
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    model = tf.keras.models.load_model('model.h5')
    # Make predictions using the trained model

    predictions = model.predict(img_array)
    # Map the predictions to class labels
    class_labels = ["Biru, Warna biru pada urine tidak umum dan mungkin merupakan hasil dari konsumsi pewarna makanan tertentu. Namun, jika warna biru terus menerus muncul, itu bisa menunjukkan masalah dengan ginjal atau saluran kemih. Disarankan untuk berkonsultasi dengan profesional kesehatan.",
                    "Coklat, Warna coklat pada urine bisa disebabkan oleh dehidrasi, konsumsi makanan tertentu, atau masalah dengan hati. Tetapi, coklat juga dapat menjadi tanda adanya darah dalam urine, yang memerlukan perhatian medis segera.",
                    "Hijau, Warna hijau pada urine biasanya disebabkan oleh konsumsi makanan atau suplemen tertentu. Namun, jika hijau terus muncul dan tidak dapat dijelaskan oleh faktor diet, itu bisa mengindikasikan masalah kesehatan seperti infeksi atau penyakit hati. Konsultasikan dengan dokter untuk evaluasi lebih lanjut.",
                    "Hitam, Urine hitam dapat menjadi tanda adanya darah teroksidasi atau masalah hati. Beberapa jenis makanan dan obat-obatan juga dapat menyebabkan urine hitam. Jika urine hitam terus muncul, segera hubungi profesional kesehatan.",
                    "Jingga, Warna jingga pada urine mungkin disebabkan oleh dehidrasi atau konsumsi vitamin B kompleks. Namun, jika jingga terus muncul tanpa alasan yang jelas, itu bisa menunjukkan masalah dengan hati atau saluran empedu. Periksakan ke dokter untuk evaluasi lebih lanjut.",
                    "Kuning, Warna kuning pada urine biasanya normal dan disebabkan oleh pigmen urine yang disebut urobilin. Namun, warna kuning yang sangat gelap atau kuning kecoklatan bisa menunjukkan dehidrasi. Pastikan untuk cukup minum air.",
                    "Merah, Urine merah dapat disebabkan oleh keberadaan darah. Ini bisa disebabkan oleh infeksi saluran kemih, batu ginjal, atau masalah lain pada ginjal atau kandung kemih. Segera cari bantuan medis jika urine berwarna merah.",
                    "Putih, Urine yang putih atau bening (transparan) umumnya dianggap normal dan sehat. Ini menunjukkan bahwa Anda mungkin sedang minum cukup air, dan ginjal Anda berfungsi dengan baik untuk menyaring kelebihan air dalam tubuh. Peningkatan konsumsi air dapat menghasilkan urine yang lebih transparan."
                    ]

    confidence_score = predictions.max() * 100

    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]

    print(f'The predicted class is: {predicted_class_label}')
    print("Confidence score (accuracy): {:.2f}%".format(confidence_score))

    return img_array

if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    image_path = "image/baru.jpg"
    model = solution()
    saved(model)
    predicted_label = preprocess_image(image_path)