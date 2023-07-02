todos = []
while True:
    accion = input('Ingresa una accion Agregar (a) , Mostrar (m), Salir (s):')
    match accion:
        case 'a':
            todo = input('Ingresa una tarea:')
            todos.append(todo.capitalize())
        case 'm':
            for a in todos:
                print(a)
        case 's':
            break

print('Saliendo del programa...')