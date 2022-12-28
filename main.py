from tkinter import filedialog

'''
コマンドラインベースで動かす
・まず読み込むファイルをGUIで選んでもらう
・次にFSECとTryptophanを選択してもらう
・plotして図をアウトプットする(file名を記入してもらう)
'''


def inputFile():
    typ = [("textfile", "*.txt"), ("csvfile", "*.csv"), ("Excelfile", "*.xlsx")]
    fle = filedialog.askopenfilenames(filetypes=typ)
    print(fle)


def main():
    print("This is plotting program for FSEC")
    inputFile()
