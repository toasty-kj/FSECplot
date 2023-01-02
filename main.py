import ConvertList
import FSECplot
import GetIndices
import ReadFile
import StartEnd

'''
まず複数のファイルを重ね合わせるかどうか聞く
今のところ読み込むファイルはFSECファイルのtxt形式のみ
一行ずつリストとしてdataListに格納して正規表現で目的の場所の最初と最後のインデックスをとる
その範囲においてdataListを読み込み空白で区切って一番目をtime, ２番目をintensityとしてリストに格納する
matplotlibによって作図する
'''
print("source code : https://github.com/toasty-kj/FSECplot")
print("written by Koji Takaki 2022/12/27")
print("This is plotting program for SHIMAZU Labsolution FSEC")
# ファイルの読み込みとListへの格納
rf = ReadFile.ReadFile()
# dataList = rf.readfile()
multipleData = rf.readfiles()

# 目的の列のインデックスを得る
getIndex = GetIndices.GetIndices()
numlist = getIndex.getNumList(multipleData)

# time, intensity, start,endを変数にもつクラスを作る
# selとmultipleDataを引数にとって
startEnd = StartEnd.StartEnd()
sel = startEnd.getSel()
convert = ConvertList.ConvertList()
lists = convert.convert_list(sel, multipleData, numlist)

# print(time[-1])
# matplotlibを用いた作図
fsec = FSECplot.FSECplot()
fsec.plotfsec(lists, sel)
