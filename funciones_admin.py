from base_datos import agregar_cancion,mostrar_canciones
def menu_admin():
    while True:
        print("\n"+"="*50)
        print("===MENU ADMINISTRADOR===")
        print("1. Agregar canción")
        print("2. Ver todas las canciones")
        print("3. Salir")
        print("="*50)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            print("\n---Agregar Nueva Cancion---")
            nombre = input("nombre de la canción: ")
            artista = input("artista: ")
            album = input("álbum: ")
            genero = input("género: ")
            agregar_cancion(nombre, artista, album, genero)
        elif opcion == "2":
            mostrar_canciones()
        elif opcion == "3":
            print("Saliendo del menú de administrador...")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")