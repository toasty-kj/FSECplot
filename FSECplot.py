from matplotlib import pyplot


class FSECplot:
    def plotfsec(self, list, sel):
        print("Input the title")
        print("図のタイトルを記入してください")
        title = input("ENTER to skip >>")

        pyplot.title(title)
        if sel == "1":
            label = "GFP fluorescence intensity (A.U.)"
        else:
            label = "Tryptophan fluorescence intensity (A.U.)"
        pyplot.xlabel("Ret.time(min)", {"fontsize": 15})
        pyplot.ylabel(label, {"fontsize": 12})
        i = 0
        for i in range(len(list)):
            time = list[i].get_time(list[i])
            intensity = list[i].get_intensity(list[i])
            print("図に表示する以下のファイルの名前を教えてください。")
            print("what is the legend of ", list[i].name)
            legend = input("ENTER to skip >>")
            pyplot.plot(time, intensity, label=legend)

        pyplot.legend()
        pyplot.subplots_adjust(left=0.145, right=0.98)
        print("Plotting successful!! "
              "click save to save the image")
        print("作図に成功しました。画像を保存する場合はウィンドウ内のセーブボタンをクリックしてください")
        pyplot.show()
