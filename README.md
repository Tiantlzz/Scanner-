
#  Escáner de Puertos Multihilo en Python

Un script de línea de comandos simple pero potente para descubrir puertos TCP abiertos en un host o dirección IP. Este proyecto fue creado con fines educativos para aprender sobre redes y ciberseguridad utilizando Python.



---
## ¿Qué hace el proyecto?

Esta herramienta realiza un escaneo de puertos en un objetivo específico para identificar qué servicios podrían estar ejecutándose. Utiliza múltiples hilos para realizar el escaneo de forma concurrente, lo que lo hace significativamente más rápido que un escaneo secuencial.

**Características Principales:**
* **Rápido y Eficiente:** Utiliza multihilo para escanear miles de puertos en segundos.
* **Flexible:** Permite al usuario especificar el objetivo y un rango de puertos personalizado a través de la línea de comandos.
* **Ligero y Seguro:** No requiere la instalación de ninguna librería de terceros, ya que utiliza únicamente la biblioteca estándar de Python.

---
## Tecnologías Utilizadas

Este proyecto se basa exclusivamente en la **biblioteca estándar de Python**, lo que garantiza su portabilidad y seguridad sin necesidad de dependencias externas.

* **`socket`**: La base de toda la comunicación de red. Se utilizó para intentar establecer conexiones TCP con los puertos del objetivo.
* **`threading` y `queue`**: Se usaron para implementar la concurrencia. `threading` permite ejecutar múltiples funciones de escaneo a la vez, y `queue` gestiona de forma segura la lista de puertos que cada hilo debe procesar. Esto es clave para la velocidad del escáner.
* **`argparse`**: Se eligió para crear una interfaz de línea de comandos (CLI) limpia y profesional. Permite al usuario pasar argumentos como el objetivo (`-t`) y los puertos (`-p`) de una manera intuitiva.
* **`time`**: Utilizado para medir el rendimiento del script, calculando el tiempo total que tarda en completarse el escaneo.

---
## Instalación y Uso

La mejor parte de este proyecto es que **no requiere instalación**. Solo necesitas tener Python 3 instalado en tu sistema.

**1. Clona o descarga el proyecto:**
Guarda el código en un archivo llamado `port_scanner_v2.py`.

**2. Abre una terminal:**
Navega hasta el directorio donde guardaste el archivo.

**3. Ejecuta el escáner:**
Usa el comando `python` o `python3` para ejecutar el script, especificando el objetivo con el flag `-t` o `--target`.

**Ejemplos de Comandos:**

* **Escanear los puertos por defecto (1-1024) en un dominio:**
    ```bash
    python port_scanner_v2.py -t google.com
    ```

* **Escanear un rango de puertos personalizado en una IP:**
    ```bash
    python port_scanner_v2.py -t 192.16X.X.X -p 20-1000
    ```

* **Obtener ayuda para ver todas las opciones:**
    ```bash
    python port_scanner_v2.py -h
    ```

---
## Advertencia Ética

Este script es una herramienta educativa. El escaneo de puertos en redes o sistemas para los que no tienes permiso explícito es ilegal y puede ser considerado como el primer paso de un ciberataque. Úsalo de manera responsable y solo en tus propios sistemas o en entornos donde tengas autorización.







------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------














#  Multi-Threaded Port Scanner in Python

A simple yet powerful command-line script to discover open TCP ports on a target host or IP address. This project was created for educational purposes to learn about networking and cybersecurity using Python.



---
## What does this project do?

This tool performs a port scan on a specific target to identify which services might be running. It uses multiple threads to perform the scan concurrently, making it significantly faster than a sequential scan.

**Key Features:**
* **Fast and Efficient:** Uses multi-threading to scan thousands of ports in seconds.
* **Flexible:** Allows the user to specify the target and a custom port range via the command line.
* **Lightweight and Secure:** Requires no installation of third-party libraries, as it only uses Python's standard library.

---
## Technologies Used

This project is built exclusively with Python's **standard library**, ensuring its portability and security without the need for external dependencies.

* **`socket`**: The foundation for all network communication. It was used to attempt TCP connections to the target's ports.
* **`threading` & `queue`**: Used to implement concurrency. `threading` allows multiple scan functions to run at once, and `queue` safely manages the list of ports for each thread to process. This is key to the scanner's speed.
* **`argparse`**: Chosen to create a clean and professional Command-Line Interface (CLI). It allows the user to pass arguments like the target (`-t`) and ports (`-p`) in an intuitive way.
* **`time`**: Used to measure the script's performance by calculating the total time it takes for the scan to complete.

---
## Installation and Usage

The best part of this project is that it **requires no installation**. You only need to have Python 3 installed on your system.

**1. Clone or download the project:**
Save the code in a file named `port_scanner_v2.py`.

**2. Open a terminal:**
Navigate to the directory where you saved the file.

**3. Run the scanner:**
Use the `python` or `python3` command to run the script, specifying the target with the `-t` or `--target` flag.

**Command Examples:**

* **Scan the default ports (1-1024) on a domain:**
    ```bash
    python port_scanner_v2.py -t google.com
    ```

* **Scan a custom port range on an IP address:**
    ```bash
    python port_scanner_v2.py -t 192.16X.X.X -p 20-1000
    ```

* **Get help to see all options:**
    ```bash
    python port_scanner_v2.py -h
    ```

---
## Ethical Warning

This script is an educational tool. Port scanning networks or systems for which you do not have explicit permission is illegal and can be considered the first step of a cyberattack. Use it responsibly and only on your own systems or in environments where you have authorization.
