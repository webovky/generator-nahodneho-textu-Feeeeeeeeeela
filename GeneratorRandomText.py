import random
try:
    pocet_slov = int(input("Zadej počet slov: \n"))
    jmeno_souboru = str(input("Jméno souboru: \n"))
except:
    print("zadal si neplatný formát :))))))))))")

jmeno_souboru += ".txt"
samohlasky = ["a","e","i","o","u","y"]
souhlasky = ["q","w","r","t","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
seznamslov = []
pocet_znaku = 0

for _ in range(pocet_slov):
    delka_slova = random.randint(1,7)
    slovo = []
    prvni = random.choice(samohlasky + souhlasky)   #náhoda, že bude začínat na samohlasku je 6:18 ->
    slovo.append(prvni)
                           #->což mi přijde ideální podle toho, jak moc se v češtině vyskytují
    for _ in range(delka_slova - 1):
        if slovo[-1] in samohlasky:
            slovo.append(random.choice(souhlasky))
        else:
            slovo.append(random.choice(samohlasky))       
    if pocet_znaku >= 73:
        seznamslov.append("\n")
        pocet_znaku = 0
        
    else:
        slovo.append(" ")
    slovo1 = ''.join(slovo)
    seznamslov.append(slovo1)
    pocet_znaku += (delka_slova + 1) 
with open(jmeno_souboru, "w", encoding = "utf-8") as textak:
    text = ''.join(seznamslov)
    textak.write(text)
