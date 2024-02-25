from models.Data import Data

class CreateDataForChart:
    """データを変換して描画する"""
    def __init__(self,data_path_list:[],is_gfp_or_typ:str) -> None:
        # validate_file_path_list(data_path_list)
        self.data_path_list = data_path_list

        self.is_GFP_or_Trp = is_gfp_or_typ

    def convert_list(self):
        """データごとにクラスに変換して、配列に入れる"""
        lists = []
        for data in self.data_path_list:
            lists.append(Data(sel=self.is_GFP_or_Trp, data_list=data))
        return lists
    
    