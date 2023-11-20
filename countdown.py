import time
import os


def counter():
    os.system("cls")
    temp = int(input("type the time: "))
    temp_machine = 0
    while temp_machine <= temp: 
        print(temp_machine)
        temp_machine += 1
        time.sleep(1)
        os.system("cls")
    print("countdown was finished")


counter()
