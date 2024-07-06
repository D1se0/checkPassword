# checkPassword

checkPassword es una herramienta de línea de comandos desarrollada en Python que te permite verificar si una contraseña ha sido comprometida en bases de datos conocidas de contraseñas filtradas. Utiliza la API de Pwned Passwords de Have I Been Pwned para realizar esta verificación de manera segura y eficiente.

## Funcionalidades

### Verificación de Contraseñas Comprometidas:

Ingresa una contraseña para verificar si ha aparecido en filtraciones conocidas.

Utiliza una técnica segura de hash para proteger la privacidad de la contraseña durante la verificación.

## Interfaz de Línea de Comandos (CLI):

Interacción amigable con el usuario a través de la terminal.

Muestra mensajes de advertencia si la contraseña está comprometida y recomendaciones para cambiarla.

## Seguridad y Privacidad:

La verificación se realiza sin enviar la contraseña completa a través de la red.

Solo se envía una porción del hash SHA-1 de la contraseña para buscar coincidencias en la base de datos de contraseñas comprometidas.

## Uso:

### Requisitos Previos

Asegúrate de tener instalado `Python3` en tu sistema. Además, las dependencias necesarias (`colorama` y `requests`) se instalan automáticamente ejecutando el script `requirements.sh`.

## Instalación:

Ejecuta el siguiente comando para instalar las dependencias y configurar el script para ejecutarse globalmente:

```bash
sudo ./requirements.sh
```

## Ejecución:

Para verificar una contraseña, simplemente ejecuta el script `checkPassword` seguido del comando:

```bash
python3 checkPassword.py
```

## Ejemplo de Uso:

```bash
python3 checkPassword.py
```
### less

```bash
██████╗ ███████╗██████╗ ██╗   ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
██║  ██║█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
██║  ██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
██████╔╝███████╗██████╔╝ ╚████╔╝ ███████╗██║  ██║
╚═════╝ ╚══════╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝

Ingrese la contraseña a verificar (o 'q' para salir): secreta123

La contraseña 'secreta123' no ha sido comprometida en bases de datos conocidas.
¡La contraseña es segura!
```

## Contribución:

Si encuentras algún problema o tienes alguna sugerencia de mejora, no dudes en abrir un issue o enviar un pull request. ¡Tu colaboración es bienvenida!

## Créditos:

Desarrollado por @d1se0 - (Link Perfil GitHub)[https://github.com/D1se0]

## Licencia:

Este proyecto está licenciado bajo la [Licencia XYZ]. Ver el archivo LICENSE para más detalles.
