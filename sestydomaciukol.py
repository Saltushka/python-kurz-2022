class Auto:
    def __init__(self, 
                 registracni_znacka,
                 typ_vozidla,
                 najete_km, 
                 dostupne = True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne
        
    # Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. 
    # Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu dostupne,
    # který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo 
    # již půjčené, vrátí text "Vozidlo není k dispozici


    def pujc_auto(self):                       
            if self.dostupne == True:
                self.dostupne = False
                return "Potvrzuji zapůjčení vozidla"
            else:                
                return "Vozidlo není k dispozici"

    # Dále tříde Auto přidej funkci get_info(), 
    # která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

    def get_info(self):
        return f"registracni znacka: {self.registracni_znacka} typ vozidla: {self.typ_vozidla}"
        
Peugeot = Auto ("4A2 3020", "Peugeot 403 Cabrio", 47534)
Škoda = Auto ("1P3 4747", "Škoda Octavia", 41253)

"""Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. 
Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci 
o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto()."""

inputAuto = input("Jakou značku si přejete půjčit: Peugeot nebo Škoda? ")
if inputAuto.lower() == "peugeot":
    auto = Peugeot    
elif inputAuto.lower() == "škoda":
    auto = Škoda    
else:
    print("Neplatný výběr značky vozidla.")

# Auto informace:
print(auto.get_info())

# First time renting Auto:
print(auto.pujc_auto())

# Verify if selected car is available to rent again:
print(auto.pujc_auto())
