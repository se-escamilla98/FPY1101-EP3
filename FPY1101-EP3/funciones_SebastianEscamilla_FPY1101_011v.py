libros_prestados = []
def registrar_libro (libros):
    print(" ")
    nombre_del_libro = input("ingrese los datos del libro que quiere ingresar a la biblioteca. \nIngrese el titulo del libro: ")
    autor_libro = input ("\n\t Ingrese nombre de autor: ")
    ano_de_pbli = input ("\n\t Año de publicacion: ")
    Sku_libro = input ("\n\tAsigne un SKU para el libro (año - autor) : ")
        
    libros.append({
        "nombre" : nombre_del_libro,
        "autor_libro": autor_libro,
        "ano_de_pbl":ano_de_pbli,
        "sku": Sku_libro
        })

def listado_libros (libros):
    print("listado de libros")
    for libro in libros:
        print(libro)


def prestamos_libro (libros):
    nombre_usuario = input ("ingrese su nombre para el prestamo: ")
    Sku_libro = input("ingrese el sku del libro deseado: ")
    for Sku_libro in libros_prestados:
        if Sku_libro not in libros_prestados:
            libros_prestados.append({'nombre':nombre_usuario, 'sku':Sku_libro})
            print("Su prestamo a sido autorizado")
            
        elif Sku_libro in libros_prestados:
                    print("Este libro ya se encuentra prestado")
                                                                            
                                                                                     
def planilla_prestamos (libros_prestados):
    Sku_libro = input("Ingrese el sku del libro prestado")
    
    if Sku_libro == libros_prestados[1]:
        archivo_planilla = "planilla de prestamos.txt"
        with open (archivo_planilla, "w") as archivo:
            for libros_prestados in libros_prestados:
                
                archivo.write(f"nombre del usuario: {libros_prestados['nombre']}\n")
                archivo.write(f"sku: {libros_prestados[1]}\n")
    else:
        print("Libro no encontrado, intente de nuevo")
