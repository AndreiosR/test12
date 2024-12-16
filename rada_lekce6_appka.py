

def cml_calculate():
    weight_invalid=True
    while weight_invalid:
        try:
            print("Kolik vážíš:")
            hmotnost=float(input())
            weight_invalid=False
        except ValueError:
            print("Vepiš číslo, prosím")
    """
    try:
        hmotnost = float(input())
    except ValueError:
        print("You must enter a number")
        hmotnost=float(input())
    """
    cml = hmotnost*24.2*1.2
    cml = round(cml, 2)
    print(cml)

"""
def working():
    from random import randint
    from random import randrange
    myn1=str(randint(1,10))
    myn2=str(randrange(20,100,10))
    print("Právě teď musíš udělat "+myn1+" dřepů.")
    print("Dnes ještě musíš udělat "+myn2+" dřepů.")
"""

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