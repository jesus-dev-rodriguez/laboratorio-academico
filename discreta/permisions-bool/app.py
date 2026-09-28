from permissions import Permissions

lectura = Permissions(Permissions.Read)
creacion = Permissions(Permissions.Create)
eliminacion = Permissions(Permissions.Delete)
actualizacion = Permissions(Permissions.Update)


def eliminar_recurso(p: Permissions, recurso: str):
    if p * eliminacion == eliminacion:
        print("U: elimino", recurso)
    else:
        print("U: No tiene los permisos para eliminar", recurso)

def permisos_usuario(p:Permissions):
    if p * lectura == lectura: print("U: tiene permiso de lectura")
    if p * creacion == creacion: print("U: tiene permiso de creacion")
    if p * eliminacion == eliminacion: print("U: tiene permiso de eliminacion")
    if p * actualizacion == actualizacion: print("U: tiene permiso de actualizacion")

if __name__ == "__main__":
    user = Permissions(Permissions.Read)
    recurso = "Tarea: 124"

    print("# Permisos de usuario")
    permisos_usuario(user)

    print("\n## Intentando eliminar un recurso")
    eliminar_recurso(user, recurso)

    print("\n## Añadiendo permiso de eliminiacion")
    user = user + eliminacion
    permisos_usuario(user)
    
    print("\n## Intentando eliminar un recurso")
    eliminar_recurso(user, recurso)

    print("\n## Quitando permiso de eliminiacion")
    user = user * ~eliminacion
    permisos_usuario(user)

    print("\n## Intentando eliminar un recurso")
    eliminar_recurso(user, recurso)

    print("\n## Usuario con todos los permisos")
    user = Permissions(Permissions.Full)
    permisos_usuario(user)

    print("\n## Intentando eliminar un recurso")
    eliminar_recurso(user, recurso)
    
    print("\n## Quitando los permisos de creacion y eliminacion")
    user = user * ~(creacion + eliminacion)
    permisos_usuario(user)

    print("\n## Usuario con todos los permisos")
    user = Permissions(Permissions.Full)
    permisos_usuario(user)

    print("\n## Quitando los permisos de creacion y eliminacion")
    user = user - creacion - eliminacion
    permisos_usuario(user)

    
