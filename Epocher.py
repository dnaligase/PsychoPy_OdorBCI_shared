#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:52:38 2021

@author: gric-gosha
"""
import numpy as np
import mne
import glob
import os
import re

from tqdm import tqdm
from itertools import groupby
from datetime import datetime


        
os.chdir("/Volumes/EXTSTORAGE/physionet.org/files/hmc-sleep-staging/1.0.1/recordings")

correspondence = {"Sleep stage W": 1, "Sleep stage N1": 2, "Sleep stage N2": 2,
                  "Sleep stage N3": 2, "Sleep stage N4": 2,
                  "Sleep stage R": 3, "Lights on": 4, "Lights off": 5}

# correspondence = {"W": 1, "S1": 2, "S2": 3,
#                   "S3": 4, "S4": 5,
#                   "R": 6, "MT": 7}

def timestr_to_seconds(timestrings:list):
    """NOTE: May fail to work when more than one 24hr shifts occur."""
    obj = map(lambda x: datetime.strptime(x, '%H:%M:%S'), timestrings)
    
    seconds_arr = np.zeros(len(timestrings))
    for i, instance in enumerate(list(obj)):
        seconds_arr[i] = instance.second + \
                            instance.minute * 60 + \
                                instance.hour * 3600
                                
    seconds = np.where(seconds_arr < seconds_arr[0], seconds_arr + 86400, seconds_arr)
    seconds -= seconds.min()                            
    return seconds


def truncate_to_divisible(X, divisor):
    """
    Checks if array is divisible without remainder.
    If yes, returns the array of originial shape.
    If no, returns the truncated divisable array.
    """
    integer = int(X.shape[0] // divisor)
    remainder = int(X.shape[0] % divisor)
    
    if remainder != 0:
        X = X[:-remainder]
    else:
        pass
    
    return X, integer


def epoch_slicer(data, annotations, epoch_length=30.0, fs=256.0, 
                 onsets_float=False, separator="\t", header_idx=21):
    """
    Prepare epochs according to data and annotations.
    
    Parameters
    ----------
    data : tuple of ndarrays
        A tuple containing signal and time arrays.
    annotations : list
        A list of time events with first row as a column names
    epoch_length : float
        Desired epoch length in secods.
    fs : float
        Sampling frequency.

    Returns
    -------
    epochs : list
        List of epoch arrays. Each epoch is of shape (epoch_length * fs,).
    labels : list
        List of integer labels corresponding to each extracted epoch.
    """
    # le = LabelEncoder()
    
    # Search for keywords to extract proper columns from .txt
    # >>>Is there any more elegant way?<<<
    for i, col in enumerate(annotations[header_idx].split(separator)):
        if re.search(r"[Oo][Nn][Ss]", col):
            onset_col = i
    
    for i, col in enumerate(annotations[header_idx].split(separator)):
        if re.search(r"[Aa][Nn][Nn][Oo]", col):
            annot_col = i
            
    for i, col in enumerate(annotations[header_idx].split(separator)):
        if re.search(r"[Dd][Uu][Rr]", col):
            duration_col = i
        
    durations = [float(annotations[i].split(separator)[duration_col]) for i in range(header_idx+1, len(annotations))]
    targets_categ = [annotations[i].split(separator)[annot_col] for i in range(header_idx+1, len(annotations))]
    if onsets_float:
        onsets = [float(annotations[i].split(separator)[onset_col]) for i in range(header_idx+1, len(annotations))]
    else:
        try:
            onsets = [annotations[i].split(separator)[onset_col] for i in range(header_idx+1, len(annotations))]
            onsets = timestr_to_seconds(onsets)
        except ValueError:
            raise AssertionError("Wrong datetime format!")
    
    signal, times = data
    
    false_idxs = []
    for i, duration in enumerate(durations):
        try:
            assert duration == 30. 
        except AssertionError:
            false_idxs.append(i)
            continue
        
        
    # targets = le.fit_transform(targets_categ) 
    targets = [correspondence[target] for target in targets_categ]
    targets = np.delete(targets, false_idxs, 0)
    onsets = np.delete(onsets, false_idxs, 0)
    
    # find the indexes where transition between classes occurs
    phase_shifts_idxs = np.where(targets[:-1] != targets[1:])[0] + 1
    # place a zero index in the beginning of an array
    phase_shifts_idxs = np.insert(phase_shifts_idxs, 
                                  [0, phase_shifts_idxs.shape[0]], [0, -1])
    
    epochs = []
    labels = []
    
    targets = [k for k, g in groupby(targets)]
    targets += [0]
    
    for i in range(1, len(phase_shifts_idxs)): 
        idx_onset = np.argwhere(times == onsets[phase_shifts_idxs[i - 1]])[0, 0]
        idx_end = np.argwhere(times == onsets[phase_shifts_idxs[i]])[0, 0]
        label = targets[i - 1]
        
        signal_trunc, denominator = truncate_to_divisible(np.squeeze(signal)[idx_onset:idx_end],
                                                          epoch_length * fs)
        try:
            arrays = np.split(signal_trunc, denominator)
        except ZeroDivisionError:
            continue
        
        epochs += arrays
        labels += [label] * len(arrays)
        
    return epochs, labels, targets, phase_shifts_idxs
    
        
# Here prepare the epochs        
fnames = [os.path.basename(fname) for fname in glob.glob(os.path.join(os.getcwd(), "SN???.edf"))]
annotnames = [os.path.basename(fname) for fname in glob.glob(os.path.join(os.getcwd(), "*.txt"))]
fnames.sort(), annotnames.sort()

epochs_list = []
labels_list = []
subjects_list = []

print(f"Preparing {len(fnames)} files.")
for fname, annotname in tqdm(zip(fnames, annotnames), total=len(fnames)):
    raw = mne.io.read_raw_edf(fname, verbose=False)
    raw.resample(80.)
    
    with open(annotname, "r") as f:
        annotations = f.readlines()
        f.close()
        
    if 'EEG F4-M1' in raw.ch_names:
        epochs, labels, targets, psi = epoch_slicer(raw['EEG F4-M1'], annotations, 10., 80.,
                                                    True, ", ", 0)
        epochs_list.append(epochs), \
            labels_list.append(labels), \
                subjects_list.append(re.findall(r'\d+', annotname))
    else:
        continue
        
epochs_arr = np.asarray(epochs_list, object)
labels_arr = np.asarray(labels_list, object)

np.save("labels_new.npy", labels_arr, allow_pickle=True)
np.save("epochs_new.npy", epochs_arr, allow_pickle=True)