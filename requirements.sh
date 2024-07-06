#!/bin/bash

# Verificar que el script se ejecute como root
if [[ $(id -u) -ne 0 ]]; then
    echo "Este script debe ser ejecutado como root." >&2
    exit 1
fi

# Instalar dependencias
pip install colorama requests

# Copiar el script .py a /usr/bin sin la extensión .py
cp checkPassword.py /usr/bin/checkPassword
chmod +x /usr/bin/checkPassword

echo "Instalación completada. Ahora puedes ejecutar 'checkPassword' desde cualquier parte de la terminal."
