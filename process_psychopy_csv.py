#!/usr/bin/env python
# coding: utf-8

# In[0]:


import os
import glob

import pandas as pd
import argparse

from datetime import datetime

from math import nan


# In[1]:


filedir = os.path.abspath('')

cols_to_extract = ["correct_smell", "correct_smell_refName", "correct_symbol", "image_selected", "correct_key", "correct_key_test",
 "key_resp_test_trial.keys", "generic_screens_onset", "before_trial_onset", "red_fixcross_onset", "green_fixcross_onset", "polygon_screen_onset", "blank500_onset", "generic_screens_duration", "before_trial_duration", "latency", "latency_wo_fixation", "button_intervals", "name", "age", "sex", "session", "date", "expName",
 "psychopyVersion", "frameRate"]


# In[2]:


def process_psychopy_output(args):
    output_dir = os.path.join(filedir, args.output_dir) # path to a folder to save data to
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir) # create new folder in the same as input data directory
    
    if args.names:
        fnames = args.names
    else:
        input_dir = os.path.join("data", "*.csv")
        fnames = glob.glob(input_dir) # parse all the .csv files in data folder
    
    dfs = {}
    # create dictionary of processed dataframes
    for i, name in enumerate(fnames):
        df = pd.read_csv(fnames[i])

        # create a column for latency
        df.insert(df.columns.get_loc("latency") + 1, "latency_wo_fixation",
        df.latency - args.fixation_duration)

        df.latency_wo_fixation.fillna(df["key_resp_study_trial.rt"], inplace=True)

        # define generic text screens event onset times
        df["generic_screens_onset"] = df[["text_welcome_screen.started", "text_second_start.started", "text_end_screen.started"]].sum(axis=1).replace(0.0, nan)
        
        # define before trial screen event onset times
        df["before_trial_onset"] = df["text__for_start_trial_screen.started"]
        
        # define red fixation cross onset times
        df["red_fixcross_onset"] = df["fixation_point_during_smell.started"]

        # define generic text screens duration, i. e. "Welcome screen" and "Before test trials screen"
        df["generic_screens_duration"] = df[["key_resp.rt", "key_resp_second_start.rt"]].sum(axis=1).replace(0.0, nan)
 
        # define green fixation cross onset times (aka as breathing onset)
        df["green_fixcross_onset"] = df["background_for_smell_screen.started"]

        # define polygon screen onset time
        df["polygon_screen_onset"] = df[["polygon_study_background.started", "image_test.started"]].sum(axis=1).replace(0.0, nan)

        # define the 500 ms blank screen onset time
        df["blank500_onset"] = df["polygon_blank_500.started"]

        # define the duration of before trial screen
        df["before_trial_duration"] = df["key_resp_for_start_trial.rt"]
        
        # collapse a columns into one
        sum_for_buttons = df[["key_resp.rt", "key_resp.started", "key_resp_second_start.rt", "key_resp_second_start.started", "key_resp_for_start_trial.rt", "key_resp_for_start_trial.started"]].sum(axis=1)
        
        # find time intervals between button clicks
        df["button_intervals"] = sum_for_buttons.diff()

        
        df.correct_smell.fillna(5.0, inplace=True) # assign the value to idle button press
        df["correct_smell_refName"] = df["correct_smell"].replace({0.0: "Vanilla", 1.0: "Citrus", 2.0: "Coffee", 3.0: "Water", 5.0: "Idle_Press"})
        df = df.loc[:, cols_to_extract]
        dfs[name.split(os.sep)[-1]] = df.iloc[:-1, :]
    
    # save concatenated dataframes if specified
    if args.concatenate:
        result = pd.concat(dfs)
        result.to_csv(os.path.join(output_dir, "merged" +
                                   datetime.now().strftime("_%Y-%b-%d_%H%M") + ".csv"))
    # else save each dataframe separately
    else:
        for fname, df in dfs.items():
            df.to_csv(os.path.join(output_dir, "processed" + fname))

# In[3]:


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Turns the PsychoPy .csv output into human-readable format. See 'usage' for further details.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--concatenate", action="store_true",
                        help="Export data, concatenated across subjects")
    group.add_argument("-s", "--separate", action="store_true",
                        help="Export separate file for each individual")

    group.add_argument("-n", "--names", nargs="+", help="Allows to enter specific file(s)")
    parser.add_argument("output_dir", nargs="?", default="data_processed", type=str, help="Dir to save output to (Default: data_processed)")
    parser.add_argument("fixation_duration", nargs="?", default=12.000000, type=float, help="Fixation point duration (Default: 12.000000)")
    
    parser.set_defaults(func=process_psychopy_output)
    args = parser.parse_args()
    args.func(args)
    print(">>>Success!<<<\nProceed to {}{}".format(os.sep, args.output_dir))



