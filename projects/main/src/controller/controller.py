from typing import List
from models.FSECplot import FSECplot
from models.create_data_for_chart import CreateDataForChart
from models.ReadFile import read_row_by_path_list
from models.get_default_name import PathAndName, create_path_and_name_list

def create_chart(path_list:list, title:str, is_gfp_or_typ:str):
    """ファイルパスとグラフのタイトル、蛍光の種類からファイルを読み込んで、描画用のクラスに変換する"""
    fsec_data = create_fsec_data(path_list, is_gfp_or_typ)
    
    # matplotlibを用いた作図
    fsec = FSECplot(is_gfp_or_typ,title)
    fsec.plotfsec(fsec_data)
    
def create_fsec_data(path_list:list, is_gfp_or_typ: str):
    """ファイルパスとグラフのタイトル、蛍光の種類からファイルを読み込んで、描画用のクラスに変換する"""
    
    # ファイルの読み込みと配列の配列として読み込んだ行ごとに格納する
    input_data = read_row_by_path_list(path_list)

    # time, intensity, start,endを変数にもつクラスを作る
    createData = CreateDataForChart(input_data,is_gfp_or_typ)
    return createData.convert_list()
    
def get_default_data_name(path_list:List[str], is_gfp_or_typ: str = '1')-> List[PathAndName]:
    fsec_data = create_fsec_data(path_list,is_gfp_or_typ)
    path_name_list = create_path_and_name_list(path_list,fsec_data)
    return path_name_list
