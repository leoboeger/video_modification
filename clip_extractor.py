# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:46:08 2021

@author: LeoBoeger
"""

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
import os

##############################################################################
### initial settings
 
video = input('set path of video: ')
ext_name = ['_TSrem','_TSwake',"_TSnrem"]
video_dir = os.path.dirname(video)
video_name = os.path.basename(video).split('.')[0]
print(video_name)

##############################################################################
### define functions 


def get_times(vid, folder, name, state):
    if vid.__contains__('avi') or vid.__contains__('mp4'):
        
        try:
            with open(os.path.join(folder,name+state+'.txt')) as f:
                Time = f.readlines()
                
            Time = [x.strip() for x in Time]
        except:
            query = input('proceed with processing of full video?\nyes/no: ')
            if query == 'yes':
                clip = VideoFileClip(vid)
                end = int(clip.fps * clip.duration)
                Time = [str(0)+'-'+str(end)]
            else:
                exit()
        
        return Time
        
def clock_writer(Time, folder, name, state):
    clock_lst = []
    for time in Time:
        starttime = int(time.split('-')[0])
        #endtime = int(time.split('-')[1])
        hh_st = starttime // 3600
        mm_st = (starttime - 3600 * hh_st)// 60
        ss_st = starttime -(60 * mm_st) - (3600 * hh_st)
        
        clock = str(hh_st)+':'+str(mm_st)+':'+str(ss_st)
        clock_lst.append(clock)
        
        with open(os.path.join(folder,name+state+'_clock.txt'), mode='wt', encoding='utf-8') as myfile:
            myfile.write('\n'.join(clock_lst))
        
    return clock_lst

def make_clips(Time, vid, folder, name, state, resize_w=None):   
        temp_clips = []
        for time in times:
            starttime = int(time.split('-')[0])
            endtime = int(time.split('-')[1])
            
            #new_name = name+'_'+str(starttime)+'sec'
            #new_path = os.path.join(folder,new_name+str(times.index(time)+1)+'.avi')
            
            #ffmpeg_extract_subclip(video, starttime, endtime, targetname = new_path)
            clip = VideoFileClip(vid)
            sub_clip = clip.subclip(starttime, endtime)
            
            if resize_w != None:
                orig_w = sub_clip.w
                #orig_h = sub_clip.h
                ratio = resize_w/orig_w
        
                sub_clip = sub_clip.resize(ratio)
                
            if len(times) >= 2:
                temp_clips.append(sub_clip)
            elif len(times) == 1:
                temp_clips = sub_clip
        
        out_path = os.path.join(folder,name+state+'.avi')
        final = concatenate_videoclips(temp_clips)
        final.ipython_display(width=480)
        final.write_videofile(out_path,codec='rawvideo')
        
        return out_path

##############################################################################
### call functions 
for stage in ext_name:
    
    times = get_times(video, video_dir, video_name, stage)
    
    clock_start = clock_writer(times, video_dir, video_name, stage)
    
    clip_out = make_clips(times, video, video_dir, video_name, stage, resize_w=320)
    print("the video clip was saved at", clip_out)
    
