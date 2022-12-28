import re
from tkinter import filedialog

from matplotlib import pyplot

'''
まず複数のファイルを重ね合わせるかどうか聞く
仮に１つのファイルのみの場合はaskopenfilename, ２つの時はfileがタプルなので注意する
今のところ読み込むファイルはFSECファイルのtxt形式のみ
一行ずつリストとしてdataListに格納して正規表現で目的の場所の最初と最後のインデックスをとる
その範囲においてdataListを読み込み空白で区切って一番目をtime, ２番目をintensityとしてリストに格納する
matplotlibによって作図する
'''
print("This is plotting program for FSEC")

typ = [("textfile", "*.txt"), ("csvfile", "*.csv"), ("Excelfile", "*.xlsx")]
files = filedialog.askopenfilename(filetypes=typ)
print(files)
# 複数のファイルの時はタプルなのでfor文とかでまわしてインデックスのついてリストを得る？
# 作図の時も同様

f = open(files, "r")

dataList = f.readlines()
# indexをしらべる
i = 0
for line in dataList:
    i = i + 1
    if re.search("LC Chromatogram\\(Detector A-Ch1\\)", line):
        gfp_index = i + 9
        break

i = 0
for line in dataList:
    i = i + 1
    if re.search("LC Chromatogram\\(Detector A-Ch2\\)", line):
        tryp_index = i + 9
        gfp_indexend = i - 3
        break
i = 0
for line in dataList:
    i = i + 1
    if re.search("Pump A Pressure", line):
        tryp_indexend = i - 3
        break

i = 0
time = []
intensity = []
while True:
    print("GFPなら1をTryptophanなら2を入力してください")
    flu = input(">>")
    if flu == "1":
        start = gfp_index
        end = gfp_indexend
        break
    if flu == "2":
        start = tryp_index
        end = tryp_indexend
        break
for l in dataList[start:end]:
    line = l.split()
    if len(line) < 1:
        break
    time.append(float(line[0]))
    intensity.append(float(line[1]))

print(time[-1])
print("Input the title")
print("図のタイトルを記入してください")
title = input(">>")

pyplot.title(title)
pyplot.xlabel("Ret.time(min)")
pyplot.ylabel("GFP fluorescence intensity (A.U.)")
pyplot.plot(time, intensity)

pyplot.show()
f.close()
