from tkinter import filedialog


class ReadFile:

    def readfile(self):
        typ = [("textfile", "*.txt"), ("csvfile", "*.csv"), ("Excelfile", "*.xlsx")]
        file = filedialog.askopenfilename(filetypes=typ)
        print(file)
        f = open(file, "r")
        dataList = f.readlines()
        f.close()
        return dataList

    def readfiles(self):
        typ = [("textfile", "*.txt"), ("csvfile", "*.csv"), ("Excelfile", "*.xlsx")]
        files = filedialog.askopenfilenames(filetypes=typ)
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
            f = open(files[i], "r")
            data[i] = f.readlines()
            f.close()
        return data
