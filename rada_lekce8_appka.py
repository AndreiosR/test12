"""
def cml_calculate():
    weight_invalid=True
    while weight_invalid:
        try:
            print("Kolik vážíš:")
            hmotnost=float(input())
            weight_invalid=False
        except ValueError:
            print("Vepiš číslo, prosím")
    

    try:
        hmotnost = float(input())
    except ValueError:
        print("You must enter a number")
        hmotnost=float(input())
    
    
    cml = hmotnost*24.2*1.2
    cml = round(cml, 2)
    print(cml)



def oslovenii():
    pohlavi_vldtn=True
    osloveni="Dobrý den, "
    while pohlavi_vldtn:
            print("Pohlaví (pište s malými písmeny a s diakritikou)")
            pohlavi=input()
            if pohlavi=="muž":
                print(osloveni+"Vážený pane!")
                pohlavi_vldtn=False
            elif pohlavi=="žena":
                print("Preferujete za a) Vážená paní nebo za b) Vážená slečno? (Odpověďte buď malým písmenem a nebo malým písmenem b...)")
                damske_osloveni=input()
                if damske_osloveni=="a":
                    print(osloveni+"Vážená paní!")
                    pohlavi_vldtn=False
                elif damske_osloveni=="b":
                    print(osloveni+"Vážená slečno!")
                    pohlavi_vldtn=False
            else:
                print("Vepiš 'muž' nebo 'žena', prosím")
                pohlavi_vldtn=True


oslovenii()
cml_calculate()
# Zakomentování provedeno zkratkou buď Ctrl+ˇ, případně Alt+35
# working()
"""






# def fce():
    # times_table = 5
    # answer = 0
    # print(f"Here is the {times_table} times table")
    # for x in range(1,11):
        # answer = x * times_table
        # print(f"{x} times {times_table} is {answer}")

# fce()


def users_load():
    users="Jaromír,Libor,Lubomír " 
    for l in users:
        print(l)

users_load()

def username_check():
    print("prohlášení: Pod tímto řádkem budou vypsána jednotlivá uživatelská jména!")
    users="Jaromír,Libor,Lubomír " 
    name=""
    for l in users:
        if l == "," or l == " ":
            print(name)
            name=""
        else:
            name += l

username_check()