from auxiliares.info_app import nombre_aplicacion
from auxiliares.version import numero_version

def menu_principal():
    print()
    print(f'{nombre_aplicacion} {numero_version}')
    print('===============')
    print('[1]')
    print('[2]')
    print('[3]')
    print('[0] salir')
