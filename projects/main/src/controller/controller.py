from models.FSECplot import FSECplot
from models.create_data_for_chart import CreateDataForChart
from models.ReadFile import read_row_by_path_list


def create_chart(path_list:list, title:str, is_gfp_or_typ:str):
    # ファイルの読み込みとListへの格納

    # time, intensity, start,endを変数にもつクラスを作る
    # selとmultipleDataを引数にとって
    input_data = read_row_by_path_list(path_list)
    createData = CreateDataForChart(input_data,is_gfp_or_typ)
    lists = createData.convert_list()
    sel = createData.is_GFP_or_Trp

    # matplotlibを用いた作図
    fsec = FSECplot()
    fsec.plotfsec(lists, sel, False,title)
    
