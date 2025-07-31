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



# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'Noel_SocCuriosity'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': 'test',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1920, 1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\DUBITO\\Desktop\\noel_main_241112\\Noel_SocCuriosity.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color="'#212121'", colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = "'#212121'"
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Measuring frame rate, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
    from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib
    
    # --- Initialize components for Routine "INTRO" ---
    # Run 'Begin Experiment' code from code_intro
    from psychopy import event
    from psychopy.hardware import joystick
    from psychopy.core import getTime, wait
    import pandas as pd
    import pathlib
    import re
    import random
    import linecache
    import math
    
    #Import excel file
    #ForOpt = 0
    #data = pd.read_excel (r'C:\Users\Dubito\Desktop\Elaboration Exp\2nd stage\Sentence List.xlsx') 
    #ForOpt = pd.DataFrame(data, columns= ['ForOpt'])
    
    PhotoFolder = './Image Pool/'
    
    nJoys = joystick.getNumJoysticks()  
    id = 0
    joy = joystick.Joystick(id) 
    timer = core.Clock()
    
    
    #Global variable definition
    Elaboration_Flag = True
    
    Elaborationstart = 0
    Elaboration = 0
    Sentencestart = 0
    Sentencereading = 0
    
    Trial_Num = 1
    Write_Flag = True
    evalMultiplier = 0
    Joystick_Return_Flag = True
    
    win.mouseVisible=False
    
    choice = 0
    
    slider_satisfaction_Flag = True
    slider_aux_Flag = False
    slider_curiosity_Flag = True
    slider_knowledge_Flag = False
    
    
    Time_Rating = 1
    #Time_Rating is minute
    #Time_Allexp = 60
    TotalRatingDuration = 0
    
    text_intro = visual.TextStim(win=win, name='text_intro',
        text=' 第１セッションを開始します。\n\nJoystickのトリガーを引いて始めてください。',
        font='LINE Seed JP App_OTF Regular',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color="'#ffffff'", colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "SCREENING" ---
    header_list = visual.TextStim(win=win, name='header_list',
        text='',
        font='Trebuchet MS',
        pos=(0, 0.15), draggable=True, height=0.06, wrapWidth=1.5, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_q_knowledge = visual.TextStim(win=win, name='text_q_knowledge',
        text='How likely is it that you know the answer?',
        font='LINE Seed JP App_OTF Regular',
        pos=(0, -0.1), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color="'#d3d3d3'", colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    slider_knowledge = visual.Slider(win=win, name='slider_knowledge',
        startValue=0, size=(1.3, 0.02), pos=(0, -0.15), units=win.units,
        labels=('No Idea', '', '', '', '', 'Tip-of-the-Tongue'), ticks=(-2.5, -1.5, -0.5, 0.5, 1.5, 2.5), granularity=0.005,
        style='rating', styleTweaks=(), opacity=None,
        labelColor="'#d3d3d3'", markerColor="'#ffa500'", lineColor='#d3d3d3', colorSpace='rgb',
        font='Trebuchet MS', labelHeight=0.02,
        flip=False, ori=0.0, depth=-3, readOnly=False)
    text_q_precuriosity = visual.TextStim(win=win, name='text_q_precuriosity',
        text='How curious are you about the answer?',
        font='Arial',
        pos=(0, -0.3), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='#d3d3d3', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    slider_precuriosity = visual.Slider(win=win, name='slider_precuriosity',
        startValue=0, size=(1.3, 0.02), pos=(0, -0.35), units=win.units,
        labels=('0', '', '', '', '', '5'), ticks=(-2.5, -1.5, -0.5, 0.5, 1.5, 2.5), granularity=0.005,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor="'#ffa500'", lineColor='LightGray', colorSpace='rgb',
        font='Trebuchet MS', labelHeight=0.02,
        flip=False, ori=0.0, depth=-5, readOnly=False)
    
    # --- Initialize components for Routine "EXP_START" ---
    text_commence_exp = visual.TextStim(win=win, name='text_commence_exp',
        text='第１セッションが終わりました。\n\nトリガーを引くと第２セッションに入ります。',
        font='LINE Seed JP_OTF',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='#d3d3d3', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    x, y = [None, None]
    commence_exp = type('', (), {})() # Create an object to use as a name space
    commence_exp.device = None
    commence_exp.device_number = 0
    commence_exp.joystickClock = core.Clock()
    commence_exp.xFactor = 1
    commence_exp.yFactor = 1
    
    try:
        numJoysticks = joysticklib.getNumJoysticks()
        if numJoysticks > 0:
            try:
                joystickCache
            except NameError:
                joystickCache={}
            if not 0 in joystickCache:
                joystickCache[0] = joysticklib.Joystick(0)
            commence_exp.device = joystickCache[0]
            if win.units == 'height':
                commence_exp.xFactor = 0.5 * win.size[0]/win.size[1]
                commence_exp.yFactor = 0.5
        else:
            commence_exp.device = virtualjoysticklib.VirtualJoystick(0)
            logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(commence_exp.device_number))
    except Exception:
        pass
        
    if not commence_exp.device:
        logging.error('No joystick/gamepad device found.')
        core.quit()
    
    commence_exp.status = None
    commence_exp.clock = core.Clock()
    commence_exp.numButtons = commence_exp.device.getNumButtons()
    commence_exp.getNumButtons = commence_exp.device.getNumButtons
    commence_exp.getAllButtons = commence_exp.device.getAllButtons
    commence_exp.getX = lambda: commence_exp.xFactor * commence_exp.device.getX()
    commence_exp.getY = lambda: commence_exp.yFactor * commence_exp.device.getY()
    
    text = visual.TextStim(win=win, name='text',
        text='Trigger unlocks in 3...',
        font='LINE Seed JP_OTF',
        pos=(0, -0.3), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='#d3d3d3', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_2 = visual.TextStim(win=win, name='text_2',
        text='Trigger unlocks in 2...',
        font='LINE Seed JP_OTF',
        pos=(0, -0.3), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='#d3d3d3', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Trigger unlocks in 1...',
        font='LINE Seed JP_OTF',
        pos=(0, -0.3), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='#d3d3d3', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "FIXATION" ---
    # Run 'Begin Experiment' code from code_fixation
    #loopClock = core.Clock()
    polygon_2 = visual.ShapeStim(
        win=win, name='polygon_2', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor="'#ffffff'", fillColor="'#ffffff'",
        opacity=None, depth=-1.0, interpolate=True)
    
    # --- Initialize components for Routine "EXP_IMAGE" ---
    # Run 'Begin Experiment' code from code_exp_2
    import random
    
    # Generate a list of row indices (0 to 60 if your CSV has 61 rows)
    row_indices = list(range(6))
    
    # Randomly shuffle the indices
    random.shuffle(row_indices)
    
    # Select the first 30 indices
    selected_rows = row_indices[:3]
    
    # Convert the list of indices to a comma-separated string
    selected_rows_str = ','.join(map(str, selected_rows))
    image_exp = visual.ImageStim(
        win=win,
        name='image_exp', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.1, 0.5097),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    text_4 = visual.TextStim(win=win, name='text_4',
        text='Move right to continue ⇒',
        font='LINE Seed JP_OTF',
        pos=(0.41, -0.28), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color=[0.0039, 0.0039, 0.0039], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "EXP_RATING" ---
    text_q_satisfaction = visual.TextStim(win=win, name='text_q_satisfaction',
        text='How satisfied are you with the article provided?',
        font='LINE Seed JP_OTF',
        pos=(0, 0.35), draggable=False, height=0.04, wrapWidth=None, ori=0, 
        color='#d3d3d3', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    slider_satisfaction = visual.Slider(win=win, name='slider_satisfaction',
        startValue=0, size=(1.3, 0.02), pos=(0, 0.29), units=win.units,
        labels=('0', '', '', '', '', '5'), ticks=(-2.5, -1.5, -0.5, 0.5, 1.5, 2.5), granularity=0.005,
        style=['rating'], styleTweaks=(), opacity=1,
        labelColor='#d3d3d3', markerColor='Red', lineColor='#d3d3d3', colorSpace='rgb',
        font='LINE Seed JP_OTF', labelHeight=0.04,
        flip=False, ori=0, depth=-2, readOnly=False)
    text_q_postcuriosity = visual.TextStim(win=win, name='text_q_postcuriosity',
        text='How curious are you to learn more about this topic?',
        font='LINE Seed JP_OTF',
        pos=(0, 0.025), draggable=False, height=0.04, wrapWidth=None, ori=0, 
        color='#d3d3d3', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    slider_postcuriosity = visual.Slider(win=win, name='slider_postcuriosity',
        startValue=0, size=(1.3, 0.02), pos=(0, -0.03), units=win.units,
        labels=('0', '', '', '', '', '5'), ticks=(-2.5, -1.5, -0.5, 0.5, 1.5, 2.5), granularity=0.005,
        style=['rating'], styleTweaks=(), opacity=1,
        labelColor='#d3d3d3', markerColor='Red', lineColor='#d3d3d3', colorSpace='rgb',
        font='LINE Seed JP_OTF', labelHeight=0.04,
        flip=False, ori=0, depth=-4, readOnly=False)
    text_q_cogsocial = visual.TextStim(win=win, name='text_q_cogsocial',
        text='How many people liked this article?',
        font='LINE Seed JP_OTF',
        pos=(0, -0.29), draggable=False, height=0.04, wrapWidth=None, ori=0, 
        color='#d3d3d3', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-5.0);
    slider_cogsocial = visual.Slider(win=win, name='slider_cogsocial',
        startValue=0, size=(1.3, 0.02), pos=(0, -0.35), units=win.units,
        labels=('0', '', '', '', '', '5'), ticks=(-2.5, -1.5, -0.5, 0.5, 1.5, 2.5), granularity=0.005,
        style=['rating'], styleTweaks=(), opacity=1,
        labelColor='#d3d3d3', markerColor='Red', lineColor='#d3d3d3', colorSpace='rgb',
        font='LINE Seed JP_OTF', labelHeight=0.04,
        flip=False, ori=0, depth=-6, readOnly=False)
    
    # --- Initialize components for Routine "END" ---
    text_end_announce = visual.TextStim(win=win, name='text_end_announce',
        text='すべてのセッションが終わりました。',
        font='LINE Seed JP_OTF',
        pos=(0, 0.1), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    text_end_ty = visual.TextStim(win=win, name='text_end_ty',
        text='ご協力いただきありがとうございました。',
        font='LINE Seed JP_OTF',
        pos=(0, -0.1), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "INTRO" ---
    # create an object to store info about Routine INTRO
    INTRO = data.Routine(
        name='INTRO',
        components=[text_intro],
    )
    INTRO.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for INTRO
    INTRO.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    INTRO.tStart = globalClock.getTime(format='float')
    INTRO.status = STARTED
    INTRO.maxDuration = None
    # keep track of which components have finished
    INTROComponents = INTRO.components
    for thisComponent in INTRO.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "INTRO" ---
    INTRO.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_intro
        if joy.getButton(0) == True:
            continueRoutine = False
            Joystick_Return_Flag = False
        
        win.mouseVisible=False
        
        # *text_intro* updates
        
        # if text_intro is starting this frame...
        if text_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_intro.frameNStart = frameN  # exact frame index
            text_intro.tStart = t  # local t and not account for scr refresh
            text_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_intro, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_intro.status = STARTED
            text_intro.setAutoDraw(True)
        
        # if text_intro is active this frame...
        if text_intro.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            INTRO.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in INTRO.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "INTRO" ---
    for thisComponent in INTRO.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for INTRO
    INTRO.tStop = globalClock.getTime(format='float')
    INTRO.tStopRefresh = tThisFlipGlobal
    # Run 'End Routine' code from code_intro
    Time_start = timer.getTime()
    thisExp.nextEntry()
    # the Routine "INTRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    screening_loop = data.TrialHandler2(
        name='screening_loop',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('header_list.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(screening_loop)  # add the loop to the experiment
    thisScreening_loop = screening_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisScreening_loop.rgb)
    if thisScreening_loop != None:
        for paramName in thisScreening_loop:
            globals()[paramName] = thisScreening_loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisScreening_loop in screening_loop:
        currentLoop = screening_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisScreening_loop.rgb)
        if thisScreening_loop != None:
            for paramName in thisScreening_loop:
                globals()[paramName] = thisScreening_loop[paramName]
        
        # --- Prepare to start Routine "SCREENING" ---
        # create an object to store info about Routine SCREENING
        SCREENING = data.Routine(
            name='SCREENING',
            components=[header_list, text_q_knowledge, slider_knowledge, text_q_precuriosity, slider_precuriosity],
        )
        SCREENING.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_screening
        
            
        startRoutine = timer.getTime()
        Joystick_Flag = False
        
        slider_knowledge_Flag = True
        slider_precuriosity_Flag = False
        
        slider_precuriosity.markerPos = 0
        slider_knowledge.markerPos = 0
        header_list.setText(Header)
        slider_knowledge.reset()
        slider_precuriosity.reset()
        # store start times for SCREENING
        SCREENING.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        SCREENING.tStart = globalClock.getTime(format='float')
        SCREENING.status = STARTED
        SCREENING.maxDuration = None
        # keep track of which components have finished
        SCREENINGComponents = SCREENING.components
        for thisComponent in SCREENING.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "SCREENING" ---
        # if trial has changed, end Routine now
        if isinstance(screening_loop, data.TrialHandler2) and thisScreening_loop.thisN != screening_loop.thisTrial.thisN:
            continueRoutine = False
        SCREENING.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_screening
            currentAxisVal = joy.getAxis(0)
            
            
            if Joystick_Return_Flag:
                if currentAxisVal >  0.1 or currentAxisVal < -0.1:
                    Joystick_Flag = True
            else:
                if currentAxisVal <  0.1 and currentAxisVal > -0.1:
                    Joystick_Return_Flag = True
            
            
            
            if Joystick_Flag and joy.getButton(0) == True:
                if slider_knowledge_Flag:
                    slider_knowledge_RT = timer.getTime() - startRoutine
                    knowledge_time = timer.getTime()
                    slider_knowledge.markerPos = currentAxisVal * 2.65
                    slider_knowledge_Flag = False
                    slider_precuriosity_Flag = True
                    slider_precuriosity.markerPos = 0
                    Joystick_Flag = False
                    Joystick_Return_Flag = False
                elif slider_precuriosity_Flag:
                    slider_precuriosity_RT = timer.getTime() - knowledge_time
                    precuriosity_time = timer.getTime()
                    slider_precuriosity.markerPos = currentAxisVal * 2.65
                    slider_precuriosity_Flag = False
                    Joystick_Flag = False
                    Joystick_Return_Flag = False
                    continueRoutine = False
                    
            
                
            elif Joystick_Flag:
                if slider_precuriosity_Flag:
                    slider_precuriosity.markerPos = currentAxisVal * 2.65
                elif slider_knowledge_Flag:
                    slider_knowledge.markerPos = currentAxisVal * 2.65
            
            #elif slider_makesense_Flag:
            #    slider_makesense.markerPos = 0
            
            
            
            #VerticalAxisVal = joy.getAxis(1)
            
            
            
            
            
            
            
            
            
            
            # *header_list* updates
            
            # if header_list is starting this frame...
            if header_list.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                header_list.frameNStart = frameN  # exact frame index
                header_list.tStart = t  # local t and not account for scr refresh
                header_list.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(header_list, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'header_list.started')
                # update status
                header_list.status = STARTED
                header_list.setAutoDraw(True)
            
            # if header_list is active this frame...
            if header_list.status == STARTED:
                # update params
                pass
            
            # *text_q_knowledge* updates
            
            # if text_q_knowledge is starting this frame...
            if text_q_knowledge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_q_knowledge.frameNStart = frameN  # exact frame index
                text_q_knowledge.tStart = t  # local t and not account for scr refresh
                text_q_knowledge.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_q_knowledge, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_q_knowledge.status = STARTED
                text_q_knowledge.setAutoDraw(True)
            
            # if text_q_knowledge is active this frame...
            if text_q_knowledge.status == STARTED:
                # update params
                pass
            
            # *slider_knowledge* updates
            
            # if slider_knowledge is starting this frame...
            if slider_knowledge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_knowledge.frameNStart = frameN  # exact frame index
                slider_knowledge.tStart = t  # local t and not account for scr refresh
                slider_knowledge.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_knowledge, 'tStartRefresh')  # time at next scr refresh
                # update status
                slider_knowledge.status = STARTED
                slider_knowledge.setAutoDraw(True)
            
            # if slider_knowledge is active this frame...
            if slider_knowledge.status == STARTED:
                # update params
                pass
            
            # *text_q_precuriosity* updates
            
            # if text_q_precuriosity is starting this frame...
            if text_q_precuriosity.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_q_precuriosity.frameNStart = frameN  # exact frame index
                text_q_precuriosity.tStart = t  # local t and not account for scr refresh
                text_q_precuriosity.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_q_precuriosity, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_q_precuriosity.status = STARTED
                text_q_precuriosity.setAutoDraw(True)
            
            # if text_q_precuriosity is active this frame...
            if text_q_precuriosity.status == STARTED:
                # update params
                pass
            
            # *slider_precuriosity* updates
            
            # if slider_precuriosity is starting this frame...
            if slider_precuriosity.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_precuriosity.frameNStart = frameN  # exact frame index
                slider_precuriosity.tStart = t  # local t and not account for scr refresh
                slider_precuriosity.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_precuriosity, 'tStartRefresh')  # time at next scr refresh
                # update status
                slider_precuriosity.status = STARTED
                slider_precuriosity.setAutoDraw(True)
            
            # if slider_precuriosity is active this frame...
            if slider_precuriosity.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                SCREENING.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SCREENING.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SCREENING" ---
        for thisComponent in SCREENING.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for SCREENING
        SCREENING.tStop = globalClock.getTime(format='float')
        SCREENING.tStopRefresh = tThisFlipGlobal
        # Run 'End Routine' code from code_screening
        #evalScore = (evalScore*evalMultiplier)
        
        
        
        thisExp.addData('Knowledge Score',slider_knowledge.markerPos)
        
        thisExp.addData('slider_knowledge_RT',slider_knowledge_RT )
        
        thisExp.addData('Pre-Curiosity Score',slider_precuriosity.markerPos)
        
        thisExp.addData('slider_precuriosity_RT',slider_precuriosity_RT )
        
        # the Routine "SCREENING" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'screening_loop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "EXP_START" ---
    # create an object to store info about Routine EXP_START
    EXP_START = data.Routine(
        name='EXP_START',
        components=[text_commence_exp, commence_exp, text, text_2, text_3],
    )
    EXP_START.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    commence_exp.oldButtonState = commence_exp.device.getAllButtons()[:]
    commence_exp.activeButtons=[i for i in range(commence_exp.numButtons)]
    # setup some python lists for storing info about the commence_exp
    gotValidClick = False  # until a click is received
    # store start times for EXP_START
    EXP_START.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EXP_START.tStart = globalClock.getTime(format='float')
    EXP_START.status = STARTED
    EXP_START.maxDuration = None
    # keep track of which components have finished
    EXP_STARTComponents = EXP_START.components
    for thisComponent in EXP_START.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EXP_START" ---
    EXP_START.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_commence_exp* updates
        
        # if text_commence_exp is starting this frame...
        if text_commence_exp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_commence_exp.frameNStart = frameN  # exact frame index
            text_commence_exp.tStart = t  # local t and not account for scr refresh
            text_commence_exp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_commence_exp, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_commence_exp.status = STARTED
            text_commence_exp.setAutoDraw(True)
        
        # if text_commence_exp is active this frame...
        if text_commence_exp.status == STARTED:
            # update params
            pass
        # *commence_exp* updates
        
        # if commence_exp is starting this frame...
        if commence_exp.status == NOT_STARTED and t >= 3-frameTolerance:
            # keep track of start time/frame for later
            commence_exp.frameNStart = frameN  # exact frame index
            commence_exp.tStart = t  # local t and not account for scr refresh
            commence_exp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(commence_exp, 'tStartRefresh')  # time at next scr refresh
            # update status
            commence_exp.status = STARTED
            commence_exp.status = STARTED
            commence_exp.joystickClock.reset()
        if commence_exp.status == STARTED:  # only update if started and not finished!
            commence_exp.newButtonState = commence_exp.getAllButtons()[:]
            if commence_exp.newButtonState != commence_exp.oldButtonState: # New button press
                commence_exp.pressedButtons = [i for i in range(commence_exp.numButtons) if commence_exp.newButtonState[i] and not commence_exp.oldButtonState[i]]
                commence_exp.releasedButtons = [i for i in range(commence_exp.numButtons) if not commence_exp.newButtonState[i] and commence_exp.oldButtonState[i]]
                commence_exp.newPressedButtons = [i for i in commence_exp.activeButtons if i in commence_exp.pressedButtons]
                commence_exp.oldButtonState = commence_exp.newButtonState
                commence_exp.buttons = commence_exp.newPressedButtons
                [logging.data("joystick_{}_button: {}, pos=({:1.4f},{:1.4f})".format(commence_exp.device_number, i, commence_exp.getX(), commence_exp.getY())) for i in commence_exp.pressedButtons]
                if len(commence_exp.buttons) > 0:  # state changed to a new click
                    # abort routine on response
                    continueRoutine = False
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.tStopRefresh = tThisFlipGlobal  # on global time
                text.frameNStop = frameN  # exact frame index
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.tStopRefresh = tThisFlipGlobal  # on global time
                text_2.frameNStop = frameN  # exact frame index
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EXP_START.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EXP_START.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EXP_START" ---
    for thisComponent in EXP_START.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EXP_START
    EXP_START.tStop = globalClock.getTime(format='float')
    EXP_START.tStopRefresh = tThisFlipGlobal
    # Run 'End Routine' code from code_start
    Time_rating_start = timer.getTime()
    # store data for thisExp (ExperimentHandler)
    # store data for thisExp (ExperimentHandler)
    x, y = commence_exp.getX(), commence_exp.getY()
    commence_exp.newButtonState = commence_exp.getAllButtons()[:]
    commence_exp.pressedState = [commence_exp.newButtonState[i] for i in range(commence_exp.numButtons)]
    commence_exp.time = commence_exp.joystickClock.getTime()
    thisExp.addData('commence_exp.x', x)
    thisExp.addData('commence_exp.y', y)
    [thisExp.addData('commence_exp.button_{0}'.format(i), int(commence_exp.pressedState[i])) for i in commence_exp.activeButtons]
    thisExp.addData('commence_exp.time', commence_exp.time)
    thisExp.nextEntry()
    # the Routine "EXP_START" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    exp_trials = data.TrialHandler2(
        name='exp_trials',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(
        'image_list.xlsx', 
        selection=selected_rows_str
    )
    , 
        seed=None, 
    )
    thisExp.addLoop(exp_trials)  # add the loop to the experiment
    thisExp_trial = exp_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp_trial.rgb)
    if thisExp_trial != None:
        for paramName in thisExp_trial:
            globals()[paramName] = thisExp_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisExp_trial in exp_trials:
        currentLoop = exp_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisExp_trial.rgb)
        if thisExp_trial != None:
            for paramName in thisExp_trial:
                globals()[paramName] = thisExp_trial[paramName]
        
        # --- Prepare to start Routine "FIXATION" ---
        # create an object to store info about Routine FIXATION
        FIXATION = data.Routine(
            name='FIXATION',
            components=[polygon_2],
        )
        FIXATION.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_fixation
        #if exp_trials.thisN == 0:
        #    loopClock.reset()
        # store start times for FIXATION
        FIXATION.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        FIXATION.tStart = globalClock.getTime(format='float')
        FIXATION.status = STARTED
        FIXATION.maxDuration = 2
        # keep track of which components have finished
        FIXATIONComponents = FIXATION.components
        for thisComponent in FIXATION.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "FIXATION" ---
        # if trial has changed, end Routine now
        if isinstance(exp_trials, data.TrialHandler2) and thisExp_trial.thisN != exp_trials.thisTrial.thisN:
            continueRoutine = False
        FIXATION.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > FIXATION.maxDuration-frameTolerance:
                FIXATION.maxDurationReached = True
                continueRoutine = False
            # Run 'Each Frame' code from code_fixation
            Time_current = timer.getTime()-Time_rating_start
            
                
            
            # Define the time limit in seconds
            #loopTimeLimit = 60  # Replace XX with the desired duration in seconds
            
            # Check if the time limit has been exceeded
            #if loopClock.getTime() >= loopTimeLimit:
            
            
            # *polygon_2* updates
            
            # if polygon_2 is starting this frame...
            if polygon_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                polygon_2.frameNStart = frameN  # exact frame index
                polygon_2.tStart = t  # local t and not account for scr refresh
                polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_2.status = STARTED
                polygon_2.setAutoDraw(True)
            
            # if polygon_2 is active this frame...
            if polygon_2.status == STARTED:
                # update params
                pass
            
            # if polygon_2 is stopping this frame...
            if polygon_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_2.tStop = t  # not accounting for scr refresh
                    polygon_2.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_2.frameNStop = frameN  # exact frame index
                    # update status
                    polygon_2.status = FINISHED
                    polygon_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                FIXATION.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FIXATION.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "FIXATION" ---
        for thisComponent in FIXATION.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for FIXATION
        FIXATION.tStop = globalClock.getTime(format='float')
        FIXATION.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if FIXATION.maxDurationReached:
            routineTimer.addTime(-FIXATION.maxDuration)
        elif FIXATION.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "EXP_IMAGE" ---
        # create an object to store info about Routine EXP_IMAGE
        EXP_IMAGE = data.Routine(
            name='EXP_IMAGE',
            components=[image_exp, text_4],
        )
        EXP_IMAGE.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_exp_2
        
            
        startRoutine = timer.getTime()
        Joystick_Flag = False
        
        
        
        slider_satisfaction_Flag = True
        slider_aux_Flag = False
        
        
        slider_satisfaction.markerPos = 2.5
        
        image_exp.setImage('image_pool/' + imageFile)
        # store start times for EXP_IMAGE
        EXP_IMAGE.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        EXP_IMAGE.tStart = globalClock.getTime(format='float')
        EXP_IMAGE.status = STARTED
        EXP_IMAGE.maxDuration = None
        # keep track of which components have finished
        EXP_IMAGEComponents = EXP_IMAGE.components
        for thisComponent in EXP_IMAGE.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "EXP_IMAGE" ---
        # if trial has changed, end Routine now
        if isinstance(exp_trials, data.TrialHandler2) and thisExp_trial.thisN != exp_trials.thisTrial.thisN:
            continueRoutine = False
        EXP_IMAGE.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_exp_2
            currentAxisVal = joy.getAxis(0)
            
            
            if Joystick_Return_Flag:
                if currentAxisVal >  0.1 or currentAxisVal < -0.1:
                    Joystick_Flag = True
            else:
                if currentAxisVal <  0.1 and currentAxisVal > -0.1:
                    Joystick_Return_Flag = True
            
            if currentAxisVal > 0.5:
                continueRoutine = False
            
            
            #if Joystick_Flag and joy.getButton(0) == True:
            #    if slider_satisfaction_Flag:
            #        slider_satisfaction_RT = timer.getTime() - startRoutine
            #        satisfaction_time = timer.getTime()
            #        slider_satisfaction.markerPos = currentAxisVal * 40
            #        slider_satisfaction_Flag = False
            #        slider_aux_Flag = True
            #        slider_aux.markerPos = 3
            #        Joystick_Flag = False
            #        Joystick_Return_Flag = False
            #    elif slider_aux_Flag:
            #        slider_aux_RT = timer.getTime() - satisfaction_time
            #        aux_time = timer.getTime()
            #        slider_aux.markerPos = currentAxisVal * 40
            #        slider_aux_Flag = False
            #        Joystick_Flag = False
            #        Joystick_Return_Flag = False
            #        continueRoutine = False
            
            
                
            #elif Joystick_Flag:
            #    if slider_satisfaction_Flag:
            #        slider_satisfaction.markerPos = currentAxisVal * 40
            #    elif slider_aux_Flag:
            #        slider_aux.markerPos = currentAxisVal * 40
            
            ##elif slider_makesense_Flag:
            ##    slider_makesense.markerPos = 0
            
            
            
            ##VerticalAxisVal = joy.getAxis(1)
            
            
            
            
            
            
            
            
            
            
            # *image_exp* updates
            
            # if image_exp is starting this frame...
            if image_exp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_exp.frameNStart = frameN  # exact frame index
                image_exp.tStart = t  # local t and not account for scr refresh
                image_exp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_exp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_exp.started')
                # update status
                image_exp.status = STARTED
                image_exp.setAutoDraw(True)
            
            # if image_exp is active this frame...
            if image_exp.status == STARTED:
                # update params
                pass
            
            # *text_4* updates
            
            # if text_4 is starting this frame...
            if text_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_4.status = STARTED
                text_4.setAutoDraw(True)
            
            # if text_4 is active this frame...
            if text_4.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                EXP_IMAGE.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EXP_IMAGE.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "EXP_IMAGE" ---
        for thisComponent in EXP_IMAGE.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for EXP_IMAGE
        EXP_IMAGE.tStop = globalClock.getTime(format='float')
        EXP_IMAGE.tStopRefresh = tThisFlipGlobal
        # Run 'End Routine' code from code_exp_2
        #evalScore = (evalScore*evalMultiplier)
        
        
        
        #thisExp.addData('Satisfaction Score',slider_satisfaction.markerPos)
        #thisExp.addData('MoreCurious Score',slider_aux.markerPos )
        
        #thisExp.addData('slider_Satisfaction_RT',slider_satisfaction_RT )
        #thisExp.addData('slider_MoreCurious_RT',slider_aux_RT )
        
        # the Routine "EXP_IMAGE" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "EXP_RATING" ---
        # create an object to store info about Routine EXP_RATING
        EXP_RATING = data.Routine(
            name='EXP_RATING',
            components=[text_q_satisfaction, slider_satisfaction, text_q_postcuriosity, slider_postcuriosity, text_q_cogsocial, slider_cogsocial],
        )
        EXP_RATING.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_exp
        
            
        startRoutine = timer.getTime()
        Joystick_Flag = False
        
        
        
        slider_satisfaction_Flag = True
        slider_postcuriosity_Flag = False
        slider_cogsocial_Flag = False
        
        
        slider_satisfaction.markerPos = 0
        slider_postcuriosity.markerPos = 0
        slider_cogsocial.markerPos = 0
        
        slider_satisfaction.reset()
        slider_postcuriosity.reset()
        slider_cogsocial.reset()
        # store start times for EXP_RATING
        EXP_RATING.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        EXP_RATING.tStart = globalClock.getTime(format='float')
        EXP_RATING.status = STARTED
        EXP_RATING.maxDuration = None
        # keep track of which components have finished
        EXP_RATINGComponents = EXP_RATING.components
        for thisComponent in EXP_RATING.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "EXP_RATING" ---
        # if trial has changed, end Routine now
        if isinstance(exp_trials, data.TrialHandler2) and thisExp_trial.thisN != exp_trials.thisTrial.thisN:
            continueRoutine = False
        EXP_RATING.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_exp
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
            
            #elif slider_makesense_Flag:
            #    slider_makesense.markerPos = 0
            
            
            
            #VerticalAxisVal = joy.getAxis(1)
            
            
            
            
            
            
            
            
            
            
            # *text_q_satisfaction* updates
            
            # if text_q_satisfaction is starting this frame...
            if text_q_satisfaction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_q_satisfaction.frameNStart = frameN  # exact frame index
                text_q_satisfaction.tStart = t  # local t and not account for scr refresh
                text_q_satisfaction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_q_satisfaction, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_q_satisfaction.status = STARTED
                text_q_satisfaction.setAutoDraw(True)
            
            # if text_q_satisfaction is active this frame...
            if text_q_satisfaction.status == STARTED:
                # update params
                pass
            
            # *slider_satisfaction* updates
            
            # if slider_satisfaction is starting this frame...
            if slider_satisfaction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_satisfaction.frameNStart = frameN  # exact frame index
                slider_satisfaction.tStart = t  # local t and not account for scr refresh
                slider_satisfaction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_satisfaction, 'tStartRefresh')  # time at next scr refresh
                # update status
                slider_satisfaction.status = STARTED
                slider_satisfaction.setAutoDraw(True)
            
            # if slider_satisfaction is active this frame...
            if slider_satisfaction.status == STARTED:
                # update params
                pass
            
            # *text_q_postcuriosity* updates
            
            # if text_q_postcuriosity is starting this frame...
            if text_q_postcuriosity.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_q_postcuriosity.frameNStart = frameN  # exact frame index
                text_q_postcuriosity.tStart = t  # local t and not account for scr refresh
                text_q_postcuriosity.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_q_postcuriosity, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_q_postcuriosity.status = STARTED
                text_q_postcuriosity.setAutoDraw(True)
            
            # if text_q_postcuriosity is active this frame...
            if text_q_postcuriosity.status == STARTED:
                # update params
                pass
            
            # *slider_postcuriosity* updates
            
            # if slider_postcuriosity is starting this frame...
            if slider_postcuriosity.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_postcuriosity.frameNStart = frameN  # exact frame index
                slider_postcuriosity.tStart = t  # local t and not account for scr refresh
                slider_postcuriosity.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_postcuriosity, 'tStartRefresh')  # time at next scr refresh
                # update status
                slider_postcuriosity.status = STARTED
                slider_postcuriosity.setAutoDraw(True)
            
            # if slider_postcuriosity is active this frame...
            if slider_postcuriosity.status == STARTED:
                # update params
                pass
            
            # *text_q_cogsocial* updates
            
            # if text_q_cogsocial is starting this frame...
            if text_q_cogsocial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_q_cogsocial.frameNStart = frameN  # exact frame index
                text_q_cogsocial.tStart = t  # local t and not account for scr refresh
                text_q_cogsocial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_q_cogsocial, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_q_cogsocial.status = STARTED
                text_q_cogsocial.setAutoDraw(True)
            
            # if text_q_cogsocial is active this frame...
            if text_q_cogsocial.status == STARTED:
                # update params
                pass
            
            # *slider_cogsocial* updates
            
            # if slider_cogsocial is starting this frame...
            if slider_cogsocial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_cogsocial.frameNStart = frameN  # exact frame index
                slider_cogsocial.tStart = t  # local t and not account for scr refresh
                slider_cogsocial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_cogsocial, 'tStartRefresh')  # time at next scr refresh
                # update status
                slider_cogsocial.status = STARTED
                slider_cogsocial.setAutoDraw(True)
            
            # if slider_cogsocial is active this frame...
            if slider_cogsocial.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                EXP_RATING.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EXP_RATING.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "EXP_RATING" ---
        for thisComponent in EXP_RATING.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for EXP_RATING
        EXP_RATING.tStop = globalClock.getTime(format='float')
        EXP_RATING.tStopRefresh = tThisFlipGlobal
        # Run 'End Routine' code from code_exp
        #evalScore = (evalScore*evalMultiplier)
        
        
        
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
        
        # the Routine "EXP_RATING" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'exp_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "END" ---
    # create an object to store info about Routine END
    END = data.Routine(
        name='END',
        components=[text_end_announce, text_end_ty],
    )
    END.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for END
    END.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    END.tStart = globalClock.getTime(format='float')
    END.status = STARTED
    END.maxDuration = None
    # keep track of which components have finished
    ENDComponents = END.components
    for thisComponent in END.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "END" ---
    END.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_end_announce* updates
        
        # if text_end_announce is starting this frame...
        if text_end_announce.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_end_announce.frameNStart = frameN  # exact frame index
            text_end_announce.tStart = t  # local t and not account for scr refresh
            text_end_announce.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_end_announce, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_end_announce.status = STARTED
            text_end_announce.setAutoDraw(True)
        
        # if text_end_announce is active this frame...
        if text_end_announce.status == STARTED:
            # update params
            pass
        
        # if text_end_announce is stopping this frame...
        if text_end_announce.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_end_announce.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_end_announce.tStop = t  # not accounting for scr refresh
                text_end_announce.tStopRefresh = tThisFlipGlobal  # on global time
                text_end_announce.frameNStop = frameN  # exact frame index
                # update status
                text_end_announce.status = FINISHED
                text_end_announce.setAutoDraw(False)
        
        # *text_end_ty* updates
        
        # if text_end_ty is starting this frame...
        if text_end_ty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_end_ty.frameNStart = frameN  # exact frame index
            text_end_ty.tStart = t  # local t and not account for scr refresh
            text_end_ty.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_end_ty, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_end_ty.status = STARTED
            text_end_ty.setAutoDraw(True)
        
        # if text_end_ty is active this frame...
        if text_end_ty.status == STARTED:
            # update params
            pass
        
        # if text_end_ty is stopping this frame...
        if text_end_ty.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_end_ty.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_end_ty.tStop = t  # not accounting for scr refresh
                text_end_ty.tStopRefresh = tThisFlipGlobal  # on global time
                text_end_ty.frameNStop = frameN  # exact frame index
                # update status
                text_end_ty.status = FINISHED
                text_end_ty.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            END.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in END.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "END" ---
    for thisComponent in END.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for END
    END.tStop = globalClock.getTime(format='float')
    END.tStopRefresh = tThisFlipGlobal
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if END.maxDurationReached:
        routineTimer.addTime(-END.maxDuration)
    elif END.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
