import Data


class ConvertList:
    def convert_list(self, sel, multipleData, numlist):
        lists = []
        i = 0
        for i in range(numlist + 1):
            lists.append(Data.Data(sel, multipleData[i]))
        return lists
