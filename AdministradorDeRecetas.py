import os
from os import system
from pathlib import Path
ruta_origen = Path.home() / "Recetas"
finalizar_programa = False


def contar_recetas(ruta) -> int:
    cont = 0
    for archivo in ruta.glob("**/*.txt"):
        cont += 1
    return cont


def mostrar_menu() -> None:
    print("Lista de Opciones: ")
    print("*"*30)
    print("1) Leer una receta.")
    print("2) Crear una nueva receta.")
    print("3) Crear una nueva categoria.")
    print("4) Eliminar una receta.")
    print("5) Eliminar una categoria.")
    print("6) Salir del programa.")
    print("*"*30)


def inicio(ruta) -> int:
    system("cls")
    print("*"*55)
    print("\tBienvenido al administrador de recetas!\n")
    print("*"*55)
    print(f'Las recetas se encuentran en \"{ruta}\"')
    print(f'Tenemos un total de {contar_recetas(ruta)} recetas!')
    eleccion = "x"
    while not eleccion.isnumeric() or int(eleccion) not in range(1, 7):
        print("Elija una de las siguientes opciones: ")
        mostrar_menu()
        eleccion = input("Opcion a elegir: ")
    return int(eleccion)


def volver_inicio() -> None:
    eleccion = 'x'
    while eleccion.lower() != 'v':
        eleccion = input('Ingrese "v" para volver al inicio: ')


def mostrar_categorias(ruta) -> list:
    print("Categorias: ")
    categorias = []
    ruta_categorias = Path(ruta)
    cont = 1
    for carpeta in ruta_categorias.iterdir():
        nombre = str(carpeta.name)
        categorias.append(carpeta)
        print(str(cont) + ") " + nombre)
        cont += 1
    return categorias


def elegir_categoria(lista) -> str:
    eleccion = 'x'
    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista)+1):
        eleccion = input("Opcion: ")
    return lista[int(eleccion)-1]


def mostrar_recetas(ruta) -> Path:
    ruta_recetas = Path(ruta)
    recetas = [x for x in ruta_recetas.iterdir()]
    eleccion = 'x'
    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(recetas)+1):
        print("Recetas: ")
        cont = 1
        for r in recetas:
            print(str(cont) + ") " + r.name)
            cont += 1
        eleccion = input("Opcion: ")
    return recetas[int(eleccion)-1]


def leer_receta(ruta) -> None:
    print("Receta: ")
    print("*"*55)
    contenedor_receta = Path(ruta).read_text()
    print(contenedor_receta)
    print("*"*55)


def crear_receta(ruta) -> None:
    existe = False
    while not existe:
        nombre_receta = input("Nombre de la receta: ") + ".txt"
        ruta_receta = Path(ruta / nombre_receta)
        contenedor_receta = input("Escribe la receta: ")
        if not os.path.exists(ruta_receta):
            Path.write_text(ruta_receta, contenedor_receta)
            print(f'Tu receta {nombre_receta}, ha sido creada exitosamente!')
            existe = True
        else:
            print(
                f'Tu receta {nombre_receta}, no pudo ser creada porque ya existe!')


def crear_categoria(ruta) -> None:
    existe = False
    while not existe:
        nombre_categoria = input("Nombre de la categgoria: ")
        ruta_categoria = Path(ruta / nombre_categoria)
        if not os.path.exists(ruta_categoria):
            Path.mkdir(ruta_categoria)
            print(
                f'Tu categoria {nombre_categoria}, ha sido creada exitosamente!')
            existe = True
        else:
            print(
                f'Tu categoria {nombre_categoria}, no pudo ser creada porque ya existe!')


def eliminar_receta(ruta) -> None:
    Path(ruta).unlink()
    print(f'La receta {ruta.name} ha sido eliminada!')


def eliminar_categoria(ruta) -> None:
    Path(ruta).rmdir()
    print(f'La categoria {ruta.name} ha sido eliminada!')


while finalizar_programa == False:
    opcion = inicio(ruta_origen)
    # Leer recetas
    if opcion == 1:
        lista_categoria = mostrar_categorias(ruta_origen)
        categoria_seleccionada = elegir_categoria(lista_categoria)
        receta_seleccionada = mostrar_recetas(categoria_seleccionada)
        leer_receta(receta_seleccionada)
        volver_inicio()
    # Crear recetas
    elif opcion == 2:
        lista_categoria = mostrar_categorias(ruta_origen)
        categoria_seleccionada = elegir_categoria(lista_categoria)
        crear_receta(categoria_seleccionada)
        volver_inicio()
        pass
    # Crear categorias
    elif opcion == 3:
        crear_categoria(ruta_origen)
        volver_inicio()
    # Eliminar Recetas
    elif opcion == 4:
        lista_categoria = mostrar_categorias(ruta_origen)
        categoria_seleccionada = elegir_categoria(lista_categoria)
        receta_seleccionada = mostrar_recetas(categoria_seleccionada)
        eliminar_receta(receta_seleccionada)
        volver_inicio()
    # Eliminar Categoria
    elif opcion == 5:
        lista_categoria = mostrar_categorias(ruta_origen)
        categoria_seleccionada = elegir_categoria(lista_categoria)
        eliminar_categoria(categoria_seleccionada)
        volver_inicio()
    # Salir del Programa
    elif opcion == 6:
        print("*"*55)
        print("Gracias por utilizar nuestro programa!")
        print("Cerrando el programa...")
        print("*"*55)
        finalizar_programa = True
