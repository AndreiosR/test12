def cml_calculate():
    print("Kolik vážíš?")
    try:
        hmotnost = float(input())
    except ValueError:
        print("You must enter a number")
        hmotnost=float(input())
    cml = hmotnost*24.2*1.2
    cml = round(cml, 2)
    print(cml)


def working():
    from random import randint
    from random import randrange
    myn1=str(randint(1,10))
    myn2=str(randrange(20,100,10))
    print("Právě teď musíš udělat "+myn1+" dřepů.")
    print("Dnes ještě musíš udělat "+myn2+" dřepů.")

def oslovenii():
    print("Pohlaví (pište s malými písmeny a s diakritikou)")
    pohlavi=input()
    osloveni="Dobrý den, "
    if pohlavi=="muž":
        print(osloveni+"Vážený pane!")
    elif pohlavi=="žena":
        print(osloveni+"vážená paní!")
    else:
        print(osloveni+"vaše pohlaví je "+pohlavi+".")

oslovenii()
cml_calculate()
working()