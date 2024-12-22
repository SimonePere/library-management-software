from cx_Freeze import setup, Executable

setup(
    name="LibreriaMele",
    version="1.0",
    description="Gestionale magazzino della Libreria Mele",
    executables=[Executable("index.py")],
)
