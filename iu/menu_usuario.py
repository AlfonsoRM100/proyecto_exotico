def mostrar_menu_usuario():
    while True:
        print("\n---MENU USUARIO---")
        print("[1] Crear Publicacion")
        print("[2] Ver Publicaciones")
        print("[3] DAR Like a Publicacion")
        print("[4] Enviar Mensaje")
        print("[0] Exit")


        option = input("Seleccione una opcion: ")
        if option == '1':

            print("Crear Publicacion seleccionado.")
        elif option == '2':

            print("Ver Publicaciones seleccionado.")
        elif option == '3':

            print("DAR Like a Publicacion seleccionado.")
        elif option == '4':

            print("Enviar Mensaje seleccionado.")
        elif option == '0':
            
            print("Saliendo del menú de usuario...")
        else:
            print("Opción no válida. Intente de nuevo.")