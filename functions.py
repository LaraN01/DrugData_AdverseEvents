import pandas as pd
import numpy as np
import ast

# split the entries in column 8 and 9 in single rows, add the rows to the final array and delete the original one; 
# as the array has some pd.isna the rows are ignored
# Column 8 and 9 are read as string and should be parsed in lists
# Use numpy due to the dataframe dimension

def col_splitter(array, col_1, col_2):
    new_rows = []

    for i in range(len(array)):
        col_1_data = array[i, col_1]
        col_2_data = array[i, col_2]

        if pd.isna(col_2_data):
            continue  # Skip rows with NaN in col_2

        col_1_data = ast.literal_eval(col_1_data)
        col_2_data = ast.literal_eval(col_2_data)

        # Checks
        if not isinstance(col_1_data, list) or not isinstance(col_2_data, list):
            continue
        if len(col_1_data) != len(col_2_data):
            continue

        for j in range(len(col_1_data)):
            new_row = np.copy(array[i])
            new_row[col_1] = col_1_data[j]
            new_row[col_2] = col_2_data[j]
            new_rows.append(new_row)

    new_array = np.array(new_rows)

    return new_array

def drop_nan(array, col):
    rows_to_delete = []

    for i in range(len(array)):
        col_data = array[i, col]
        if pd.isna(col_data):
            rows_to_delete.append(i)
       
    new_array = np.delete(array, rows_to_delete, axis=0)

    return new_array

def drop_string(array, col, string):
    rows_to_delete = []

    for i in range(len(array)):
        col_data = array[i, col]
        if col_data==string:
            rows_to_delete.append(i)
       
    new_array = np.delete(array, rows_to_delete, axis=0)

    return new_array

def seriousness_ranker(array, col_1, col_list):
    score_list = []
    score = 0
    for i in range(len(array)):
        col_1_data = array[i, col_1]
        if col_1_data == 1.0:
            score += 5
        else:
            for col in col_list:
                col_data = array[i, col]
                if col_data == 1.0:
                    score += 1
        score_list.append(score)
        score = 0 
    
    new_array = np.column_stack([array, score_list])
    
    return new_array

def risk_ranker(array, col_1, col_2, col_3):
    score_list=[]
    for i in range(len(array)):
        score=0
        col_1_data=array[i,col_1]
        if col_1_data==1.0:
            score+=5
        elif col_1_data==2.0:
            score+=2
        
        col_2_data = float(array[i, col_2])
        if col_2_data==1:
            score+=3
        elif col_2_data==2:
            score+=3
        elif col_2_data==3:
            score+=1
        elif col_2_data==4:
            score+=4
        elif col_2_data==5:
            score+=5
        elif col_2_data==6:
            score+=3
        
        col_3_data=array[i,col_3]
        score+=col_3_data
        score_list.append(score)

    new_array=np.column_stack([array,score_list])
    
    return new_array

# col is the column of interest, chars_to_strip is the tharacters to strip from each element

def strip_column_elements(array, col):

    for i in range(len(array)):
        print(i)
        array[i,col] = ast.literal_eval(array[i,col])
    
    return None