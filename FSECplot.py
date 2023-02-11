from matplotlib import pyplot


class FSECplot:
    def plotfsec(self, lists, sel):
        print("Input the title")
        print("図のタイトルを記入してください")
        title = input("ENTER to skip >>")

        pyplot.title(title)
        if sel == "1":
            label = "GFP fluorescence intensity (A.U.)"
        else:
            label = "Tryptophan fluorescence intensity (A.U.)"
        pyplot.xlabel("Retention time(min)", {"fontsize": 13})
        pyplot.ylabel(label, {"fontsize": 12})
        i = 0
        for i in range(len(lists)):
            time = lists[i].get_time(lists[i])
            intensity = lists[i].get_intensity(lists[i])
            print("図に表示する以下のファイルの名前を教えてください。")
            print("what is the legend of ", lists[i].name)
            legend = input("ENTER to default >> " + lists[i].default)
            if legend == "":
                legend = lists[i].default
            pyplot.plot(time, intensity, label=legend)

        pyplot.legend()
        pyplot.subplots_adjust(left=0.145, right=0.98)
        # pyplot.xticks(numpy.arange(0, 10.1, step=1))
        # pyplot.minorticks_on()
        print("Plotting completed!! "
              "click save to save the image")
        print("作図に成功しました。画像を保存する場合はウィンドウ内のセーブボタンをクリックしてください")
        pyplot.show()
