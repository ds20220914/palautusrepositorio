class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen=0
        self.toiminta=0
    def miinus(self, operandi):
        self._arvo = self._arvo - operandi
        self._edellinen= operandi
        self.toiminta="-"
    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self._edellinen= operandi
        self.toiminta="+"
    def nollaa(self):
        self._edellinen=self._arvo
        self._arvo = 0
        self.toiminta="nollaa"
    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    def kumoa(self):
        if self.toiminta=="-":
            self._arvo = self._arvo+self._edellinen
            self._edellinen=0
            self.toiminta=0
        if self.toiminta=="+":
            self._arvo = self._arvo-self._edellinen
            self._edellinen=0
            self.toiminta=0
        if self.toiminta=="nollaa":
            self._arvo = self._edellinen
            self._edellinen=0
            self.toiminta=0
        if self.toiminta=="0":
            pass
