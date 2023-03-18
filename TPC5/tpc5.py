import re

def machine_answer(string:str):
    print("maq: "+ string)


def check_coin(coin:str):
    return (re.match(r"(^|,)(5|10|20|50)c",coin) != None) or (re.match(r"(^|,)(1|2)e",coin) != None)


def convert_coin_to_balance(coin:str):
    if coin == "5c":
        return 0.05
    
    elif coin == "10c":
        return 0.1
    
    elif coin == "20c":
        return 0.2

    elif coin == "50c":
        return 0.5
    
    elif coin == "1e":
        return 1.0
    
    elif coin == "2e":
        return 2.0
    
    return 0


def add_balance(coins:str):
    balance = 0.0
    coin_list = coins[6:].split(",")
    invalid_coins = []
    for coin in coin_list:
        if check_coin(coin):
            balance += convert_coin_to_balance(coin)
        else:
            invalid_coins.append(coin)

    if len(invalid_coins) == 1:
        machine_answer(invalid_coins.pop(0) + " - moeda inválida; saldo = " + float_to_change(balance))
    
    elif len(invalid_coins) > 1:
        machine_answer(", ".join(invalid_coins) + " - moedas inválidas; saldo = " + float_to_change(balance))
    
    return balance


def call(number:str, balance:float):
    first_dig = ""
    number = number[2:]

    if re.match(r"(601|604)\d+$",number):
        machine_answer("Esse número não é permitido neste telefone. Queira discar novo número!")

    elif re.match(r"(00)\d+$",number):
        if balance >= 1.5:
            balance -= 1.5
            first_dig = "00"
        else:
            machine_answer("Não possui saldo suficiente. Queira inserir mais moedas e discar novamente!")

    elif re.match(r"(2)\d+$",number) and len(number) == 9:
        if balance >= 0.25:
            balance -= 0.25
            first_dig = "2"
        else:
            machine_answer("Não possui saldo suficiente. Queira inserir mais moedas e discar novamente!")

    elif re.match(r"(800)\d+$",number) and len(number) == 9:
        None # doesn't cost any money
    
    elif re.match(r"(808)\d+$",number) and len(number) == 9:
        if balance >= 0.15:
            balance -=0.15
            first_dig = "808"
        else:
            machine_answer("Não possui saldo suficiente. Queira inserir mais moedas e discar novamente!")

    return balance,first_dig

def float_to_change(balance:float):
    lista = str(balance).split(".")

    return lista[0] + "e" + lista[1] + "c" 
def show_change(balance:float,onCall:bool,first_dig:str):
    call_dic = {"00": "1.5","2": "0.25" ,"808": "0.15"}

    if onCall:
        machine_answer("saldo = " + float_to_change(balance))
    else:
        if len(first_dig) > 0:
            balance += float(call_dic[first_dig])
            machine_answer("Tome os seus " + float_to_change(call_dic[first_dig]) + " de volta")
            machine_answer("saldo = " + float_to_change(balance))


def interaction():
    balance = 0.0
    onCall = True

    cl_msg = str(input())

    if re.match(r"(?i:LEVANTAR)",cl_msg):
        machine_answer("Introduza moedas!")
        cl_msg = str(input())

        while re.match(r"(?i:POUSAR)",cl_msg) == None:

            if re.match(r"(?i:MOEDA)",cl_msg):
                balance += add_balance(cl_msg)
                machine_answer("saldo = " + float_to_change(balance))

            elif re.match(r"(?i:T=)",cl_msg):
                balance,first_dig = call(cl_msg,balance)
                machine_answer("saldo = " + float_to_change(balance))
            
            elif re.match(r"(?i:ABORTAR)",cl_msg):
                onCall = False
                break
            
            else:
                machine_answer("Ação inválida ou inexistente!")

            cl_msg = str(input())
        else:
            machine_answer("Precisa de inserir moedas primeiramente!")

        show_change(balance,onCall,first_dig)
    else:
        machine_answer("Ação inválida ou inexistente!")

interaction()