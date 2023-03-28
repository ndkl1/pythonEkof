# Pravljenje KLASE za sve zaposlene, svaki objekat predstavlja jednu osobu
class zaposleni():
    # pass 
    # PASS znaci da je klasa prazna - slicno kao NULL - moze da se koristi i u praznoj funkciji
    
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
    # __init__ je metoda koja se koristi da bi se objekti inicijalizovali, uvek ima prvu rec SELF
    # Self predstavlja instancu klase i njenim korišćenjem možemo pristupiti atributima i metodama klase
    
    # init ima __ sto predstavlja posebnu vrstu metode - zove se konstruktor i automatski se poziva kada neko kreira novi objekat iz klase. 
    # Konstruktor se obično koristi da se zadaju početne vrednosti varijablama iz klase.


# Pravljenje objekta iz klase - tako sto pozivamo ime klase kao da je funkcija
# Sa ovim pravimo jedan (individualni) objekat - jednu osobu od svih zaposlenih koja se zove Maja i preziva Jovic jer smo upravo to i definisali u samoj klasi
zaposleni1 = zaposleni('Nada','Kolakovic')
print("Zaposleni 1 se zove ",zaposleni1.ime,", a preziva ",zaposleni1.prezime) 
# print koristimo da bi prikazali ime i prezime ovog zaposlenog

# Sve ovo moze da se napise i na sledeci nacin ukoliko imamo samo jednog zaposlenog za koga zelimo da pokazemo informaciju:
#     def __init__(self):
#         self.ime = 'Nada Kolakovic'
# zaposleni2 = zaposleni()
# print(zaposleni2.ime)



