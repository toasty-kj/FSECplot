from typing import List
from models.InputData import InputData

class CreateDataForChart:
    """データを変換して描画する"""
    def __init__(self,data_rows_list:list, is_gfp_or_typ:str) -> None:
        # validate_file_path_list(data_rows_list)
        self.data_rows_list = data_rows_list

        self.is_GFP_or_Trp = is_gfp_or_typ

    def convert_list(self)->List[InputData]:
        """データごとにクラスに変換して、配列に入れる"""
        lists = []
        for data in self.data_rows_list:
            lists.append(InputData(sel=self.is_GFP_or_Trp, data_list=data))
        return lists
    
    