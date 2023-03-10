import GetIndices


class StartEnd:
    def __init__(self):
        self.flu = None

    def getSel(self):
        while True:
            print("Input 1 for GFP, 2 for Tryptophan")
            print("GFPなら1をTryptophanなら2を入力してください")
            flu = input(">>")
            if flu == "1":
                break
            if flu == "2":
                break
            else:
                print("半角の1もしくは2を入力してください。")
        return flu

    def getStart(self, flu, dataList):
        getIndex = GetIndices.GetIndices()
        gfpStart = getIndex.getGFPindex(dataList)
        gfpEnd = getIndex.getGFPindexend(dataList)
        trypStart = getIndex.getTrypindex(gfpEnd)
        if flu == "1":
            start = gfpStart
        if flu == "2":
            start = trypStart
        return start

    def getEnd(self, flu, dataList):
        getIndex = GetIndices.GetIndices()
        gfpEnd = getIndex.getGFPindexend(dataList)
        trypEnd = getIndex.getTrypindexend(dataList)
        if flu == "1":
            end = gfpEnd
        if flu == "2":
            end = trypEnd
        return end
