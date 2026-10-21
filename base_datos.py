lista_canciones=[]
def agregar_cancion(nombre, artista, album, genero):
    cancion = {
        "nombre": nombre,
        "artista": artista,
        "album": album,
        "genero": genero
    }
    lista_canciones.append(cancion)
    print(f"Canción '{nombre}' agregada correctamente.")
    def mostrar_canciones():
        if len (lista_canciones) == 0:
            print("No hay canciones en la lista.")
            return
        print("\n"+ "="*50)
        print("LISTA DE CANCIONES")
        print("="*50)
        for i, c in enumerate(lista_canciones,1):
            print(f"{i}.{c['nombre']} - {c['artista']} [{c['genero']}]")
            print("="*50 + "\n")
    def buscar_cancion(nombre):
                resultados =[c for c in lista_canciones if nombre.lower() in c['nombre'].lower()]
                return resultados