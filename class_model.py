import os
import random
import shutil

# Define paths to the original image directory and the directories for cancerous and non-cancerous images
dataset_dir = 'C:\\Users\\sosha\\OneDrive\\Documents\\Downloads\\project final\\dataset'
original_dir = os.path.join(dataset_dir, 'original')
cancerous_dir = os.path.join(dataset_dir, 'cancerous')
non_cancerous_dir = os.path.join(dataset_dir, 'non_cancerous')

# Create directories if they don't exist
os.makedirs(cancerous_dir, exist_ok=True)
os.makedirs(non_cancerous_dir, exist_ok=True)

# List all image files in the original directory
image_files = os.listdir(original_dir)

# Shuffle the list of image files
random.shuffle(image_files)

# Split the shuffled list into two equal parts
num_images = len(image_files)
num_cancerous = num_images // 2
num_non_cancerous = num_images - num_cancerous

# Move the first half of the shuffled images to the cancerous directory
for filename in image_files[:num_cancerous]:
    src = os.path.join(original_dir, filename)
    dst = os.path.join(cancerous_dir, filename)
    shutil.copy(src, dst)

# Move the second half of the shuffled images to the non-cancerous directory
for filename in image_files[num_cancerous:]:
    src = os.path.join(original_dir, filename)
    dst = os.path.join(non_cancerous_dir, filename)
    shutil.copy(src, dst)

print('Images classified successfully.')
