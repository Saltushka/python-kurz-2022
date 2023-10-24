import math

number = input("Prosim napiste cislo: ")
smsCost = 3

def verify(number):
    if len(number) == 13:
        return number[0:4] == "+420"

def calculatePriceSMS(text):
    print(len(text)) #for verification - can be deleted
    numberOfTextBlocks = math.ceil(len(text) / 180)
    print(numberOfTextBlocks) #for verification - can be deleted
    return numberOfTextBlocks * smsCost

if verify(number) == True:
    smsText = input("Prosim napiste text: ")
    print(f"Cena za sms zpravu bude: {calculatePriceSMS(smsText)} kc")
else:
    print("Prosim zadejte spravne cislo")