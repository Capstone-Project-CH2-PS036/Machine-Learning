# Setup Environment

- python 3.8
- tensorflow 2.9.0
- matplotlib 3.7.3
- numpy 1.22.4
- tflite 2.10.0
- joblib 1.3.2
- zipfile
- os
- cv2

# Step By Step Machine Learning Capstone

- first download the dataset or use the urine.zip file format
- secondly, do preprocessing on the dataset, using the algorithm in the run file preprocessing.py
- thirdly, use the dataset after preprocessing to train the model
- fourth run capstone.py to train the model
- fifth deploy the model to cloud computing

# About This Project
A team of machine learning engineers worked on a project to develop a machine learning model that could analyze urine color. The model was trained on a dataset of images of urine color from different health conditions. 

The dataset was collected from one open source source, Kaggle. The urine images in the dataset were divided into 8 color categories: blue, brown, green, black, orange, yellow, red, and white. There were 10-30 urine images in each color category. This small number of images could be a limitation for training a machine learning model.

To overcome the limitations of the dataset, the machine learning team used data preprocessing to increase the number of images by creating new versions of existing data. In this case, the machine learning team used data augmentation techniques to change the contrast and brightness of the images. This technique was used to make the model more trained to handle urine images in various lighting conditions.

The machine learning model developed by the team used a 3-layer convolutional neural network (CNN) image classification technique. CNN is a machine learning technique that can be used for image classification. CNN works by learning the important features of an image to distinguish between different categories. The CNN model developed by the team had an accuracy of over 95% in urine color classification.

The machine learning team has successfully developed a machine learning model that can analyze urine color with high accuracy. This model has the potential to improve the accuracy and efficiency of urine color examinations for detecting health conditions.
