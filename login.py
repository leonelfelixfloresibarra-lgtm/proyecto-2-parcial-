usuarios={"admin": {"clave":"123", "rol": "administrador"},"usuario": {"clave":"123", "rol": "usuario"}}
def iniciar_sesion():
    print ("="*40)
    print ("SISTEMA DE GESTION DE MUSICA")
    print ("="*40)
    intentos = 3
    while intentos > 0:
        usuario=input("Usuario: ")
        clave=input("Contraseña: ")
        if usuario in usuarios and usuarios[usuario]["clave"]== clave:
            print (f"\n Bienevenido {usuario}!")
            print (f"Rol: {usuarios[usuario]['rol']}")
            return usuario, usuarios[usuario]["rol"]
        else:
            intentos -= 1
            print (f"Usuario o contraseña incorrectos. Te quedan {intentos} intentos.")
            print ("Acceso Bloqueado.")
            if __name__ == "__main__":
                iniciar_sesion()