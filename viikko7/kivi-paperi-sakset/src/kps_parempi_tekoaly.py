from tekoaly_parannettu import TekoalyParannettu
from kivipaperisakset import KiviPaperiSakset

class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._parannettu_tekoaly = TekoalyParannettu(10)
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._parannettu_tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._parannettu_tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto
