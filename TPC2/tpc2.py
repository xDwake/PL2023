import string

def main():
    translator = str.maketrans('', '', string.punctuation.replace('=', ''))
    buffer = input().translate(translator).split(" ")
    somar = False
    val = 0
    for palavra in buffer:
        if palavra.lower() == "on":
            somar = True

        elif palavra.lower() == "off":
            somar = False
            
        elif palavra == "=":
            print(val)
        
        elif somar == True :
            if palavra.isdigit():
                val += int(palavra)
        
        else:
            val = val

main()
