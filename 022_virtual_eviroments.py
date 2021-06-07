#  Ambiente Virtuales
# Sirve para crear sub espacios de python y 
# no contaminar nuestra version principal
# esto funciona al rededor de "pip"
mkdir _nombre_directorio
cd _nombre_directorio
# crear ambiente virtual
python -m venv env
# activar ambiente
cd env\Scripts
activate.bat
# desactivar ambiente
deactivate
