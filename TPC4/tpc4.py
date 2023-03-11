import re
import json

def converter_csv_json(src: str, dest:str):
        
    regex1 = r'^(?P<num>\d+),(?P<nome>[^,]+),(?P<curso>[^,]+),(?P<notas>(?:\d+,)*\d+),*$'
    regex2 = r'^(?P<num>\d+),(?P<nome>[^,]+),(?P<curso>[^,]+)$'
    param_list = []
    header = []
    with open(src,"r",encoding='utf8') as f:
        for line in f.readlines():
            header = re.findall(r"(\w+(?:\{\d+(?:,\d+)?\}(?:::\w+)?)?)",line,re.UNICODE)
            match = re.match(regex1, line)
            if match:
                param_list.append(match.groupdict())
            elif match:= re.match(regex2, line):
                param_list.append(match.groupdict())
                
        print(param_list)
        print(header)
    
    for dict in param_list:
        if "notas" in dict:
            lst = dict["notas"].split(',')
            dict["notas"] = []
            dict["notas"] = lst

    if re.search("media",header[3]):
        for dict in param_list:
            res = [int(i) for i in lst] # convert elements from string to int
            dict["notas"] = sum(res)/len(res)

    elif re.search("sum",header[3]):
        for dict in param_list:
            res = [int(i) for i in lst] # convert elements from string to int
            dict["notas"] = sum(res)

    
    with open(dest,"w",encoding='utf8') as file:
        json.dump(param_list, file,indent = 4,separators=(',', ':'),ensure_ascii=False)


converter_csv_json("csv/alunos1.csv","json/alunos1.json")
converter_csv_json("csv/alunos2.csv","json/alunos2.json")
converter_csv_json("csv/alunos3.csv","json/alunos3.json")
converter_csv_json("csv/alunos4.csv","json/alunos4.json")
converter_csv_json("csv/alunos5.csv","json/alunos5.json")

