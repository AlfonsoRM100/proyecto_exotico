from negocio.publicaciones import publicaciones, Publicacion

def mostrar_menu_usuario(usuario):
    while True:
        print("\n---MENU USUARIO---")
        print("[1] Crear Publicacion")
        print("[2] Ver Publicaciones")
        print("[3] Dar Like a Publicacion")
        print("[4] Enviar Mensaje")
        print("[0] Exit")

        option = input("Seleccione una opcion: ")

        if option == '1':
            contenido = input("Ingrese publicacion: ")
            nueva_pub = Publicacion(contenido, usuario)
            publicaciones.append(nueva_pub)
            print("Publicacion creada exitosamente.")

        elif option == '2':
            if not publicaciones:
                print("No hay publicaciones disponibles.")
            else:
                for idx, pub in enumerate(publicaciones, start=1):
                    print(f"{idx}. {pub.contenido} - Likes: {pub.likes}")

        elif option == '0':
            print("Saliendo del menú de usuario...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")