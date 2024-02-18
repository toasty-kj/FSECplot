import models.GetIndices as GetIndices


class StartEnd:
    def __init__(self):
        self.flu = None

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
