# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 15:56:19 2021

@author: LeoBoeger
"""

from moviepy.editor import *
import os

file_path = input('file path: ')
folder = os.path.dirname(file_path)
name = os.path.basename(file_path).split('.')[0]

clip = VideoFileClip(file_path).subclip

orig_w = clip.w
orig_h = clip.h


desired_w = 320
ratio = desired_w/orig_w

resized_clip = clip.resize(ratio)

resized_clip.write_videofile(os.path.join(folder,name+'_resized'+'.avi'),codec='rawvideo')
    
