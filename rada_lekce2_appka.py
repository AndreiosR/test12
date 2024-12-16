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

cml_calculate()