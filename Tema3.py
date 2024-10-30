meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]
tavi = ["tava"] * 7
istoric_comenzi = []

comenzi_servite = {"papanasi": 0, "ceafa": 0, "guias": 0}
incasari = 0
preturi_dict = dict(preturi)

for student, comanda in zip(studenti[:], comenzi[:]):
    print(f"{student} a comandat {comanda}.")
    istoric_comenzi.append(comanda)
    comenzi_servite[comanda] += 1
    incasari += preturi_dict[comanda]
    studenti.pop(0)
    comenzi.pop(0)
    tavi.pop()
    meniu.remove(comanda)

print(f"\nS-au comandat {comenzi_servite['guias']} guias, {comenzi_servite['ceafa']} ceafa, {comenzi_servite['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")
print("Mai există ceafa pe stoc." if 'ceafa' in meniu else "Nu mai există ceafa pe stoc.")
print("Mai există papanasi pe stoc." if 'papanasi' in meniu else "Nu mai există papanasi pe stoc.")
print("Mai există guias pe stoc." if 'guias' in meniu else "Nu mai există guias pe stoc.")

print(f"\nCantina a încasat: {incasari} lei.")
print("Produse care costă cel mult 7 lei:")
for produs, pret in preturi:
    if pret <= 7:
        print(f"{produs.capitalize()} {pret} lei")
