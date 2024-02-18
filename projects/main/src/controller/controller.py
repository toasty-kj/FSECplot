from models.FSECplot import FSECplot
from models.create_data_for_chart import CreateDataForChart
from models.ReadFile import ReadFile


def create_chart(path_list:list):
    # ファイルの読み込みとListへの格納

    # 目的の列のインデックスを得る

    # time, intensity, start,endを変数にもつクラスを作る
    # selとmultipleDataを引数にとって
    rf = ReadFile()
    input_data = rf.create_input_file_data(path_list)
    createData = CreateDataForChart(input_data)
    lists = createData.convert_list()
    sel = createData.is_GFP_or_Trp

    # print(time[-1])
    # matplotlibを用いた作図
    fsec = FSECplot()
    fsec.plotfsec(lists, sel, False)
    
