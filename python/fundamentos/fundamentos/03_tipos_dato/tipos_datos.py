# #🔘 Booleanos: Se utiliza para representar valores de verdad en la lógica.
# #  Solamente puede tener dos valores: True o False (Nota que ponemos la T y la F en mayúsculas).
mayor_edad = True
tiene_bigote = False

# #🔢 Números: Aquí podemos tener números enteros,
# #  de punto flotante (también conocidos como números decimales) o complejos.
mayoria_edad = 18
altura = 1.72

# #🔤 Strings: También conocidas como cadenas, se refiere a textos o cadenas de caracteres.
frase = "Anita lava la tina"

# 🧩 Tipos de datos compuestos
# Estas con colecciones compuestas de los datos primitivos vistos anteriormente.

# 📋 Listas: Tipo de datos mutable (que puede cambiar) y contiene un conjunto de distintos valores. Suele utilizarse para almacenar información relacionada.

lista_vacia = []
gatos = ["Garfield", "Silvestre", "Hello Kitty"]
print(gatos[2]) #Imprime: Silvestre
gatos[1] = "Tom"
gatos.append("Felix")
print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty', 'Felix']
gatos.pop()
print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty']
gatos.pop(1)
print(gatos) #Imprime: ['Garfield', 'Hello Kitty']
# 🔒 Tuplas: Tipo de datos inmutable (que no se puede modificar) y contiene un conjunto de distintos valores. Pueden contener distintos tipos de datos.

perro = ("Scooby Doo", "Gran Danés", "Scooby Galletas", 7)
print(perro[0]) #Imprime: Scooby Doo
#perro[2] = "comida de perro" #ERROR: Las tuplas no pueden ser modificadas (TypeError: 'tuple' object does not support item assignment)
# 🗂️ Diccionarios: Nos permite almacenar contenido a través de una llave y un valor. Podemos acceder a sus datos a través de su índice único (que en este caso llamaremos llave o clave). Encuentra algunos métodos integrados de los diccionarios aquí.

diccionario_vacio = {}
persona = {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False}
persona['nombre'] = 'Valeria'  # Actualiza si el valor de la llave existente
persona['hobbies'] = ['jugar videojuegos', 'programación'] 

# # Agrega esa clave-valor si no existía previamente
print(persona)

# # Imprime: {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']}
altura = persona.pop('altura')  # Elimina la clave indicada y devuelve el valor
print(altura)    # Imprime: 1.71
print(persona) 

# # salida: {'nombre': 'Carmen', 'edad': 31, 'usa_lentes': False, 'hobbie

# las tuplas son inmutables, es decir que no pueden ser modificadas. Crear una tupla es tan sencillo como declarar distintos valores separados por comas; opcionalmente podemos ponerlos entre los paréntesis ().

tupla_letras = ("a", "e", "i", "o", "u")
tupla_sin_parentesis = "a", "e", "i", "o", "u"
# Las tuplas agrupan un conjunto de elementos que pueden contener cualquier tipo de dato.

gato = ("Miu", 5, "persa", False)
# Las tuplas son útiles para representar lo que en otros lenguajes de programación se conocen como records o registros, ya que nos permiten unir información relacionada y utilizarla como una sola entidad.

# Para consultar la información de una tupla lo hacemos a través de su índice, tal como lo hacíamos con las listas.

print(gato[0]) #Imprime: Miu
# Recuerda que las tuplas son inmutables, por lo que al intentar cambiar el valor de algún índice obtendremos un TypeError:

#gato[0] = "Michi" #ERROR: TypeError: 'tuple' object does not support item assignment
# A pesar de esto, podemos agregar elementos a las tuplas o hacer slicing.

gato = gato + ("4.1",)
print(gato) #Imprime: ('Miu', 5, 'persa', False, '4.1')

estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal
paises = {} #Diccionario vacío
paises["MEX"] = "México" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"


#JSON --> es un tipo de dato que se utiiliza
#paran almacenar  informacion en un formato de texto palano.
#Es muy utilizado en la web para intercambiar información
#entre el cliente y el servidor.

persona = {
    'nombre': 'Carmen',
    'edad': 31, 'altura': 1.71,
    'usa_lentes': False
}

persona['nombre'] = 'Valeria' #actualiza si el valor de la llave existe
persona["hobbies"] = ['jugar videojuegos', 'programación']
#incorporar nuevas llaves a persona.
#profesio, comida favorita, mascotas, pelicula_favortias.
persona['Profesion'] = 'Profesora'
persona['comida_favorita'] = 'tallarines'
persona['mascotas'] = 'perros'
persona['peliculas_favoritas'] = ['fornite la pelicula', 'una pelicula de minecraft']
print(persona)

