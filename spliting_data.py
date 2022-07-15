from glob import glob
import os
from sklearn.model_selection import train_test_split as tts
import cv2
import shutil

images = glob(os.path.join('images','*.png'))
labels = glob(os.path.join('labels','*.txt'))

images.sort()
labels.sort()

train_images, val_images, train_labels, val_labels = tts(images, labels, train_size=0.8, random_state=42)

if not os.path.isdir('images/train'):
    os.mkdir('images/train')
if not os.path.isdir('images/val'):
    os.mkdir('images/val')
if not os.path.isdir('labels/train'):
    os.mkdir('labels/train')
if not os.path.isdir('labels/val'):
    os.mkdir('labels/val')

#Utility function to move images
def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.copy(f, destination_folder)
        except:
            print(f)

# Move the splits into their folders
move_files_to_folder(train_images, 'images/train/')
move_files_to_folder(val_images, 'images/val/')

move_files_to_folder(train_labels, 'labels/train/')
move_files_to_folder(val_labels, 'labels/val/')


print('data was successfully split into train and val...')