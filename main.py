import ConvertList
import FSECplot
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
# 同時に読み込めるファイルの数を10とかに設定しといて
# 帰ってきたタプルの数でループを回す数をきめてリストに読み込むファイルの名前を入れておく
# ファイルの読み込みとListへの格納
rf = ReadFile.ReadFile()
# dataList = rf.readfile()
multipleData = rf.readfiles()

# 目的の列のインデックスを得る
getIndex = GetIndices.GetIndices()
numlist = getIndex.getNumList(multipleData)
# gfpStart = getIndex.getGFPindex(dataList)
# gfpEnd = getIndex.getGFPindexend(dataList)
# trypStart = getIndex.getTrypindex(gfpEnd)
# trypEnd = getIndex.getTrypindexend(dataList)

# time, intensity, start,endを変数にもつクラスを作る
# selとmultipleDataを引数にとって
startEnd = StartEnd.StartEnd()
sel = startEnd.getSel()
# sel と目的のデータリストさえあればよい
convert = ConvertList.ConvertList()
list = convert.convert_list(sel, multipleData, numlist)

# とりあえず10個くらいのdataクラスをリストに入れてnumlistの文だけまわす

# print(time[-1])
# matplotlibを用いた作図
fsec = FSECplot.FSECplot()
fsec.plotfsec(list)
