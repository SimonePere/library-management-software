from libro import Libro
from libri_hardcodati import libri_hardcodati


class GestioneLibri:
    def __init__(self, db):
        self.db = db
        self.collection = db["elenco_libri"]

    def add_default_books(self):
        libri_default = libri_hardcodati

        # Inserisci i libri predefiniti nel database
        self.collection.insert_many(libri_default)
        print("Libri predefiniti aggiunti al database.")

    def reset_library(self):
        print("\n❗❗ **Attenzione** ❗❗")
        print(
            "Sei sicuro di voler eliminare irreversibilmente tutti i libri dal Database?"
        )
        magic_word = "CONFERMO ELIMINA TUTTO"
        you_sure = input(
            f"Digita '{magic_word}' per confermare"
            f"\nOppure qualsiasi tasto per tornare al menu principale:  "
        )
        if you_sure == magic_word:
            # Cancella tutti i libri
            self.collection.delete_many({})
            print("🗑️ **Tutti i libri sono stati eliminati dal database.**\n")
        else:
            print("↩️ **Operazione annullata.**\n")

    def create_book(self):
        """Crea un nuovo libro con validazione per ogni campo."""
        titolo = self._richiedi_input_convalida(
            "Titolo del libro", self.validate_text_field, "Titolo"
        ).title()
        autore = self._richiedi_input_convalida(
            "Autore del libro", self.validate_text_field, "Autore"
        ).title()
        genere = self._richiedi_input_convalida(
            "Genere del libro", self.validate_text_field, "Genere"
        ).title()
        codice = self._richiedi_input_convalida(
            "Codice ISBN (13 cifre)", self.validate_isbn
        )
        copie = self._richiedi_input_convalida("Numero di copie", self.validate_number)
        anno_pubblicazione = self._richiedi_input_convalida(
            "Anno di pubblicazione", self.validate_year
        )

        libro = Libro(
            titolo=titolo,
            autore=autore,
            genere=genere,
            codice=codice,
            copie=copie,
            anno_pubblicazione=anno_pubblicazione,
        )
        self.collection.insert_one(libro.to_dict())
        print(f"📚  Libro '{libro.titolo}' aggiunto con successo!")

    # @audit validazione di tutti i campi inseriti
    def _richiedi_input_convalida(self, prompt, validazione, *args):
        """Richiede un input e lo valida, continuando finché non è corretto."""
        while True:
            valore = input(f"Inserisci {prompt}: ").strip()
            if validazione(valore, *args):
                return valore
            print(f"❌ **Errore**: {prompt} non valido.")

    def validate_isbn(self, isbn):
        """Verifica che l'ISBN sia composto da 13 cifre numeriche."""
        return isbn.isdigit() and len(isbn) == 13

    def validate_number(self, numero):
        """Verifica che il campo sia numerico."""
        return numero.isdigit()

    def validate_year(self, year):
        """Verifica che l'anno sia composto da 4 cifre numeriche."""
        return year.isdigit() and len(year) == 4

    def validate_text_field(self, field, nome_campo):
        """Verifica che il campo testuale non sia vuoto."""
        if field:
            return True
        print(f"Errore: {nome_campo} non può essere vuoto.")
        return False

    def view_books_list(self):
        libri = list(self.collection.find())
        if not libri:
            print("\n📚 La libreria è vuota.\n")
        else:
            print("\n📚 Elenco completo dei libri:\n" + "=" * 40)
            for libro in libri:
                # Creiamo l'istanza di Libro ignorando `_id`
                print("📖")
                libro = {key: value for key, value in libro.items() if key != "_id"}
                for chiave, valore in libro.items():
                    print(f"{chiave.capitalize()}: {valore}")
                print("=" * 40)  # Separatore tra i libri

    def search_book_by_title(self, titolo=""):
        titolo = titolo.lower()  # Converte a minuscolo per la ricerca
        libro = self.collection.find_one(
            {"titolo": {"$regex": f"^{titolo}$", "$options": "i"}}
        )  # Cerca indipendentemente da maiusc/minusc
        if libro:
            libro = {key: value for key, value in libro.items() if key != "_id"}
            print("✔️  La ricerca ha prodotto i seguenti risultati:\n ")
            for chiave, valore in libro.items():
                print(f"{chiave.capitalize()}: {valore}")
            print("=" * 30)  # Separatore tra i libri
        else:
            print("✖️  Mi spiace, libro non trovato.")

    def remove_book(self, titolo):
        titolo = titolo.lower()  # Converte a minuscolo per la rimozione
        result = self.collection.delete_one(
            {"titolo": {"$regex": f"^{titolo}$", "$options": "i"}}
        )  # Elimina indipendentemente da maiusc/minusc
        if result.deleted_count:
            print(f"\n🗑️  Libro '{titolo}' eliminato con successo.\n")
        else:
            print("\n✖️  Libro non trovato.\n")
