#!/usr/bin/env python
# coding: utf-8

# In[0]:


import os
import glob

import pandas as pd
import argparse

from datetime import datetime


# In[1]:


filedir = os.path.abspath('')

cols_to_extract = ["correct_smell", "correct_symbol", "image_selected", "correct_key", "correct_key_test",
 "key_resp_test_trial.keys", "latency", "latency_wo_fixation", "name", "age", "sex", "session", "date", "expName",
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
        df.insert(df.columns.get_loc("latency") + 1, "latency_wo_fixation",
        df.latency - args.fixation_duration)
        df = df.loc[:, cols_to_extract]
        dfs[name.split(os.sep)[-1]] = df[df.correct_smell.notna()]
    
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
    parser.add_argument("fixation_duration", nargs="?", default=5.000000, type=float, help="Fixation point duration (Default: 5.000000)")
    
    parser.set_defaults(func=process_psychopy_output)
    args = parser.parse_args()
    args.func(args)
    print(">>>Success!<<<\nProceed to {}data_processed".format(os.sep))



