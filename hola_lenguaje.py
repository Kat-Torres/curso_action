import os

def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GITHUB!")
    lenguaje =  os.getenv("LANGUAGE")
    print(f"¡lenguaje favorito, {lenguaje}")

if __name__== "__main__":
    main()
