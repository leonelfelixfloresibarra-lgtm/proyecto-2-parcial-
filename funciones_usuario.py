from base_datos import mostrar_canciones,buscar_cancion
def menu_usuario():
    while True:
        print("\n"+"="*50)
        print("===MENU USUARIO===")
        print("1. Ver todas las canciones")
        print("2. Buscar canción")
        print("3. Salir")
        print("="*50)
        opcion=input ("elige una opcion: ")
        if opcion=="1":
            mostrar_canciones()
        elif opcion=="2":
            nombre=input("Ingrese el nombre de la canción a buscar: ")
            resultados= buscar_cancion(nombre)
            if resultados:
                print("\n---Resultados Encontrados---")
                for c in resultados:
                    print(f"{c['nombre']} - {c['artista']} - {c['album']}")
                else:
                    print("No se encontraron canciones con ese nombre.")
        elif opcion=="3":
            print("Saliendo del menú de usuario...")
            break
        else:
            print("Opción inválida. Intenta Nuevamente.")