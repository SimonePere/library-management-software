from gestione_interfaccia import GestioneInterfaccia
from gestione_libri import GestioneLibri


def main():
    interfaccia = GestioneInterfaccia()
    interfaccia.view_menu()


if __name__ == "__main__":
    main()


# @audit Reset e inserimento dei dati hardcoded
# gestore_libri.reset_library()
# gestore_libri.add_default_books()
