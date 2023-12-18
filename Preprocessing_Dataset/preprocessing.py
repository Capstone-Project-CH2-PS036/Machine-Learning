import os
import cv2
import numpy as np

def adjust_contrast(image, alpha=1.0):
    # Menerapkan perubahan kontrast
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha)
    return adjusted_image

def adjust_brightness(image, beta=0):
    # Menerapkan perubahan kecerahan
    adjusted_image = cv2.convertScaleAbs(image, beta=beta)
    return adjusted_image

# Path folder input
input_folder_path = "D:\\Project\\capstone\\dataset"

# Path folder output
output_folder_path = "D:\\Project\\capstone\\dataset\\apaantuh"

# Membaca setiap gambar dari folder input
for filename in os.listdir(input_folder_path):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        input_image_path = os.path.join(input_folder_path, filename)
        image = cv2.imread(input_image_path)

        # Membuat 5 gambar dengan tingkat kontrast yang berbeda
        for i in range(1, 6):
            contrast_level = i * 0.1
            adjusted_image = adjust_contrast(image, alpha=contrast_level)
            output_filename = f"{os.path.splitext(filename)[0]}_CONTRAST_LEVEL{i}.jpg"
            output_path = os.path.join(output_folder_path, output_filename)
            cv2.imwrite(output_path, adjusted_image)

        # Membuat 5 gambar dengan tingkat kecerahan yang berbeda
        for i in range(1, 6):
            brightness_level = i * 10
            adjusted_image = adjust_brightness(image, beta=brightness_level)
            output_filename = f"{os.path.splitext(filename)[0]}_BRIGHTNESS_LEVEL{i}.jpg"
            output_path = os.path.join(output_folder_path, output_filename)
            cv2.imwrite(output_path, adjusted_image)
