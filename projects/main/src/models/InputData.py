import re

import models.StartEnd as StartEnd


class InputData:
    def __init__(self, sel, data_list):
        startEnd = StartEnd.StartEnd()

        self.start = startEnd.getStart(sel, data_list)
        self.end = startEnd.getEnd(sel, data_list)
        self.data_list = data_list
        self.name = data_list[3]
        self.default = InputData.extract_name(self, data_list[3])

    def get_time(self, data):
        dataList = data.data_list
        start = data.start
        end = data.end
        l = 0
        time = []
        for l in dataList[start:end]:
            line = l.split()
            if len(line) < 1:
                break
            time.append(float(line[0]))
        return time

    def get_intensity(self, data):
        dataList = data.data_list
        start = data.start
        end = data.end
        l = 0
        intensity = []
        for l in dataList[start:end]:
            line = l.split()
            if len(line) < 1:
                break
            intensity.append(float(line[1]))
        return intensity

    def extract_name(self, string):
        p = r'_(.*?)_'
        r = re.findall(p, string)
        return r[0]
    
    
