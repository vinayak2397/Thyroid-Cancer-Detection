import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

# Define the path to your dataset directory
dataset_dir = 'dataset/'

# Define a function to load and preprocess images
def load_and_preprocess_images(directory):
    images = []
    labels = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            img_path = os.path.join(directory, filename)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (224, 224))  # Resize the image to 224x224 pixels
            img = img.astype('float32') / 255.0  # Normalize pixel values to [0, 1]
            images.append(img)
            # Check the filename to determine the label
            if 'thyroid' in filename.lower():
                labels.append(1)  # 1 for thyroid cancer
            else:
                labels.append(0)  # 0 for non-thyroid cancer
    return np.array(images), np.array(labels)

# Load and preprocess images from the dataset directory
images, labels = load_and_preprocess_images(dataset_dir)

# Split the dataset into training and validation sets (80% train, 20% validation)
X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)

print("Training images shape:", X_train.shape)
print("Training labels shape:", y_train.shape)
print("Validation images shape:", X_val.shape)
print("Validation labels shape:", y_val.shape)
