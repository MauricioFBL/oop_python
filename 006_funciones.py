##       FUNCIONES REPASO

# Funcion comun
def elevar_cubo(numero):
	return numero * numero * numero

print(elevar_cubo(5))
# # Funciones cómo objetos de primera-clase
# en Python las funciones son objetos de primera-clase, es decir, que pueden ser pasados y utilizados cómo argumentos
#  al igual que cualquier otro objeto (strings, enteros, flotantes, listas, etc.).

def presentarse(nombre):
	return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
	return f"¡Hey {nombre}, aprendamos Python!"

def consume_funciones(funcion_entrante, nombre):
	return funcion_entrante(nombre)

print(consume_funciones(presentarse,'mau'))
print(consume_funciones(estudiemos_juntos,'mau'))

# Funciones anidadas
# Al igual que los condicionales y bucles también puedes colocar funciones dentro de otra función.
def funcion_mayor():
	print("Esta es una función mayor y su mensaje de salida.")

	def librerias():
		print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

	def frameworks():
		print("Algunos frameworks de Python son: Django, Dash y Flask.")

	frameworks()
	librerias()
    
funcion_mayor()





