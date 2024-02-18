import logging
import os
import tkinter
from tkinter import filedialog


class ReadFile:
    def create_input_file_data(self,input_file_path:[]):
        files = input_file_path
        length = len(files)
        data1 = []
        data2 = []
        data3 = []
        data4 = []
        data5 = []
        data6 = []
        data7 = []
        data8 = []
        data9 = []
        data10 = []
        data = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]
        i = 0
        for i in range(length):
            print(files[i])
            if not os.path.exists(files[i]):
                logging.warn(f'file not found in {files[i]}')
            f = open(files[i], "r")
            data[i] = f.readlines()
            f.close()
        return data

    def input_file(self):
        # ルートウィンドウの非表示
        root = tkinter.Tk()
        root.withdraw()
        typ = [("textfile", "*.txt"), ("csvfile", "*.csv"), ("Excelfile", "*.xlsx")]
        files = filedialog.askopenfilenames(filetypes=typ)
        self.input_file_path = files
        
