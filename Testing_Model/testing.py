import tensorflow as tf
import numpy as np
import keras.utils as image

model = tf.keras.models.load_model('model.h5')

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

image_path = "image/baru.jpg"

preprocessed_image = preprocess_image(image_path)

predictions = model.predict(preprocessed_image)

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