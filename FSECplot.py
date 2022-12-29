from matplotlib import pyplot


class FSECplot:
    def plotfsec(self, list):
        print("Input the title")
        print("図のタイトルを記入してください")
        title = input(">>")

        pyplot.title(title)
        pyplot.xlabel("Ret.time(min)")
        pyplot.ylabel("GFP fluorescence intensity (A.U.)")
        i = 0
        for i in range(len(list)):
            time = list[i].get_time(list[i])
            intensity = list[i].get_intensity(list[i])
            pyplot.plot(time, intensity)

        pyplot.show()
