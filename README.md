# PsychoPy_OdorBCI_shared
A general pipeline to build an experimental flow. This repo implies the adding/updating a custom code snippets to work with the corresponding setup within PsychoPy.


### Example usage
To run process_psychopy_csv.py (Requires launch within the same directory as **data** folder is stored!):
* Execute `python process_psychopy_csv.py --help` to get detailed description
* For example, create cleaned and concatenated across individuals dataframes, using statement below. The new file will appear in *myNewFolder*:
    
    ```
    python process_psychopy_csv.py data/Stephanie_smell_experiment_main_2020_Dec_16_2017.csv myNewFolder -c
    ```



...
