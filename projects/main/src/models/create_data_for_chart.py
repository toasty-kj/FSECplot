from models.Data import Data

class CreateDataForChart:
    def __init__(self,data_path_list:[],is_gfp_or_typ:str) -> None:
        # validate_file_path_list(data_path_list)
        self.data_path_list = data_path_list

        # TODO 絶対にいい方法があるので後からリファクタリングする
        self.data_list_length =self.getNumList()

        # TODO 画面側から選択してもらうようにする
        self.is_GFP_or_Trp = is_gfp_or_typ


    def getNumList(self):
        i = 0
        for i in range(len(self.data_path_list)):
            if i == (len(self.data_path_list)):
                numlist = i
                break
            if len(self.data_path_list[i]) == 0:
                numlist = i - 1
                break
            else:
                numlist = i - 1
        return numlist

    def convert_list(self):
        lists = []
        i = 0
        for i in range(self.data_list_length + 1):
            lists.append(Data(sel=self.is_GFP_or_Trp, data_list=self.data_path_list[i]))
        return lists
    
    