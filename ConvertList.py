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
                        if numlist >= 4:
                            data5 = Data.Data(sel, multipleData[4])
                            list.append(data5)
                            if numlist >= 5:
                                data6 = Data.Data(sel, multipleData[5])
                                list.append(data6)
                                if numlist >= 6:
                                    data7 = Data.Data(sel, multipleData[6])
                                    list.append(data7)
                                    if numlist >= 7:
                                        data8 = Data.Data(sel, multipleData[7])
                                        list.append(data8)
                                        if numlist >= 8:
                                            data9 = Data.Data(sel, multipleData[8])
                                            list.append(data9)
                                            if numlist >= 9:
                                                data10 = Data.Data(sel, multipleData[9])
                                                list.append(data10)

        return list
