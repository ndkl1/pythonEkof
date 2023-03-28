#ZADATAK 1

# Napraviti klasu Pravugaonik, upotrebiti metodu __init__ sa argumentima duzina i sirina.
# Napraviti u okviru ove klase dve nove metode obim i povrsina tako da za svaki pravugaonik
# moze da se izracuna.
# TEST: Izracunati obim i povrsinu pravugaonika sa sirinom od 120cm i duzinom 160cm

class Pravugaonik():
    def __init__(self, duzina, sirina):
        self.duzina = duzina
        self.sirina = sirina
    
    def obim(self):
        return 2*(self.duzina+self.sirina)
    
    def povrsina(self):
        return self.duzina*self.sirina
    
# Kao i svaka druga metoda (kao i __init__) i obicne napravljene moraju da sadrze SELF.
# Svaki put kada se pozovete na neku od varijabli ili metoda
# iz klase morate reč self staviti ispred naziva varijable ili metode.
# SELF.ARGUMENT

p1 = Pravugaonik(120, 160)
print("Obim ovog pravugaonika je: ", p1.obim())
print("Povrsina je: ", p1.povrsina())
# PAZI! kod obim i povrsina moraju da stoje i (), jer su to metode 