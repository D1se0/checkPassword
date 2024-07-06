# checkPassword

<p align="center">
  <img src="https://github.com/D1se0/checkPassword/assets/164921056/6c3d5009-0726-42c3-ac5c-bd85efcd04b0" alt="Directorybrute" width="400">
</p>

`checkPassword` is a command line tool developed in Python that allows you to check if a password has been compromised against known databases of leaked passwords. Use Have I Been Pwned's Pwned Passwords API to perform this verification safely and efficiently.

## Features

### Verification of Compromised Passwords:

Enter a password to check if it has appeared in known leaks.

It uses a secure hashing technique to protect password privacy during verification.

## Command Line Interface (CLI):

Friendly interaction with the user through the terminal.

Displays warning messages if the password is compromised and recommendations to change it.

## Security and Privacy:

Verification is performed without sending the full password over the network.

Only a portion of the SHA-1 hash of the password is sent to match the compromised password database.

## Use:

### Previous requirements

Make sure you have `Python3` installed on your system. Additionally, the necessary dependencies (`colorama` and `requests`) are installed automatically by running the `requirements.sh` script.

## Install:

Run the following command to install the dependencies and configure the script to run globally:

```bash
sudo ./requirements.sh
```

## Execution:

To verify a password, simply run the `checkPassword` script followed by the command:

```bash
python3 checkPassword.py
```

## Example of Use:

```bash
python3 checkPassword.py
```
### Info:

```bash
██████╗ ███████╗██████╗ ██╗   ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
██║  ██║█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
██║  ██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
██████╔╝███████╗██████╔╝ ╚████╔╝ ███████╗██║  ██║
╚═════╝ ╚══════╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝

Enter the password to verify (or 'q' to exit): secret123

The password 'secret123' has not been compromised in known databases.
The password is secure!
```

## Contribution:

If you encounter any problems or have any suggestions for improvement, don't hesitate to open an issue or submit a pull request. Your collaboration is welcome!

## Credits:

Developed by `@d1se0` - [GitHub Profile Link](https://github.com/D1se0)

## License:

This project is licensed under the [XYZ License]. See the LICENSE file for more details.
