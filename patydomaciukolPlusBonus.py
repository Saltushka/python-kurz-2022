def mean(seznam):
    return sum(seznam)/len(seznam)

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumerne_teploty = [] 
for den in teploty:
    prumerne_teploty.append(sum(den)/len(den))
print(prumerne_teploty)

prumerne_teploty = [sum(den)/len(den) for den in teploty] 
print(prumerne_teploty)

prumerne_teploty = [mean(den) for den in teploty] 
print(prumerne_teploty)

#seznam ranních teplot.
print([den[0] for den in teploty])

#seznam nočních teplot.
print([den[-1] for den in teploty])

#seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
print([[den[1], den[-1]] for den in teploty])



#BONUS zadani

def mean(seznam):
    return sum(seznam)/len(seznam)

teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

slovnik = {den[0]: mean(den[1:]) for den in teploty}

print(slovnik)