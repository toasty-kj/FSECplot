import StartEnd


class Data:
    def __init__(self, sel, data_list):
        startEnd = StartEnd.StartEnd()

        self.start = startEnd.getStart(sel, data_list)
        self.end = startEnd.getEnd(sel, data_list)
        self.data_list = data_list

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
