class entry:

    def __init__(self,lineArgs):
        if(len(lineArgs) != 5):
            raise ValueError

        self._gender = lineArgs[0]
        self._tensao = lineArgs[1]
        self._colesterol = lineArgs[2]
        self._batimento = lineArgs[3]
        self._temDoença = lineArgs[4]

    def gender(self):
        return self._gender
    
    def tensao(self):
        return self._tensao

    def colesterol(self):
        return self._colesterol

    def batimento(self):
        return self._batimento
    
    def temDoença(self):
        return self._temDoença

    def __repr__(self):

        l = "gender :: '{}', tensao :: '{}', colesterol :: '{}', batimento :: '{}', temDoença :: '{}'".format(self._gender, self._tensao, self._colesterol,self._batimento,self._temDoença)
        return l 

def cria_dicionario():
    file = open("./myheart.csv")
    dict = {}
    file.readline()

    for line in file:
        list = line.strip('\n').split(',')
        if(list[0] not in dict.keys()):
            dict[list[0]] = []
            dict[list[0]].append(entry(list[1:6]))
        else:
            dict[list[0]].append(entry(list[1:6]))

    return dict

def doenca_por_sexo(dict):
    dm = 0
    df = 0

    for key in dict:    
        object = dict[key]
        for entry in object:
            gender = entry.gender()
            temDoença = entry.temDoença()
            
            if(gender == 'M' and temDoença == '1'):
                dm += 1

            elif(gender == 'F' and temDoença == '1'):
                df += 1

    return dm, df


def get_categoria(idade):
    resto = int(idade)%5

    return (int(idade)-resto,int(idade)-resto+4)


def agrupa_por_categoria(dict):

    dict_por_categoria = {}

    for key in dict:
        if(get_categoria(key) not in dict_por_categoria.keys()):
            dict_por_categoria[get_categoria(key)] = []
            for pessoa in dict[key]:
                dict_por_categoria[get_categoria(key)].append(pessoa)
        else:
            for pessoa in dict[key]:
                dict_por_categoria[get_categoria(key)].append(pessoa)
    
    return dict_por_categoria
        

def doenca_por_faixa_etaria(dict):
    dict_por_categoria = {}
    dict_por_categoria = agrupa_por_categoria(dict)

    for key in dict_por_categoria:
        r = 0
        for entry in dict_por_categoria[key]:
            r += int(entry.temDoença())
        
        dict_por_categoria[key] = r

    return sort_dict(dict_por_categoria)    


def get_colesterol(colesterol):
    resto = int(colesterol)%10

    return (int(colesterol)-resto,int(colesterol)-resto+9)

def agrupa_por_colesterol(dict):

    dict_por_colesterol = {}

    for val in dict.values():
        for pessoa in val:
            if(get_colesterol(pessoa.colesterol()) not in dict_por_colesterol.keys()):
                dict_por_colesterol[get_colesterol(pessoa.colesterol())] = []
                dict_por_colesterol[get_colesterol(pessoa.colesterol())].append(pessoa)
            else:
                dict_por_colesterol[get_colesterol(pessoa.colesterol())].append(pessoa)

    return dict_por_colesterol

def sort_dict (dictionary):
    sorted_keys = sorted(dictionary.keys())
    sorted_dict = {key:dictionary[key] for key in sorted_keys}
    
    return sorted_dict


def doenca_por_colesterol(dict):
    dict_por_colesterol = {}
    dict_por_colesterol = agrupa_por_colesterol(dict)

    for key in dict_por_colesterol:
        r = 0
        for entry in dict_por_colesterol[key]:
            r += int(entry.temDoença())
        
        dict_por_colesterol[key] = r
    
    return sort_dict(dict_por_colesterol)

def cria_tabela_por_dicionario(dict):
    print(f"   VALORES   |  QUANTIDADE")
    print( "-----------------------------")
    for key in dict:
        n = 11 - len(str(key))
        s = " " * (n+2)
        print(f"{key}{s}|   {dict[key]}")
    

def cria_tabela_por_genero(tuplo):
    print(f"   GÉNEROS   |  QUANTIDADE")
    print( "-----------------------------")
    print(f"      M      |      {tuplo[0]} ")
    print(f"      F      |      {tuplo[1]} ")

def main():
    dict = {}
    dict = cria_dicionario()
    print("\n\n\nDOENÇA POR GÉNERO\n")
    cria_tabela_por_genero(doenca_por_sexo(dict))
    print("\n\n\nDOENÇA POR FAIXA ETÁRIA\n")
    cria_tabela_por_dicionario(doenca_por_faixa_etaria(dict))
    print("\n\n\nDOENÇA POR FAIXA DE COLESTEROL\n")
    cria_tabela_por_dicionario(doenca_por_colesterol(dict))
    

if __name__ == "__main__":
    main()

