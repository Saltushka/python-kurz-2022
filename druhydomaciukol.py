sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

article = input ("Prosim napiste kod soucastky: ")
articleQuantity = int(input ("Prosim napiste mnozstvi: "))

if article in sklad and articleQuantity > sklad[article]:
    print(f"lze prodat pouze omezené množství kusů. Jste zadal/a {articleQuantity} kusu. Maximalni pocet kusu lze objednat {sklad[article]}")
    sklad.pop(article)
    print(sklad)
elif article in sklad and articleQuantity <= sklad[article]:
    print("Poptávku lze uspokojit v plné výši")
    sklad[article] = sklad[article] - articleQuantity
    print(sklad)
else:
    print("Není součástka skladem")


