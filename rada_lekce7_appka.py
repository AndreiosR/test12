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
    for letter in users:
        print(letter)

users_load()

def username_check():
    print("prohlášení: Pod tímto řádkem budou vypsána jednotlivá uživatelská jména!")
    users="Jaromír,Libor,Lubomír " 
    name=""
    for letter in users:
        if letter == "," or letter == " ":
            print(name)
            name=""
        else:
            name += letter

username_check()