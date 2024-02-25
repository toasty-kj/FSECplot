import InputData


class ConvertList:
    def convert_list(self, sel, multipleData, numlist):
        lists = []
        i = 0
        for i in range(numlist + 1):
            lists.append(InputData.InputData(sel, multipleData[i]))
        return lists


'''
exe化する場合

'''
