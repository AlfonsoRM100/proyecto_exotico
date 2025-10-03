from auxiliares.info_app import nombre_aplicacion
from auxiliares.version import numero_version
from iu.menu_usuario import  mostrar_menu_usuario
from iu.registro import registrar_usuario
def menu_principal():
    while True:


        print()
        print(f'{nombre_aplicacion} {numero_version}')
        print('===============')
        print('[1.Crear Usuario]')
        print('[2.Iniciar Sesion]')
        print('[3.Exit]')
        
        
        opcion = input('Seleccione una opcion: ')
        if opcion == '1':

            registrar_usuario()
        elif opcion == '2':
            from iu.login import iniciar_sesion
            iniciar_sesion()
        elif opcion == '3':
            print('Saliendo de la aplicacion...')
            break
        else:
            print('Opcion no valida. Intente de nuevo.')
