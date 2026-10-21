from login import iniciar_sesion
from funciones_admin import menu_admin
from funciones_usuario import menu_usuario
def main():
    usuario, rol=iniciar_sesion()
    if rol=="administrador":
        menu_admin()
    elif rol=="usuario":
        menu_usuario()
if __name__=="__main__":
    main()