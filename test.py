from matplotlib import pyplot

import GetIndices
import ReadFile
import StartEnd

'''
まず複数のファイルを重ね合わせるかどうか聞く
仮に１つのファイルのみの場合はaskopenfilename, ２つの時はfileがタプルなので注意する
今のところ読み込むファイルはFSECファイルのtxt形式のみ
一行ずつリストとしてdataListに格納して正規表現で目的の場所の最初と最後のインデックスをとる
その範囲においてdataListを読み込み空白で区切って一番目をtime, ２番目をintensityとしてリストに格納する
matplotlibによって作図する
'''
print("This is plotting program for FSEC")

# ファイルの読み込みとListへの格納
readFile = ReadFile.ReadFile
dataList = readFile.readFile()
# 目的の列のインデックスを得る
getIndex = GetIndices.GetIndices

# indexをしらべる
gfpStart = getIndex.getGFPindex(dataList)
gfpEnd = getIndex.getGFPindexend(dataList)
trypStart = getIndex.getTrypindex(gfpEnd)
trypEnd = getIndex.getTrypindex(dataList)

startEnd = StartEnd.StartEnd
sel = startEnd.getSel()
start = startEnd.getStart(sel, gfpStart, trypStart)
end = startEnd.getEnd(sel, gfpEnd, trypEnd)

i = 0
time = []
intensity = []

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
