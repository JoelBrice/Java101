import tkinter as tk
import pandas as pd
import PyQt5 as qt
import numpy as np
import cv2

def getFace():
    frame = cv2.cap(0)
    while True:
        frame.dir("C:/users")
        
        