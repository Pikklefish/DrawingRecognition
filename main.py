import pickle
import os.path

import tkinter.messagebox
from tkinter import *

import numpy as np
import PIL
import cv2 as cv

from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


class DrawingClassifier:
    
    def __init__(self):
        self.class1, self.class2, self.class3 = None, None, None
        self.class1_counter,self.class2_counter,self.class3_counter = None, None, None
        self.clf = None
        self.proj_name = None
        self.root = None
        self.image1 = None