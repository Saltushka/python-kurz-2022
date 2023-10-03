jmeno = input("Zadejte prosim Vase jmeno a prijmeni: ")
print (jmeno.upper())
print (jmeno.lower())
splitted_name = jmeno.split()
print (splitted_name [0].capitalize()+ " " + splitted_name [1].capitalize())
print (splitted_name [0][0].upper() + ". " + splitted_name[0][1].upper() + ".")
if len (splitted_name[0]) >5:
    print (splitted_name [0][0].upper() + " " + splitted_name[1].capitalize())   