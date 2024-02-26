from typing import List
from models.InputData import InputData

class PathAndName:
    def __init__(self,path: str, name: str) -> None:
        self.path = path
        self.name = name
    
    def to_dict(self):
        return {'path':self.path,'name':self.name }
    
def create_path_and_name_list(file_path_list:List[str],fsec_data_list: List[InputData])->List[PathAndName]:
    path_and_name_list:List[PathAndName] = []
    if len(file_path_list) != len(fsec_data_list):
        raise Exception("file_path_listとfsec_data_listの配列の長さが異なります")
    
    for i in range(len(file_path_list)):
        path_and_name_list.append(PathAndName(file_path_list[i],fsec_data_list[i].name))

    return path_and_name_list

def path_and_name_list_2_json(path_and_name_list:List[PathAndName]):
    result = []
    for path_and_name in path_and_name_list:
        result.append(path_and_name.to_dict())
    return result