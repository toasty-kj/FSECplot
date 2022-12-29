from matplotlib import pyplot


class FSECplot:
    def plotfsec(self, time, intensity):
        print("Input the title")
        print("図のタイトルを記入してください")
        title = input(">>")

        pyplot.title(title)
        pyplot.xlabel("Ret.time(min)")
        pyplot.ylabel("GFP fluorescence intensity (A.U.)")
        pyplot.plot(time, intensity)

        pyplot.show()
