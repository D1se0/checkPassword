#!/bin/python3

import requests
import hashlib
import colorama
from colorama import Fore, Style

# Inicializar colorama para los colores de la terminal
colorama.init()

class CheckPasswordAPI:
    def __init__(self):
        self.api_url = 'https://api.pwnedpasswords.com/range/'

    def check_password(self, password):
        sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix, suffix = sha1_password[:5], sha1_password[5:]
        url = f"{self.api_url}{prefix}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            hashes = (line.split(':') for line in response.text.splitlines())
            for h, count in hashes:
                if h == suffix:
                    return int(count)
            return 0
        
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error al consultar API: {str(e)}")

class CheckPasswordCLI:
    def __init__(self):
        self.checker = CheckPasswordAPI()

    def run(self):
        self.print_logo()
        while True:
            password = input("\nIngrese la contraseña a verificar (o 'q' para salir): ")
            if password.lower() == 'q':
                break
            
            try:
                compromised_count = self.checker.check_password(password)
                if compromised_count > 0:
                    print(f"\n{Fore.RED}La contraseña '{password}' ha sido comprometida en {compromised_count} bases de datos conocidas.{Style.RESET_ALL}")
                    print(f"Se recomienda cambiar esta contraseña.")
                else:
                    print(f"\n{Fore.GREEN}La contraseña '{password}' no ha sido comprometida en bases de datos conocidas.{Style.RESET_ALL}")
                    print(f"¡La contraseña es segura!")
            except Exception as e:
                print(f"\n{Fore.YELLOW}Error durante la verificación: {str(e)}{Style.RESET_ALL}")

    def print_logo(self):
        logo = """
██████╗ ███████╗██████╗ ██╗   ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
██║  ██║█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
██║  ██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
██████╔╝███████╗██████╔╝ ╚████╔╝ ███████╗██║  ██║
╚═════╝ ╚══════╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
        """
        print(Fore.CYAN + logo + Style.RESET_ALL)

def main():
    app = CheckPasswordCLI()
    app.run()

if __name__ == "__main__":
    main()
