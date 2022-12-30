import re


class GetIndices:
    def getGFPindex(self, dataList):
        i = 0
        for line in dataList:
            i = i + 1
            if re.search("LC Chromatogram\\(Detector A-Ch1\\)", line):
                gfp_index = i + 9
                break
        return gfp_index

    def getGFPindexend(self, dataList):
        i = 0
        for line in dataList:
            i = i + 1
            if re.search("LC Chromatogram\\(Detector A-Ch2\\)", line):
                gfp_indexend = i - 3
                break
        return gfp_indexend

    def getTrypindex(self, gfpindexend):
        tryp_index = gfpindexend + 12
        return tryp_index

    def getTrypindexend(self, dataList):
        i = 0
        for line in dataList:
            i = i + 1
            if re.search("Pump A Pressure", line):
                tryp_indexend = i - 3
                break
        return tryp_indexend

    def getNumList(self, multipledata):
        i = 0
        for i in range(len(multipledata)):
            if i == (len(multipledata)):
                numlist = i
                break
            if len(multipledata[i]) == 0:
                numlist = i - 1
                break
        return numlist
