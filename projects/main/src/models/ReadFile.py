import logging
import os
import tkinter
from tkinter import filedialog


def read_row_by_path_list(file_path_list:list):
    file_path_list
    data_by_row_list = []
    for file in file_path_list:
        if not os.path.exists(file):
            logging.warn(f'file not found in {file}')
        f = open(file, "r")
        data_by_row_list.append(f.readlines())
        f.close()
    return data_by_row_list

def input_file():
    """tkinterでファイルを選択する(electron移行後は使用しない)"""
    # ルートウィンドウの非表示
    root = tkinter.Tk()
    root.withdraw()
    typ = [("textfile", "*.txt"), ("csvfile", "*.csv"), ("Excelfile", "*.xlsx")]
    files = filedialog.askopenfilenames(filetypes=typ)
    return  files
        
