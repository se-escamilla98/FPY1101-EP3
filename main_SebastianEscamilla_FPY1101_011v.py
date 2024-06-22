import funciones_menu as fn
libros = []
menu = "1. Registrar libro\n2. Prestar libro\n3. Listar libros\n4. Imprimir reporte de prestamos\n5. Salir"
while True:
    try:
        print(menu)
        op = int(input("Bienvenido, para empezar elija una opcion: "))
        if op == 1:
            fn.registrar_libro(libros)
        elif op == 2:
            fn.prestamos_libro(libros)
        elif op == 3:
            fn.listado_libros(libros)
        elif op == 4:
            fn.planilla_prestamos(libros)
        elif op == 5:
            print("Programa Finalizado\n\tDeveloped by: Sebastian Marcelo Escamilla Vazques.\n\t20.099.239-3")
            break
    except ValueError:
        print("Ingrese solo valores numericos del 1 al 5.")
