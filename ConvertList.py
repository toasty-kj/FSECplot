import Data


class ConvertList:
    def convert_list(self, sel, multipleData, numlist):
        list = []
        if numlist >= 0:
            data1 = Data.Data(sel, data_list=multipleData[0])
            list.append(data1)
            if numlist >= 1:
                data2 = Data.Data(sel, multipleData[1])
                list.append(data2)
                if numlist >= 2:
                    data3 = Data.Data(sel, multipleData[2])
                    list.append(data3)
                    if numlist >= 3:
                        data4 = Data.Data(sel, multipleData[3])
                        list.append(data4)

        return list
