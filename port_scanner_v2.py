import socket
import argparse
import threading
from queue import Queue
import time
NUMBER_OF_THREADS = 200
queue = Queue()
open_ports = []
print_lock = threading.Lock()
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  
        s.connect((target_ip, port))
    except (socket.timeout, ConnectionRefusedError):
        pass
    else:
        with print_lock:
            print(f"Puerto {port}: Abierto ")
            open_ports.append(port)
    finally:
        s.close()
def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()
def main(target, port_range):
    global target_ip
    try:
        target_ip = socket.gethostbyname(target)
        print(f"[*] Escaneando:{target_ip}")
    except socket.gaierror:
        print("[!] Error: Nombre de host no pudo ser resuelto.")
        return
    for port in range(port_range[0], port_range[1] + 1):
        queue.put(port)
    for _ in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target=worker)
        thread.daemon = True  
        thread.start()
    start_time = time.time()
    queue.join()
    end_time = time.time()
    print(f"\n[*] Escaneo completado en {end_time - start_time:.2f} segundos.")
    if open_ports:
        print(f"[*] Puertos abiertos encontrados:{sorted(open_ports)}")
    else:
        print("[*] No se encontraron puertos abiertos en el rango especificado.")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Escáner de puertos multihilo rápido y simple.")
    parser.add_argument("-t", "--target", required=True, help="El host o la dirección IP a escanear.")
    parser.add_argument("-p", "--ports", default="1-1024", help="Rango de puertos a escanear (ej. 1-1024, 80-100).")
    args = parser.parse_args()
    try:
        start_port, end_port = map(int, args.ports.split('-'))
        port_range = (start_port, end_port)
    except ValueError:
        print("[!] Formato de puerto inválido.)
    else:
        main(args.target, port_range)
