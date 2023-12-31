from kivipaperisakset import KiviPaperiSakset
from start import luo_peli
def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        if vastaus.endswith("a") or vastaus.endswith("b") or vastaus.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            start= KiviPaperiSakset.luo_peli(vastaus,luo_peli)
            start.pelaa()

        else:
            break

if __name__ == "__main__":
    main()
