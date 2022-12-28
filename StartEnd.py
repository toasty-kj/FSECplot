class StartEnd:
    def getSel(self):
        while True:
            print("GFPなら1をTryptophanなら2を入力してください")
            flu = input(">>")
            if flu == "1":
                break
            if flu == "2":
                break
            else:
                print("半角の1もしくは2を入力してください。")
        return flu

    def getStart(self, flu, gfpStart, trypStart):
        if flu == "1":
            start = gfpStart
        if flu == "2":
            start = trypStart
        return start

    def getEnd(self, flu, gfpEnd, trypEnd):
        if flu == "1":
            end = gfpEnd
        if flu == "2":
            end = trypEnd
        return end
