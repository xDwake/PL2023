import re

class increment:
    
    def __init__(self,year):
        self._year = year
        self._val = 0

    def inc(self):
        return self._val + 1
    

def freq_processos_ano(file):
    dict = {}
    with open(file,'r') as f:
        for line in f:
            line = line.strip('\n')
            if len(line) > 0:
                line_list = line.split("::")
                if len(line_list[1]) > 0: 
                    list_date = line_list[1].split("-")
                    if list_date[0] not in dict.keys():
                        dict[list_date[0]] = 0
                    
                    else:
                        dict[list_date[0]] = dict.get(list_date[0]) + 1 
    
    print(dict)

freq_processos_ano("./TPC3/processos.txt")




