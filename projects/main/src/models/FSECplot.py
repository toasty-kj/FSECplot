from typing import List
import numpy
from matplotlib import pyplot

from models.InputData import InputData


class FSECplot:
    def __init__(self,data_name_list: List[str], is_gfp_or_typ:str, chart_title:str,is_zoom = False ) -> None:
        self.data_name_list =data_name_list
        self.is_gfp_or_typ = is_gfp_or_typ
        self.ylabel = self.get_ylabel_by_fluorescence(is_gfp_or_typ)
        self.y_font_size = 12
        self.xlabel = "Retention time(min)"
        self.x_font_size = 13
        self.title = chart_title
        self.is_zoom = is_zoom

    @staticmethod
    def get_ylabel_by_fluorescence(selected_fulorescence:str):
        if selected_fulorescence == "1":
            return"GFP fluorescence intensity (A.U.)"
        else:
            return "Tryptophan fluorescence intensity (A.U.)"

    def plotfsec(self, lists:InputData  ):
        pyplot.title(self.title,fontdict={"fontname":"MS Gothic"})
        pyplot.xlabel(self.xlabel, {"fontsize": self.x_font_size,"fontname":"Times New Roman"})
        pyplot.ylabel(self.ylabel, {"fontsize": self.y_font_size,"fontname":"Times New Roman"})
        i = 0
        for i in range(len(lists)):
            time = lists[i].get_time(lists[i])
            intensity = lists[i].get_intensity(lists[i])

            legend =  self.data_name_list[i]

            # もし画面からデータが入力されていない場合はデフォルトの値を使用する
            if legend == "":
                legend = lists[i].default
            pyplot.plot(time, intensity, label=legend)

        pyplot.legend(prop={"family":"MS Gothic"})
        pyplot.subplots_adjust(left=0.145, right=0.98)
        pyplot.xlim([0, 10])
        pyplot.grid(which="both", linestyle="--")
        if self.is_zoom == False:
            pyplot.xticks(numpy.arange(0, 10.1, step=1))
        # pyplot.xticks(numpy.arange(0, 10.1, step=1))
        # pyplot.minorticks_on()
        print("Plotting completed!! "
              "click save to save the image")
        print("作図に成功しました。画像を保存する場合はウィンドウ内のセーブボタンをクリックしてください")
        pyplot.show()
