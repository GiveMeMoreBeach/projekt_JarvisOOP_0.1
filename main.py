from DesktopMenager import DesktopManager
from Speech_Engine import Talk

class Main:
    def __init__(self):
        self.engine = Talk()
        self.user = "Kacper"
        self.isWorking = True
        self.dm = DesktopManager(self.engine)
        self.version = 1.0

    def zakoncz(self):
        self.engine.talk("Do widzenia, panie")
        self.isWorking = False

    def desktop_manager_action(self):
        self.engine.talk("Odpalam menadzera pulpitu. Powiedz co chcemy tu zrobić")
        komenda_dm = self.engine.listen()
        if "ile" in komenda_dm or "plików" in komenda_dm:
            self.dm.ile_plikow()
        elif "stworz" in komenda_dm:
            self.dm.stworz_folder("testowy")

    def Start(self):
        print(f"\n Menu Jarvis ver{self.version}\n")
        self.engine.talk(f"Dzien dobry {self.user} w czym moge pomoc?")
        while self.isWorking:
            print("\n 1.Desktop Menager || 2.Zakończ")
            komenda = self.engine.listen()

            if "manager" in komenda or "pulpit" in komenda:
                self.desktop_manager_action()
            elif "zakończ" in komenda or "wyłącz" in komenda:
                self.zakoncz()

if __name__ == "__main__":
    app = Main()
    app.Start()
