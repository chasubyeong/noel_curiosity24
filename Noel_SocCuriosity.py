#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on November 14, 2024, at 23:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'pyo'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_intro
from psychopy import visual

# ====== START: Modified for Curiosity24 ======
try:
    participant_id = int(expInfo['participant'])
except ValueError:
    participant_id = 0  # Default seed if participant ID is not a number

random.seed(participant_id)

import pandas as pd
import random

# Load the conditions file
conditions_df = pd.read_excel('post_list_original.xlsx')

# Get the unique post numbers
all_posts = conditions_df['post_num'].unique().tolist()

# Define the number of posts to display
num_posts_to_show = 50  # Adjust as needed

# Ensure that num_posts_to_show is less than or equal to the total number of posts
if num_posts_to_show > len(all_posts):
    raise ValueError("Number of posts to show cannot exceed the total number of available posts.")

# Randomly select posts
selected_posts = random.sample(all_posts, num_posts_to_show)

# Shuffle the selected posts
random.shuffle(selected_posts)

# Calculate half of the posts for balance
half = num_posts_to_show // 2

# Assign conditions
HiSC_posts = selected_posts[:half]  # First half assigned to HiSC
LoSC_posts = selected_posts[half:]  # Second half assigned to LoSC

# Create a list to store the indices of the selected trials
selectedRows = []

# Iterate over the DataFrame to find matching rows
for idx, row in conditions_df.iterrows():
    if row['post_num'] in HiSC_posts and row['condition'] == 'HiSC':
        selectedRows.append(idx)
    elif row['post_num'] in LoSC_posts and row['condition'] == 'LoSC':
        selectedRows.append(idx)

# Shuffle the selectedRows to randomize trial order
random.shuffle(selectedRows)
# ====== END: Modified for Curiosity24 ======

# --- Setup global variables (available in all functions) ---
# ... [rest of file unchanged until next modified block] ...

# === Later in code (e.g. inside routines) ===

# ====== START: Modified for Curiosity24 ======
currentAxisVal = joy.getAxis(0)

if Joystick_Return_Flag:
    if currentAxisVal >  0.1 or currentAxisVal < -0.1:
        Joystick_Flag = True
else:
    if currentAxisVal <  0.1 and currentAxisVal > -0.1:
        Joystick_Return_Flag = True

if currentAxisVal > 0.7:
    continueRoutine = False
# ====== END: Modified for Curiosity24 ======

# ====== START: Modified for Curiosity24 ======
if Joystick_Flag and joy.getButton(0) == True:
    if slider_satisfaction_Flag:
        slider_satisfaction_RT = timer.getTime() - startRoutine
        satisfaction_time = timer.getTime()
        slider_satisfaction.markerPos = currentAxisVal * 40
        slider_satisfaction_Flag = False
        slider_aux_Flag = True
        slider_aux.markerPos = 3
        Joystick_Flag = False
        Joystick_Return_Flag = False
    elif slider_aux_Flag:
        slider_aux_RT = timer.getTime() - satisfaction_time
        aux_time = timer.getTime()
        slider_aux.markerPos = currentAxisVal * 40
        slider_aux_Flag = False
        Joystick_Flag = False
        Joystick_Return_Flag = False
        continueRoutine = False

elif Joystick_Flag:
    if slider_satisfaction_Flag:
        slider_satisfaction.markerPos = currentAxisVal * 40
    elif slider_aux_Flag:
        slider_aux.markerPos = currentAxisVal * 40

#VerticalAxisVal = joy.getAxis(1)
# ====== END: Modified for Curiosity24 ======

# ====== START: Modified for Curiosity24 ======
expImageDuration = expImageClock.getTime()
thisExp.addData('Post RT', expImageDuration)
# ====== END: Modified for Curiosity24 ======

# ====== START: Modified for Curiosity24 ======
startRoutine = timer.getTime()
Joystick_Flag = False

slider_satisfaction_Flag = True
slider_postcuriosity_Flag = False
slider_cogsocial_Flag = False

slider_satisfaction.markerPos = 0
slider_postcuriosity.markerPos = 0
slider_cogsocial.markerPos = 0
# ====== END: Modified for Curiosity24 ======

# ====== START: Modified for Curiosity24 ======
currentAxisVal = joy.getAxis(0)

if Joystick_Return_Flag:
    if currentAxisVal >  0.1 or currentAxisVal < -0.1:
        Joystick_Flag = True
else:
    if currentAxisVal <  0.1 and currentAxisVal > -0.1:
        Joystick_Return_Flag = True

if Joystick_Flag and joy.getButton(0) == True:
    if slider_satisfaction_Flag:
        slider_satisfaction_RT = timer.getTime() - startRoutine
        satisfaction_time = timer.getTime()
        slider_satisfaction.markerPos = currentAxisVal * 2.65
        slider_satisfaction_Flag = False
        slider_postcuriosity_Flag = True
        slider_postcuriosity.markerPos = 0
        Joystick_Flag = False
        Joystick_Return_Flag = False
    elif slider_postcuriosity_Flag:
        slider_postcuriosity_RT = timer.getTime() - satisfaction_time
        postcuriosity_time = timer.getTime()
        slider_postcuriosity.markerPos = currentAxisVal * 2.65
        slider_postcuriosity_Flag = False
        slider_cogsocial_Flag = True
        slider_cogsocial.markerPos = 0
        Joystick_Flag = False
        Joystick_Return_Flag = False
    elif slider_cogsocial_Flag:
        slider_cogsocial_RT = timer.getTime() - postcuriosity_time
        cogsocial_time = timer.getTime()
        slider_cogsocial.markerPos = currentAxisVal * 2.65
        slider_cogsocial_Flag = False
        Joystick_Flag = False
        Joystick_Return_Flag = False
        continueRoutine = False

elif Joystick_Flag:
    if slider_satisfaction_Flag:
        slider_satisfaction.markerPos = currentAxisVal * 2.65
    elif slider_postcuriosity_Flag:
        slider_postcuriosity.markerPos = currentAxisVal * 2.65
    elif slider_cogsocial_Flag:
        slider_cogsocial.markerPos = currentAxisVal * 2.65

#VerticalAxisVal = joy.getAxis(1)
# ====== END: Modified for Curiosity24 ======

# ====== START: Modified for Curiosity24 ======
thisExp.addData('Satisfaction Score',slider_satisfaction.markerPos)
thisExp.addData('Post-Curious Score',slider_postcuriosity.markerPos )
thisExp.addData('CogSocial Score',slider_cogsocial.markerPos )

thisExp.addData('slider_Satisfaction_RT',slider_satisfaction_RT )
thisExp.addData('slider_postcuriosity_RT',slider_postcuriosity_RT )
thisExp.addData('slider_cogsocial_RT',slider_cogsocial_RT )

#TotalRatingDuration = timer.getTime()-Time_rating_start

#if TotalRatingDuration >= Time_Rating * 60:
#    exp_trials.finished = True  # Ends the loop
#    continueRoutine = False       # Ends the current routine
#    thisExp.addData('TotalRatingDuration', TotalRatingDuration)
# ====== END: Modified for Curiosity24 ======

# ... [rest of file unchanged] ...