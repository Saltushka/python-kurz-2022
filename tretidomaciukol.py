import json
with open("body.json", mode="r", encoding="utf-8") as soubor:
    testDictionary = json.load(soubor)

pass_fail_dictionary = {}

for student, score in testDictionary.items():
    if score >= 60:
        pass_fail_dictionary[student] = "Pass"
    else:
        pass_fail_dictionary[student] = "Fail"

print(pass_fail_dictionary)