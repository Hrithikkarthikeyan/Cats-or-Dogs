import cv2
import numpy as np
import os
from tqdm import tqdm
from random import shuffle

TRAIN_DIR = 'Downloads/cats_and_dogs/train'
TEST_DIR = 'Downloads/cats_and_dogs/test1'
IMG_SIZE = 50
LR = 1e-3 #learning rate

MODEL_NAME = 'dogsvscats-{}-{}.model'.format(LR,'5conv-basic')




def label_img(img):
    word_label = img.split('.')[-3]
    if word_label == 'cat': return [1,0]
    elif word_label == 'dog' : return [0,1]


