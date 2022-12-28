class ReadFile:
    def readFile(self):
        typ = [("textfile", "*.txt"), ("csvfile", "*.csv"), ("Excelfile", "*.xlsx")]
        files = filedialog.askopenfilename(filetypes=typ)
        print(files)
        # 複数のファイルの時はタプルなのでfor文とかでまわしてインデックスのついてリストを得る？
        # 作図の時も同様

        f = open(files, "r")

        dataList = f.readlines()
        f.close()
        return dataList
