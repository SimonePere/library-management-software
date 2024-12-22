class Libro:
    def __init__(
        self,
        titolo="Unknown",
        autore="Unknown",
        anno_pubblicazione=0,  # deve essere 4 cifre
        genere="Unknown",
        codice=1111111111111,  # deve essere 13 cifre
        copie=0,  # deve essere numerico
    ):
        self.titolo = titolo
        self.autore = autore
        self.genere = genere
        self.anno_pubblicazione = anno_pubblicazione
        self.codice = codice
        self.copie = copie

    def to_dict(self):
        return {
            "titolo": self.titolo,
            "autore": self.autore,
            "genere": self.genere,
            "anno di pubblicazione": self.anno_pubblicazione,
            "ISBN": self.codice,
            "copie": self.copie,
        }

    def __str__(self):
        return (
            f"\n📚Titolo: {self.titolo} 📚\n"
            f"Autore: {self.autore}\n"
            f"Genere: {self.genere}\n"
            f"Anno di pubblicazione: {self.anno_pubblicazione}\n"
            f"ISBN: {self.codice}\n"
            f"Copie disponibili: {self.copie}\n"
            f"{'-'*30}"
        )
