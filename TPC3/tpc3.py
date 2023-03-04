import re  
import json

def file_parse(file):
    
    reg_exp = r"(?P<dir>\d+)::(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<nome_pai>[a-zA-Z ]+)::(?P<nome_mae>[a-zA-Z ]+)::(?P<obs>.*)::"
    regex = re.compile(reg_exp)
    parsed_list = []
    with open(file,'r') as f:
        for line in f:
            if match := regex.finditer(line):
               parsed_list = parsed_list + [m.groupdict() for m in match]

    return parsed_list

def separa_nomes(nome):

    return re.match(r"\w+\b",nome).group(), re.search(r"\b\w+$",nome).group()

def freq_processos_ano(parsed_list):

    dict_por_ano = {}

    for dict in parsed_list:
        if dict["ano"] not in dict_por_ano:
            dict_por_ano[dict["ano"]] = 0

        dict_por_ano[dict["ano"]] += 1

    print("\n\n\n\n")
    print(dict_por_ano)

def seculo_para_intervalo(seculo):
    primeiro_ano = (seculo - 1) * 100 + 1
    ultimo_ano = primeiro_ano + 99

    return (primeiro_ano, ultimo_ano)

def freq_top5_nomes(parsed_list,seculo,nome_id):

    dict_top5_nomes = {}
    for dict in parsed_list:
        if (int(dict["ano"]) - 1) // 100 + 1 == seculo:
            nome = separa_nomes(dict["nome"])
            if nome[nome_id] not in dict_top5_nomes:
                dict_top5_nomes[nome[nome_id]] = 0

            dict_top5_nomes[nome[nome_id]] += 1

            pai = separa_nomes(dict["nome_pai"])

            if pai[nome_id] not in dict_top5_nomes:
                dict_top5_nomes[pai[nome_id]] = 0
            
            dict_top5_nomes[pai[nome_id]] += 1 

            mae = separa_nomes(dict["nome_mae"])

            if mae[nome_id] not in dict_top5_nomes:
                dict_top5_nomes[mae[nome_id]] = 0
            
            dict_top5_nomes[mae[nome_id]] += 1
    
    return sorted(dict_top5_nomes.items(), key=lambda x:x[1], reverse=True)[:5]

def top5_nomes_seculo(parsed_file):
    first_name = {}
    last_name = {}

    for i in range(0,22):
        first_name[seculo_para_intervalo(i)] = freq_top5_nomes(parsed_file,i,0)
        last_name[seculo_para_intervalo(i)] = freq_top5_nomes(parsed_file,i,1)

    print("\n\n\n\n")
    print(first_name)
    print("\n\n")
    print(last_name)

def freq_parentesco(parsed_file):
    
    reg_exp1 = r",[\w\s]+.[\s*](?i:Proc)|,[\w\s]+.[:]+"
    regex1 = re.compile(reg_exp1)
    reg_exp2= r".[\s*](?i:Proc.)"
    regex2 = re.compile(reg_exp2)
    dict_parentesco = {}

    for dict in parsed_file:
        if match := regex1.findall(dict["obs"]):
            for elem in match:
                pos = elem.find(".")
                elem = elem[1:-(len(elem)-pos)]

                if elem not in dict_parentesco:
                    dict_parentesco[elem] = 0
                
                dict_parentesco[elem] += 1
    
    print("\n\n\n\n")
    print(dict_parentesco)

def convert_to_json(parsed_file,output):

    if ".json" not in output:
        output = output + ".json"

    file = open(output, "w")
    file.write("[\n")

    for i in range(0,20):
        json.dump(data[i], file, indent= 3,separators=(',',': '))
        if i != 19: 
            file.write(",\n")
    file.write("\n]")
    
    file.close()


data = file_parse("./processos.txt")
freq_processos_ano(data)
top5_nomes_seculo(data)
freq_parentesco(data)
convert_to_json(data,"baguete")