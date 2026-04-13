import os
from send2trash import send2trash
from Speech_Engine import Talk

class DesktopManager(object):
    def __init__(self):
        self.pulpit = os.path.join(os.path.expanduser("~"),"Desktop")
        self.sciezka_pliki = os.path.join(os.path.expanduser("~"),"Pliki")
        self.talk = Talk()

    def lista_plikow(self):
        return os.listdir(self.pulpit)


    def ile_plikow(self):
        pliki = self.lista_plikow()
        self.talk.talk(f"Na Pulpicie jest {len(pliki)} plikow")


    def stworz_folder(self,nazwafolderu):
        sciezka = os.path.join(self.pulpit,nazwafolderu)
        if not os.path.exists(sciezka):
            os.mkdir(sciezka)
            self.talk.talk(f"Folder {nazwafolderu} zostal stworzony")
        else:
            self.talk.talk(f"Folder {nazwafolderu} już istnieje")


    def stworz_plik(self,nazwa):
        sciezka = os.path.join(self.pulpit,nazwa)
        if not os.path.exists(sciezka):
            open(sciezka,"w").close()
            self.talk.talk("Plik zostal stworzony")
        else:
            self.talk.talk("[Plik  już istnieje")


    def stworz_plik_z_zawartoscia(self,nazwa,tresc):
        sciezka = os.path.join(self.pulpit,nazwa)
        if not os.path.exists(sciezka):
            with open(sciezka,"w") as f:
                f.write(tresc)
            self.talk.talk("Plik zostal stworzony")
        else:
            self.talk.talk("Plik juz istnieje")

    def usun_plik_do_kosza(self,nazwa):
        sciezka = os.path.join(self.pulpit,nazwa)
        if not os.path.exists(sciezka):
            self.talk.talk(f"Folder {nazwa} nie istnieje")
        else:
            send2trash(sciezka)
            self.talk.talk(f"Folder {nazwa} zostal usunięty")


    def usun_plik_klucz(self,klucz):
        licznik = 0
        for plik in self.sciezka_pliki:
            if klucz.lower() in plik.lower():
                sciezka = os.path.join(self.pulpit,plik)
                send2trash(sciezka)
                print(f"plik o nazwie {plik} zostal usuniety ")
                licznik += 1
        if licznik > 0:
            self.talk.talk(f"Zdołałem usunąć : {licznik} plik")
        else:
            self.talk.talk("Nie usunalem zadnego pliku")
