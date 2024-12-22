from InquirerPy import prompt
from database_mongo import DatabaseMongo
from gestione_libri import GestioneLibri


class GestioneInterfaccia:
    def __init__(self):
        self.db_mongo = DatabaseMongo()
        self.db_mongo.connetti()
        self.gestione_libri = GestioneLibri(self.db_mongo.db)

    def view_menu(self):
        domanda = {
            "type": "list",
            "name": "scelta",
            "message": "Menu Libreria Mele:",
            "choices": [
                "Visualizza elenco completo",
                "Aggiungi nuovo libro",
                "Cerca",
                "Elimina libro",
                "Riempi libreria",
                "Cancella tutta la libreria",
                "Chiudi programma",
            ],
        }

        while True:
            ask = prompt(domanda)
            if ask["scelta"] == "Visualizza elenco completo":
                self.gestione_libri.view_books_list()
            elif ask["scelta"] == "Aggiungi nuovo libro":
                self.gestione_libri.create_book()
            elif ask["scelta"] == "Cerca":
                titolo = input("Inserisci il titolo del libro da cercare: ")
                self.gestione_libri.search_book_by_title(titolo)
            elif ask["scelta"] == "Elimina libro":
                titolo = input("Inserisci il titolo del libro da rimuovere: ")
                self.gestione_libri.remove_book(titolo)

            elif ask["scelta"] == "Riempi libreria":
                self.gestione_libri.add_default_books()

            elif ask["scelta"] == "Cancella tutta la libreria":
                self.gestione_libri.reset_library()
            elif ask["scelta"] == "Chiudi programma":
                self.db_mongo.disconnetti()
                print("Uscita dal programma.")
                break
            else:
                print("Operazione non valida. Riprova.")
