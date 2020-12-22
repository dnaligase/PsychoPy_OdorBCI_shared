#Codemap
#port settings -- 106
#odor list -- 119
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Oct 20, 2020, at 15:35
If you publish work using this script the most relevant publication is:
    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y
"""
#comment1:
from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
from psychopy.hardware import keyboard
from psychopy import gui
from colorama import init, Fore, Style, Back
init(autoreset=True)
#image_for_study="stimulus/bsbtbzrc.jpeg"
study_order=[0,1,2,3]
keys=['up','right','down','left']
pressedCorrect_counter = 0
#comment2
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'smell_experiment_main'  # from the Builder filename that created this script
# expInfo = {'Name': '', 'age': '', 'sex': '', 'isCycle': 'None', 'session': '01'}
keys_experiment = ['name', 'age', 'sex', 'isMenPhase', 'session']

myDlg = gui.Dlg(title="CUBE: The Smell Experiment")
myDlg.addText('Subject info')
myDlg.addField('Name:')
myDlg.addField('Age:', 21)
myDlg.addField('Sex:', choices=['Female', 'Male'])

myDlg.addText('Additional Info')
myDlg.addField('isMenstrual:', initial=False, tip="Check the box for subjects in their menstrual phase.")
myDlg.addField('Session:', 1)

ok_data = myDlg.show()  # show dialog and wait for OK or Cancel
# dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=True, title=expName)
if myDlg.OK == False:
    core.quit()  # user pressed cancel
else:
    print(ok_data)

expInfo = {key:value for key, value in zip(keys_experiment, ok_data)}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['name'], expName, expInfo['date'])
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/gric-gosha/Desktop/PsychoPy_env',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame
# Start Code - component code to be run before the window creation
# Setup the Window
win = visual.Window(
    size=(612, 384), fullscr=False, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()
# Initialize components for Routine "code_initial"
code_initialClock = core.Clock()
"""
"""
#comment2end
import random
import serial
from time import sleep
#port settings
settings = {"port": "COM6",
                  "baudrate": 115200,
                  "timeout": 1}
#randomize random
random.seed()
#initialize list for smells
smells=[1,2,3,4]
#initialize odor list
odor_keys_list = ['9', '6', '7', '8']
#create odor counter
odor_dict = {key: 0 for key in odor_keys_list}
#initialize list for symbols
symbols_set=['t','s','c','z']
#shuffle order of symbols
random.shuffle(symbols_set)
#initialise dict for symbols
symbols={}
for i in range(4):
    symbols[i]=symbols_set[i]
#set study_number
study_number = 0
#set test_number
test_number = 0
#set trial_number
trial_number = 0
#set limiter for each stimulus
limit_study = 1
limit_test = 1
fixation_point_duration = 5.000000


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def eject(smell_correct):
    
    """Eject the stimulus given selected odor. See params in serial.Serial() documentation."""
    
    msg = "w" + odor_keys_list[smell_correct] + ";" + " 1\n" 
    ser.write(msg.encode())
    print("The following command has been sent: \n" +  ">" + msg)
    print("The answer is: ")
    print(ser.readline().decode("ascii"))
    
    
def close_current_capsule(smell_correct):
    
    """Stop the last stimulus. See params in serial.Serial() documentation."""
    
    msg = "w" + odor_keys_list[smell_correct] + ";" + " 0\n" 
    ser.write(msg.encode())
    print("The following command has been sent: \n" +  ">" + msg)
    print("The answer is: ")
    print(ser.readline().decode("ascii"))
    
    
print(Fore.GREEN + "Initialized successfully.")
print("limit_study =", limit_study)
print("limit_test =", limit_test)
print(Fore.YELLOW + "fixation_point_duration =", fixation_point_duration)
#open port
continueRoutine = True
while continueRoutine:
    try:
        ser = serial.Serial(**settings)
        print(Fore.GREEN + "The port has been opened. May the experiment begin!")
        break
            
    except (FileNotFoundError, serial.SerialException): 
        print(Fore.YELLOW + "Arduino connection error. Double check the COM-port!")
        askedInput = str(input(">>>Want to start over? Type Y or N:\n")).lower()
        if askedInput == "y":
            continue
        elif askedInput == "n":
            print("Finishing experiment...")
            core.quit()
        else:
            print(Fore.RED + "Didn't get your input. Try Y or N next time." + "\n" + Fore.MAGENTA + "Trying to open the port now...")

# Initialize components for Routine "Welcome_screen"
Welcome_screenClock = core.Clock()
text_welcome_screen = visual.TextStim(win=win, name='text_welcome_screen',
    text='Прослушайте задание.\n\nДля начала эксперимента нажмите на джойстик.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
# Initialize components for Routine "Start_trial_screen"
Start_trial_screenClock = core.Clock()
background_start_trial_screen = visual.Rect(
    win=win, name='background_start_trial_screen',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text__for_start_trial_screen = visual.TextStim(win=win, name='text__for_start_trial_screen',
    text='Нажмите на джойстик\nдля подачи аромата',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_MARK = visual.ImageStim(
    win=win,
    name='image_MARK', 
    image='gesture-press.png', mask=None,
    ori=0, pos=(0.0, 0.15), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
key_resp_for_start_trial = keyboard.Keyboard()
# Initialize components for Routine "Pause_screen"
Pause_screenClock = core.Clock()
backgound_for_pause_creen = visual.Rect(
    win=win, name='backgound_for_pause_creen',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
cross_for_pause_screen = visual.TextStim(win=win, name='cross_for_pause_screen',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
# Initialize components for Routine "code_study"
code_studyClock = core.Clock()
# Initialize components for Routine "Smell_creen_with_code"
Smell_creen_with_codeClock = core.Clock()
background_for_smell_screen = visual.Rect(
    win=win, name='background_for_smell_screen',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixation_point_during_smell = visual.TextStim(win=win, name='fixation_point_during_smell',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
# Initialize components for Routine "study_trial"
study_trialClock = core.Clock()
polygon_study_background = visual.Rect(
    win=win, name='polygon_study_background',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
image_study = visual.ImageStim(
    win=win,
    name='image_study', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_study_trial = keyboard.Keyboard()
# Initialize components for Routine "codeStudy_Finished"
codeStudy_FinishedClock = core.Clock()
# Initialize components for Routine "blank_500"
blank_500Clock = core.Clock()
polygon_blank_500 = visual.Rect(
    win=win, name='polygon_blank_500',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
# Initialize components for Routine "second_start__screen"
second_start__screenClock = core.Clock()
text_second_start = visual.TextStim(win=win, name='text_second_start',
    text='Прослушайте задание для второй части эксперимента.\n\nНажмите на джойстик.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_second_start = keyboard.Keyboard()
# Initialize components for Routine "Start_trial_screen"
Start_trial_screenClock = core.Clock()
background_start_trial_screen = visual.Rect(
    win=win, name='background_start_trial_screen',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text__for_start_trial_screen = visual.TextStim(win=win, name='text__for_start_trial_screen',
    text='Нажмите на джойстик\nдля подачи аромата',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_MARK = visual.ImageStim(
    win=win,
    name='image_MARK', 
    image='gesture-press.png', mask=None,
    ori=0, pos=(0.0, 0.15), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
key_resp_for_start_trial = keyboard.Keyboard()
# Initialize components for Routine "Pause_screen"
Pause_screenClock = core.Clock()
backgound_for_pause_creen = visual.Rect(
    win=win, name='backgound_for_pause_creen',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
cross_for_pause_screen = visual.TextStim(win=win, name='cross_for_pause_screen',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
# Initialize components for Routine "code_test"
code_testClock = core.Clock()
# Initialize components for Routine "Smell_creen_with_code"
Smell_creen_with_codeClock = core.Clock()
background_for_smell_screen = visual.Rect(
    win=win, name='background_for_smell_screen',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixation_point_during_smell = visual.TextStim(win=win, name='fixation_point_during_smell',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
# Initialize components for Routine "test_trial"
test_trialClock = core.Clock()
background_test_trail = visual.Rect(
    win=win, name='background_test_trail',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
image_test = visual.ImageStim(
    win=win,
    name='image_test', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_test_trial = keyboard.Keyboard()
# Initialize components for Routine "codeTest_Finished"
codeTest_FinishedClock = core.Clock()
# Initialize components for Routine "blank_500"
blank_500Clock = core.Clock()
polygon_blank_500 = visual.Rect(
    win=win, name='polygon_blank_500',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
# Initialize components for Routine "end_screen"
end_screenClock = core.Clock()
text_end_screen = visual.TextStim(win=win, name='text_end_screen',
    text='Спасибо!\n\nЭксперимент завершен.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
# ------Prepare to start Routine "code_initial"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
code_initialComponents = []
for thisComponent in code_initialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
code_initialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# -------Run Routine "code_initial"-------
while continueRoutine:
    # get current time
    t = code_initialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=code_initialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in code_initialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
# -------Ending Routine "code_initial"-------
for thisComponent in code_initialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "code_initial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# ------Prepare to start Routine "Welcome_screen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Welcome_screenComponents = [text_welcome_screen, key_resp]
for thisComponent in Welcome_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# -------Run Routine "Welcome_screen"-------
while continueRoutine:
    # get current time
    t = Welcome_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome_screen* updates
    if text_welcome_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome_screen.frameNStart = frameN  # exact frame index
        text_welcome_screen.tStart = t  # local t and not account for scr refresh
        text_welcome_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome_screen, 'tStartRefresh')  # time at next scr refresh
        text_welcome_screen.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['q', 'space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
# -------Ending Routine "Welcome_screen"-------
for thisComponent in Welcome_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_welcome_screen.started', text_welcome_screen.tStartRefresh)
thisExp.addData('text_welcome_screen.stopped', text_welcome_screen.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# set up handler to look after randomisation of conditions etc
Study_trials = data.TrialHandler(nReps=1000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Study_trials')
thisExp.addLoop(Study_trials)  # add the loop to the experiment
thisStudy_trial = Study_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudy_trial.rgb)
if thisStudy_trial != None:
    for paramName in thisStudy_trial:
        exec('{} = thisStudy_trial[paramName]'.format(paramName))
for thisStudy_trial in Study_trials:
    currentLoop = Study_trials
    # abbreviate parameter names if possible (e.g. rgb = thisStudy_trial.rgb)
    if thisStudy_trial != None:
        for paramName in thisStudy_trial:
            exec('{} = thisStudy_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Start_trial_screen"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_for_start_trial.keys = []
    key_resp_for_start_trial.rt = []
    _key_resp_for_start_trial_allKeys = []
    # keep track of which components have finished
    Start_trial_screenComponents = [background_start_trial_screen, text__for_start_trial_screen, key_resp_for_start_trial, image_MARK]
    for thisComponent in Start_trial_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Start_trial_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Start_trial_screen"-------
    while continueRoutine:
        # get current time
        t = Start_trial_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Start_trial_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background_start_trial_screen* updates
        if background_start_trial_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background_start_trial_screen.frameNStart = frameN  # exact frame index
            background_start_trial_screen.tStart = t  # local t and not account for scr refresh
            background_start_trial_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_start_trial_screen, 'tStartRefresh')  # time at next scr refresh
            background_start_trial_screen.setAutoDraw(True)
        
        # *text__for_start_trial_screen* updates
        if text__for_start_trial_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text__for_start_trial_screen.frameNStart = frameN  # exact frame index
            text__for_start_trial_screen.tStart = t  # local t and not account for scr refresh
            text__for_start_trial_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text__for_start_trial_screen, 'tStartRefresh')  # time at next scr refresh
            text__for_start_trial_screen.setAutoDraw(True)
        
        # *key_resp_for_start_trial* updates
        waitOnFlip = False
        if key_resp_for_start_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_for_start_trial.frameNStart = frameN  # exact frame index
            key_resp_for_start_trial.tStart = t  # local t and not account for scr refresh
            key_resp_for_start_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_for_start_trial, 'tStartRefresh')  # time at next scr refresh
            key_resp_for_start_trial.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_for_start_trial.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_for_start_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_for_start_trial.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_for_start_trial.getKeys(keyList=['q', 'space'], waitRelease=False)
            _key_resp_for_start_trial_allKeys.extend(theseKeys)
            if len(_key_resp_for_start_trial_allKeys):
                key_resp_for_start_trial.keys = _key_resp_for_start_trial_allKeys[-1].name  # just the last key pressed
                key_resp_for_start_trial.rt = _key_resp_for_start_trial_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_MARK* updates
        if image_MARK.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_MARK.frameNStart = frameN  # exact frame index
            image_MARK.tStart = t  # local t and not account for scr refresh
            image_MARK.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_MARK, 'tStartRefresh')  # time at next scr refresh
            image_MARK.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Start_trial_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Start_trial_screen"-------
    for thisComponent in Start_trial_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Study_trials.addData('background_start_trial_screen.started', background_start_trial_screen.tStartRefresh)
    Study_trials.addData('background_start_trial_screen.stopped', background_start_trial_screen.tStopRefresh)
    Study_trials.addData('text__for_start_trial_screen.started', text__for_start_trial_screen.tStartRefresh)
    Study_trials.addData('text__for_start_trial_screen.stopped', text__for_start_trial_screen.tStopRefresh)
    # check responses
    if key_resp_for_start_trial.keys in ['', [], None]:  # No response was made
        key_resp_for_start_trial.keys = None
    Study_trials.addData('key_resp_for_start_trial.keys',key_resp_for_start_trial.keys)
    if key_resp_for_start_trial.keys != None:  # we had a response
        Study_trials.addData('key_resp_for_start_trial.rt', key_resp_for_start_trial.rt)
    Study_trials.addData('key_resp_for_start_trial.started', key_resp_for_start_trial.tStartRefresh)
    Study_trials.addData('key_resp_for_start_trial.stopped', key_resp_for_start_trial.tStopRefresh)
    # the Routine "Start_trial_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pause_screen"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Pause_screenComponents = [backgound_for_pause_creen, cross_for_pause_screen]
    for thisComponent in Pause_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pause_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pause_screen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Pause_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pause_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *backgound_for_pause_creen* updates
        if backgound_for_pause_creen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            backgound_for_pause_creen.frameNStart = frameN  # exact frame index
            backgound_for_pause_creen.tStart = t  # local t and not account for scr refresh
            backgound_for_pause_creen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(backgound_for_pause_creen, 'tStartRefresh')  # time at next scr refresh
            backgound_for_pause_creen.setAutoDraw(True)
        if backgound_for_pause_creen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > backgound_for_pause_creen.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                backgound_for_pause_creen.tStop = t  # not accounting for scr refresh
                backgound_for_pause_creen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(backgound_for_pause_creen, 'tStopRefresh')  # time at next scr refresh
                backgound_for_pause_creen.setAutoDraw(False)
        
        # *cross_for_pause_screen* updates
        if cross_for_pause_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross_for_pause_screen.frameNStart = frameN  # exact frame index
            cross_for_pause_screen.tStart = t  # local t and not account for scr refresh
            cross_for_pause_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_for_pause_screen, 'tStartRefresh')  # time at next scr refresh
            cross_for_pause_screen.setAutoDraw(True)
        if cross_for_pause_screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_for_pause_screen.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                cross_for_pause_screen.tStop = t  # not accounting for scr refresh
                cross_for_pause_screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross_for_pause_screen, 'tStopRefresh')  # time at next scr refresh
                cross_for_pause_screen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pause_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pause_screen"-------
    for thisComponent in Pause_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Study_trials.addData('backgound_for_pause_creen.started', backgound_for_pause_creen.tStartRefresh)
    Study_trials.addData('backgound_for_pause_creen.stopped', backgound_for_pause_creen.tStopRefresh)
    Study_trials.addData('cross_for_pause_screen.started', cross_for_pause_screen.tStartRefresh)
    Study_trials.addData('cross_for_pause_screen.stopped', cross_for_pause_screen.tStopRefresh)
    
    # ------Prepare to start Routine "code_study"-------
    
    
    study_display_order=['t','s','c','z']
    
    #shuffle order to present symbols
    random.seed()
    random.shuffle(study_display_order)
    
    #reset name of file to display
    image_for_study="stimuli/"
    
    #choose the stimulus
    smell_correct=random.randrange(4)
    
    #update number of stimuli presented
    while True:
        print ('random smell try#', smell_correct)
        if odor_dict[odor_keys_list[smell_correct]] < limit_study:
            odor_dict[odor_keys_list[smell_correct]] += 1
            break
        elif sum(odor_dict.values()) == limit_study*4:
            odor_dict = {key: 0 for key in odor_keys_list}
            Study_trials.finished = True    
        else:
            smell_correct = random.randrange(4)
            continue
    print ('random smell#', smell_correct)
    #open port and eject stimulus
    eject(smell_correct)
    
    #set correct symbol
    correct_symbol=symbols[smell_correct]
    
    #create name of file to display
    for i in range(4):
        if correct_symbol == study_display_order[i]:
            #choose red if symbol represents correct smell
            image_for_study+='r'
            correct_key=keys[i]
        else:
            #choose black for other symbols
            image_for_study+='b'
        #add symbol name according to display order
        image_for_study+=str(study_display_order[i])
    
    #add .jpg to the filename
    image_for_study+='.jpeg'
    
    #set next study_number
    study_number+=1
    
    #set next trial_number
    trial_number+=1
    
    #add data to the file
    thisExp.addData('correct_smell', smell_correct)
    thisExp.addData('correct_symbol', correct_symbol)
    thisExp.addData('image_for_study', image_for_study)
    thisExp.addData('correct_key', correct_key)
    thisExp.addData('study_number', study_number)
    thisExp.addData('trial_number', trial_number)
    # keep track of which components have finished
    code_studyComponents = []
    for thisComponent in code_studyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    code_studyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "code_study"-------
    while continueRoutine:
        # get current time
        t = code_studyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=code_studyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in code_studyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "code_study"-------
    for thisComponent in code_studyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "code_study" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Smell_creen_with_code"-------
    continueRoutine = True
    routineTimer.add(fixation_point_duration)
    # update component parameters for each repeat
    # keep track of which components have finished
    Smell_creen_with_codeComponents = [background_for_smell_screen, fixation_point_during_smell]
    for thisComponent in Smell_creen_with_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Smell_creen_with_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Smell_creen_with_code"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Smell_creen_with_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Smell_creen_with_codeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background_for_smell_screen* updates
        if background_for_smell_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background_for_smell_screen.frameNStart = frameN  # exact frame index
            background_for_smell_screen.tStart = t  # local t and not account for scr refresh
            background_for_smell_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_for_smell_screen, 'tStartRefresh')  # time at next scr refresh
            background_for_smell_screen.setAutoDraw(True)
        if background_for_smell_screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_for_smell_screen.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                background_for_smell_screen.tStop = t  # not accounting for scr refresh
                background_for_smell_screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(background_for_smell_screen, 'tStopRefresh')  # time at next scr refresh
                background_for_smell_screen.setAutoDraw(False)
        
        # *fixation_point_during_smell* updates
        if fixation_point_during_smell.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_point_during_smell.frameNStart = frameN  # exact frame index
            fixation_point_during_smell.tStart = t  # local t and not account for scr refresh
            fixation_point_during_smell.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_point_during_smell, 'tStartRefresh')  # time at next scr refresh
            fixation_point_during_smell.setAutoDraw(True)
        if fixation_point_during_smell.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_point_during_smell.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                fixation_point_during_smell.tStop = t  # not accounting for scr refresh
                fixation_point_during_smell.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_point_during_smell, 'tStopRefresh')  # time at next scr refresh
                fixation_point_during_smell.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Smell_creen_with_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Smell_creen_with_code"-------
    for thisComponent in Smell_creen_with_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Study_trials.addData('background_for_smell_screen.started', background_for_smell_screen.tStartRefresh)
    Study_trials.addData('background_for_smell_screen.stopped', background_for_smell_screen.tStopRefresh)
    Study_trials.addData('fixation_point_during_smell.started', fixation_point_during_smell.tStartRefresh)
    Study_trials.addData('fixation_point_during_smell.stopped', fixation_point_during_smell.tStopRefresh)
    
    # ------Prepare to start Routine "study_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_study.setImage(image_for_study)
    key_resp_study_trial.keys = []
    key_resp_study_trial.rt = []
    _key_resp_study_trial_allKeys = []
    # keep track of which components have finished
    study_trialComponents = [polygon_study_background, image_study, key_resp_study_trial]
    for thisComponent in study_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    study_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "study_trial"-------
    while continueRoutine:
        # get current time
        t = study_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=study_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_study_background* updates
        if polygon_study_background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_study_background.frameNStart = frameN  # exact frame index
            polygon_study_background.tStart = t  # local t and not account for scr refresh
            polygon_study_background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_study_background, 'tStartRefresh')  # time at next scr refresh
            polygon_study_background.setAutoDraw(True)
        
        # *image_study* updates
        if image_study.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_study.frameNStart = frameN  # exact frame index
            image_study.tStart = t  # local t and not account for scr refresh
            image_study.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_study, 'tStartRefresh')  # time at next scr refresh
            image_study.setAutoDraw(True)
        
        # *key_resp_study_trial* updates
        if key_resp_study_trial.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_study_trial.frameNStart = frameN  # exact frame index
            key_resp_study_trial.tStart = t  # local t and not account for scr refresh
            key_resp_study_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_study_trial, 'tStartRefresh')  # time at next scr refresh
            key_resp_study_trial.status = STARTED
            # AllowedKeys looks like a variable named `correct_key`
            if not type(correct_key) in [list, tuple, np.ndarray]:
                if not isinstance(correct_key, str):
                    logging.error('AllowedKeys variable `correct_key` is not string- or list-like.')
                    core.quit()
                elif not ',' in correct_key:
                    correct_key = (correct_key,)
                else:
                    correct_key = eval(correct_key)
            # keyboard checking is just starting
            key_resp_study_trial.clock.reset()  # now t=0
            key_resp_study_trial.clearEvents(eventType='keyboard')
        if key_resp_study_trial.status == STARTED:
            theseKeys = key_resp_study_trial.getKeys(keyList=list(correct_key), waitRelease=False)
            _key_resp_study_trial_allKeys.extend(theseKeys)
            if len(_key_resp_study_trial_allKeys):
                key_resp_study_trial.keys = _key_resp_study_trial_allKeys[-1].name  # just the last key pressed
                key_resp_study_trial.rt = _key_resp_study_trial_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in study_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "study_trial"-------
    for thisComponent in study_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Study_trials.addData('polygon_study_background.started', polygon_study_background.tStartRefresh)
    Study_trials.addData('polygon_study_background.stopped', polygon_study_background.tStopRefresh)
    Study_trials.addData('image_study.started', image_study.tStartRefresh)
    Study_trials.addData('image_study.stopped', image_study.tStopRefresh)
    # check responses
    if key_resp_study_trial.keys in ['', [], None]:  # No response was made
        key_resp_study_trial.keys = None
    Study_trials.addData('key_resp_study_trial.keys',key_resp_study_trial.keys)
    if key_resp_study_trial.keys != None:  # we had a response
        Study_trials.addData('key_resp_study_trial.rt', key_resp_study_trial.rt)
    Study_trials.addData('key_resp_study_trial.started', key_resp_study_trial.tStart)
    Study_trials.addData('key_resp_study_trial.stopped', key_resp_study_trial.tStop)
    # the Routine "study_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "codeStudy_Finished"-------
    continueRoutine = True
    # update component parameters for each repeat
    #shut down current working capsule (stops stimulus)
    close_current_capsule(smell_correct)
    
  
    
     #checks the counter to finish Study session
    if sum(odor_dict.values()) == limit_study*4:
            odor_dict = {key: 0 for key in odor_keys_list}
            Study_trials.finished = True
    # keep track of which components have finished
    codeStudy_FinishedComponents = []
    for thisComponent in codeStudy_FinishedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    codeStudy_FinishedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "codeStudy_Finished"-------
    while continueRoutine:
        # get current time
        t = codeStudy_FinishedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=codeStudy_FinishedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in codeStudy_FinishedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "codeStudy_Finished"-------
    for thisComponent in codeStudy_FinishedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "codeStudy_Finished" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank_500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank_500Components = [polygon_blank_500]
    for thisComponent in blank_500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank_500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank_500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank_500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_blank_500* updates
        if polygon_blank_500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_blank_500.frameNStart = frameN  # exact frame index
            polygon_blank_500.tStart = t  # local t and not account for scr refresh
            polygon_blank_500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_blank_500, 'tStartRefresh')  # time at next scr refresh
            polygon_blank_500.setAutoDraw(True)
        if polygon_blank_500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_blank_500.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_blank_500.tStop = t  # not accounting for scr refresh
                polygon_blank_500.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_blank_500, 'tStopRefresh')  # time at next scr refresh
                polygon_blank_500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank_500"-------
    for thisComponent in blank_500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Study_trials.addData('polygon_blank_500.started', polygon_blank_500.tStartRefresh)
    Study_trials.addData('polygon_blank_500.stopped', polygon_blank_500.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1000 repeats of 'Study_trials'
# ------Prepare to start Routine "second_start__screen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_second_start.keys = []
key_resp_second_start.rt = []
_key_resp_second_start_allKeys = []
# keep track of which components have finished
second_start__screenComponents = [text_second_start, key_resp_second_start]
for thisComponent in second_start__screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
second_start__screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# -------Run Routine "second_start__screen"-------
while continueRoutine:
    # get current time
    t = second_start__screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=second_start__screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_second_start* updates
    if text_second_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_second_start.frameNStart = frameN  # exact frame index
        text_second_start.tStart = t  # local t and not account for scr refresh
        text_second_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_second_start, 'tStartRefresh')  # time at next scr refresh
        text_second_start.setAutoDraw(True)
    
    # *key_resp_second_start* updates
    waitOnFlip = False
    if key_resp_second_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_second_start.frameNStart = frameN  # exact frame index
        key_resp_second_start.tStart = t  # local t and not account for scr refresh
        key_resp_second_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_second_start, 'tStartRefresh')  # time at next scr refresh
        key_resp_second_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_second_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_second_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_second_start.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_second_start.getKeys(keyList=['q', 'space'], waitRelease=False)
        _key_resp_second_start_allKeys.extend(theseKeys)
        if len(_key_resp_second_start_allKeys):
            key_resp_second_start.keys = _key_resp_second_start_allKeys[-1].name  # just the last key pressed
            key_resp_second_start.rt = _key_resp_second_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in second_start__screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
# -------Ending Routine "second_start__screen"-------
for thisComponent in second_start__screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_second_start.started', text_second_start.tStartRefresh)
thisExp.addData('text_second_start.stopped', text_second_start.tStopRefresh)
# check responses
if key_resp_second_start.keys in ['', [], None]:  # No response was made
    key_resp_second_start.keys = None
thisExp.addData('key_resp_second_start.keys',key_resp_second_start.keys)
if key_resp_second_start.keys != None:  # we had a response
    thisExp.addData('key_resp_second_start.rt', key_resp_second_start.rt)
thisExp.addData('key_resp_second_start.started', key_resp_second_start.tStartRefresh)
thisExp.addData('key_resp_second_start.stopped', key_resp_second_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "second_start__screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# set up handler to look after randomisation of conditions etc
Test_trials = data.TrialHandler(nReps=1000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Test_trials')
thisExp.addLoop(Test_trials)  # add the loop to the experiment
thisTest_trial = Test_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
if thisTest_trial != None:
    for paramName in thisTest_trial:
        exec('{} = thisTest_trial[paramName]'.format(paramName))
for thisTest_trial in Test_trials:
    currentLoop = Test_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
    if thisTest_trial != None:
        for paramName in thisTest_trial:
            exec('{} = thisTest_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Start_trial_screen"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_for_start_trial.keys = []
    key_resp_for_start_trial.rt = []
    _key_resp_for_start_trial_allKeys = []
    # keep track of which components have finished
    Start_trial_screenComponents = [background_start_trial_screen, text__for_start_trial_screen, key_resp_for_start_trial, image_MARK]
    for thisComponent in Start_trial_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Start_trial_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Start_trial_screen"-------
    while continueRoutine:
        # get current time
        t = Start_trial_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Start_trial_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background_start_trial_screen* updates
        if background_start_trial_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background_start_trial_screen.frameNStart = frameN  # exact frame index
            background_start_trial_screen.tStart = t  # local t and not account for scr refresh
            background_start_trial_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_start_trial_screen, 'tStartRefresh')  # time at next scr refresh
            background_start_trial_screen.setAutoDraw(True)
        
        # *text__for_start_trial_screen* updates
        if text__for_start_trial_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text__for_start_trial_screen.frameNStart = frameN  # exact frame index
            text__for_start_trial_screen.tStart = t  # local t and not account for scr refresh
            text__for_start_trial_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text__for_start_trial_screen, 'tStartRefresh')  # time at next scr refresh
            text__for_start_trial_screen.setAutoDraw(True)
        
        # *key_resp_for_start_trial* updates
        waitOnFlip = False
        if key_resp_for_start_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_for_start_trial.frameNStart = frameN  # exact frame index
            key_resp_for_start_trial.tStart = t  # local t and not account for scr refresh
            key_resp_for_start_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_for_start_trial, 'tStartRefresh')  # time at next scr refresh
            key_resp_for_start_trial.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_for_start_trial.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_for_start_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_for_start_trial.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_for_start_trial.getKeys(keyList=['q', 'space'], waitRelease=False)
            _key_resp_for_start_trial_allKeys.extend(theseKeys)
            if len(_key_resp_for_start_trial_allKeys):
                key_resp_for_start_trial.keys = _key_resp_for_start_trial_allKeys[-1].name  # just the last key pressed
                key_resp_for_start_trial.rt = _key_resp_for_start_trial_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_MARK* updates
        if image_MARK.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_MARK.frameNStart = frameN  # exact frame index
            image_MARK.tStart = t  # local t and not account for scr refresh
            image_MARK.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_MARK, 'tStartRefresh')  # time at next scr refresh
            image_MARK.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Start_trial_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Start_trial_screen"-------
    for thisComponent in Start_trial_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Test_trials.addData('background_start_trial_screen.started', background_start_trial_screen.tStartRefresh)
    Test_trials.addData('background_start_trial_screen.stopped', background_start_trial_screen.tStopRefresh)
    Test_trials.addData('text__for_start_trial_screen.started', text__for_start_trial_screen.tStartRefresh)
    Test_trials.addData('text__for_start_trial_screen.stopped', text__for_start_trial_screen.tStopRefresh)
    # check responses
    if key_resp_for_start_trial.keys in ['', [], None]:  # No response was made
        key_resp_for_start_trial.keys = None
    Test_trials.addData('key_resp_for_start_trial.keys',key_resp_for_start_trial.keys)
    if key_resp_for_start_trial.keys != None:  # we had a response
        Test_trials.addData('key_resp_for_start_trial.rt', key_resp_for_start_trial.rt)
    Test_trials.addData('key_resp_for_start_trial.started', key_resp_for_start_trial.tStartRefresh)
    Test_trials.addData('key_resp_for_start_trial.stopped', key_resp_for_start_trial.tStopRefresh)
    # the Routine "Start_trial_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pause_screen"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Pause_screenComponents = [backgound_for_pause_creen, cross_for_pause_screen]
    for thisComponent in Pause_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pause_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pause_screen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Pause_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pause_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *backgound_for_pause_creen* updates
        if backgound_for_pause_creen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            backgound_for_pause_creen.frameNStart = frameN  # exact frame index
            backgound_for_pause_creen.tStart = t  # local t and not account for scr refresh
            backgound_for_pause_creen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(backgound_for_pause_creen, 'tStartRefresh')  # time at next scr refresh
            backgound_for_pause_creen.setAutoDraw(True)
        if backgound_for_pause_creen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > backgound_for_pause_creen.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                backgound_for_pause_creen.tStop = t  # not accounting for scr refresh
                backgound_for_pause_creen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(backgound_for_pause_creen, 'tStopRefresh')  # time at next scr refresh
                backgound_for_pause_creen.setAutoDraw(False)
        
        # *cross_for_pause_screen* updates
        if cross_for_pause_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross_for_pause_screen.frameNStart = frameN  # exact frame index
            cross_for_pause_screen.tStart = t  # local t and not account for scr refresh
            cross_for_pause_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_for_pause_screen, 'tStartRefresh')  # time at next scr refresh
            cross_for_pause_screen.setAutoDraw(True)
        if cross_for_pause_screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_for_pause_screen.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                cross_for_pause_screen.tStop = t  # not accounting for scr refresh
                cross_for_pause_screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross_for_pause_screen, 'tStopRefresh')  # time at next scr refresh
                cross_for_pause_screen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pause_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pause_screen"-------
    for thisComponent in Pause_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Test_trials.addData('backgound_for_pause_creen.started', backgound_for_pause_creen.tStartRefresh)
    Test_trials.addData('backgound_for_pause_creen.stopped', backgound_for_pause_creen.tStopRefresh)
    Test_trials.addData('cross_for_pause_screen.started', cross_for_pause_screen.tStartRefresh)
    Test_trials.addData('cross_for_pause_screen.stopped', cross_for_pause_screen.tStopRefresh)
    
    # ------Prepare to start Routine "code_test"-------
    test_display_order=['t','s','c','z']
    
    #shuffle order of symbols to display
    random.seed()
    random.shuffle(test_display_order)
    
    #set number for the smell
    smell_correct = random.randrange(4)
    while True:
        print ('random smell try#', smell_correct)
        if odor_dict[odor_keys_list[smell_correct]] < limit_test:
            odor_dict[odor_keys_list[smell_correct]] += 1
            break
        elif sum(odor_dict.values()) == limit_test*4:
            odor_dict = {key: 0 for key in odor_keys_list}
            Study_trials.finished = True    
        else:
            smell_correct = random.randrange(4)
            continue
    print ('random smell#', smell_correct)
    
    #open port and eject stimulus
    eject(smell_correct)
    
    #set correct symbol
    correct_symbol=symbols[smell_correct]
    
    #reset name of file to siplay
    image_for_test="stimuli/"
    
    #Determine a correct key pressed in test session
    for i in range(4):
        if correct_symbol == test_display_order[i]:
            correct_key_test=keys[i]
            break
        else:
            continue
    #create name of file to display
    for i in range(4):
        image_for_test +='b'
        image_for_test +=str(test_display_order[i])
    image_for_test +='.jpeg'
    
    #set next test_number
    test_number+=1
    #set next trial_number
    trial_number+=1
        
    #add data to the file
    thisExp.addData('correct_smell', smell_correct)
    thisExp.addData('correct_symbol', correct_symbol)
    thisExp.addData('image_for_study', image_for_study)
    thisExp.addData('correct_key_test', correct_key_test)
    thisExp.addData('test_number', test_number)
    thisExp.addData('trial_number', trial_number)
    # keep track of which components have finished
    code_testComponents = []
    for thisComponent in code_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    code_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "code_test"-------
    while continueRoutine:
        # get current time
        t = code_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=code_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in code_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "code_test"-------
    for thisComponent in code_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "code_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Smell_creen_with_code"-------
    continueRoutine = True
    routineTimer.add(fixation_point_duration)
    # update component parameters for each repeat
    # keep track of which components have finished
    Smell_creen_with_codeComponents = [background_for_smell_screen, fixation_point_during_smell]
    for thisComponent in Smell_creen_with_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Smell_creen_with_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Smell_creen_with_code"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Smell_creen_with_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Smell_creen_with_codeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background_for_smell_screen* updates
        if background_for_smell_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background_for_smell_screen.frameNStart = frameN  # exact frame index
            background_for_smell_screen.tStart = t  # local t and not account for scr refresh
            background_for_smell_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_for_smell_screen, 'tStartRefresh')  # time at next scr refresh
            background_for_smell_screen.setAutoDraw(True)
        if background_for_smell_screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_for_smell_screen.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                background_for_smell_screen.tStop = t  # not accounting for scr refresh
                background_for_smell_screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(background_for_smell_screen, 'tStopRefresh')  # time at next scr refresh
                background_for_smell_screen.setAutoDraw(False)
        
        # *fixation_point_during_smell* updates
        if fixation_point_during_smell.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_point_during_smell.frameNStart = frameN  # exact frame index
            fixation_point_during_smell.tStart = t  # local t and not account for scr refresh
            fixation_point_during_smell.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_point_during_smell, 'tStartRefresh')  # time at next scr refresh
            fixation_point_during_smell.setAutoDraw(True)
        if fixation_point_during_smell.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_point_during_smell.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                fixation_point_during_smell.tStop = t  # not accounting for scr refresh
                fixation_point_during_smell.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_point_during_smell, 'tStopRefresh')  # time at next scr refresh
                fixation_point_during_smell.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Smell_creen_with_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Smell_creen_with_code"-------
    for thisComponent in Smell_creen_with_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Test_trials.addData('background_for_smell_screen.started', background_for_smell_screen.tStartRefresh)
    Test_trials.addData('background_for_smell_screen.stopped', background_for_smell_screen.tStopRefresh)
    Test_trials.addData('fixation_point_during_smell.started', fixation_point_during_smell.tStartRefresh)
    Test_trials.addData('fixation_point_during_smell.stopped', fixation_point_during_smell.tStopRefresh)
    
    # ------Prepare to start Routine "test_trial"-------

    continueRoutine = True
    # update component parameters for each repeat
    image_test.setImage(image_for_test)
    key_resp_test_trial.keys = []
    key_resp_test_trial.rt = []
    _key_resp_test_trial_allKeys = []
    # keep track of which components have finished
    test_trialComponents = [background_test_trail, image_test, key_resp_test_trial]
    for thisComponent in test_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test_trial"-------
    while continueRoutine:
        # get current time
        t = test_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background_test_trail* updates
        if background_test_trail.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background_test_trail.frameNStart = frameN  # exact frame index
            background_test_trail.tStart = t  # local t and not account for scr refresh
            background_test_trail.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_test_trail, 'tStartRefresh')  # time at next scr refresh
            background_test_trail.setAutoDraw(True)
        
        # *image_test* updates
        if image_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_test.frameNStart = frameN  # exact frame index
            image_test.tStart = t  # local t and not account for scr refresh
            image_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_test, 'tStartRefresh')  # time at next scr refresh
            image_test.setAutoDraw(True)
        
        # *key_resp_test_trial* updates
        waitOnFlip = False
        if key_resp_test_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_test_trial.frameNStart = frameN  # exact frame index
            key_resp_test_trial.tStart = t  # local t and not account for scr refresh
            key_resp_test_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_test_trial, 'tStartRefresh')  # time at next scr refresh
            key_resp_test_trial.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_test_trial.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_test_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_test_trial.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_test_trial.getKeys(keyList=['up', 'down', 'left', 'right'], waitRelease=False)
            _key_resp_test_trial_allKeys.extend(theseKeys)
            if len(_key_resp_test_trial_allKeys):
                key_resp_test_trial.keys = _key_resp_test_trial_allKeys[-1].name  # just the last key pressed
                key_resp_test_trial.rt = _key_resp_test_trial_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test_trial"-------
    for thisComponent in test_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Test_trials.addData('background_test_trail.started', background_test_trail.tStartRefresh)
    Test_trials.addData('background_test_trail.stopped', background_test_trail.tStopRefresh)
    Test_trials.addData('image_test.started', image_test.tStartRefresh)
    Test_trials.addData('image_test.stopped', image_test.tStopRefresh)
    # check responses
    if key_resp_test_trial.keys in ['', [], None]:  # No response was made
        key_resp_test_trial.keys = None
    Test_trials.addData('key_resp_test_trial.keys',key_resp_test_trial.keys)
    if key_resp_test_trial.keys == correct_key_test:
        print(Fore.MAGENTA + f'TEST_TRIAL: Correct key "{key_resp_test_trial.keys}" has been pressed.' + f'\nCorrect symbol: {correct_symbol}')
        pressedCorrect_counter += 1
    else:
        print(Fore.RED + f'TEST_TRIAL: Wrong key "{key_resp_test_trial.keys}" has been pressed.' + f'\nCorrect symbol: {correct_symbol}')
    if key_resp_test_trial.keys != None:  # we had a response
        Test_trials.addData('latency', key_resp_test_trial.rt + fixation_point_duration)
    Test_trials.addData('key_resp_test_trial.started', key_resp_test_trial.tStartRefresh)
    Test_trials.addData('key_resp_test_trial.stopped', key_resp_test_trial.tStopRefresh)
    # the Routine "test_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "codeTest_Finished"-------
    continueRoutine = True
    # update component parameters for each repeat
    #shut down current working capsule (stops stimulus)
    close_current_capsule(smell_correct)
    
       
    #checks the counter to finish Test session
    if sum(odor_dict.values()) == limit_test*4:
            odor_dict = {key: 0 for key in odor_keys_list}
            Test_trials.finished = True
    # keep track of which components have finished
    codeTest_FinishedComponents = []
    for thisComponent in codeTest_FinishedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    codeTest_FinishedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "codeTest_Finished"-------
    while continueRoutine:
        # get current time
        t = codeTest_FinishedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=codeTest_FinishedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in codeTest_FinishedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "codeTest_Finished"-------
    for thisComponent in codeTest_FinishedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "codeTest_Finished" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank_500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank_500Components = [polygon_blank_500]
    for thisComponent in blank_500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank_500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank_500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank_500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_blank_500* updates
        if polygon_blank_500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_blank_500.frameNStart = frameN  # exact frame index
            polygon_blank_500.tStart = t  # local t and not account for scr refresh
            polygon_blank_500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_blank_500, 'tStartRefresh')  # time at next scr refresh
            polygon_blank_500.setAutoDraw(True)
        if polygon_blank_500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_blank_500.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_blank_500.tStop = t  # not accounting for scr refresh
                polygon_blank_500.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_blank_500, 'tStopRefresh')  # time at next scr refresh
                polygon_blank_500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank_500"-------
    for thisComponent in blank_500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Test_trials.addData('polygon_blank_500.started', polygon_blank_500.tStartRefresh)
    Test_trials.addData('polygon_blank_500.stopped', polygon_blank_500.tStopRefresh)
    thisExp.nextEntry()
    
#close the port
ser.close()
print(Back.YELLOW + f"Experiment has been finished with the total score of: {pressedCorrect_counter / (limit_test * 4)}")

if not ser.isOpen():
    print(Fore.GREEN + "Port has been successfully closed")
    
# ------Prepare to start Routine "end_screen"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
end_screenComponents = [text_end_screen, key_resp_2]
for thisComponent in end_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# -------Run Routine "end_screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end_screen* updates
    if text_end_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_end_screen.frameNStart = frameN  # exact frame index
        text_end_screen.tStart = t  # local t and not account for scr refresh
        text_end_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end_screen, 'tStartRefresh')  # time at next scr refresh
        text_end_screen.setAutoDraw(True)
    if text_end_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_end_screen.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text_end_screen.tStop = t  # not accounting for scr refresh
            text_end_screen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_end_screen, 'tStopRefresh')  # time at next scr refresh
            text_end_screen.setAutoDraw(False)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_2.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_2.tStop = t  # not accounting for scr refresh
            key_resp_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
            key_resp_2.status = FINISHED
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
# -------Ending Routine "end_screen"-------
for thisComponent in end_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_end_screen.started', text_end_screen.tStartRefresh)
thisExp.addData('text_end_screen.stopped', text_end_screen.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
