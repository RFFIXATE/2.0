import psutil
import platform
import subprocess
import time
import socket
import os

while True:
    os.system('clear')
    # Obtener información sobre el disco
    disk_usage = psutil.disk_usage('/')
    total_disco = disk_usage.total
    uso_disco = disk_usage.used
    disponibilidad_disco = disk_usage.free

    # Obtener información sobre la memoria
    memoria = psutil.virtual_memory()
    memoria_total = memoria.total
    memoria_usada = memoria.used
    memoria_disponible = memoria.available

    # Obtener información sobre la CPU
    porcentaje_cpu = psutil.cpu_percent()
    numero_cpu = psutil.cpu_count()

    # Obtener información sobre las interfaces de red y sus direcciones
    interfaces = psutil.net_if_addrs()

    # Imprimir las redes disponibles
    print("REDES DISPONIBLES:")
    print("_________________________________________________________________________")
    for interface_name, addresses in interfaces.items():
        print(f"Interface: {interface_name}")
        for address in addresses:
            if address.family == socket.AF_INET:
                print(f"   Dirección IP: {address.address}")
            elif address.family == socket.AF_INET6:
                print(f"   Dirección IPv6: {address.address}")
    print("__________________________________________________________________________")
    # Imprimir los resultados en pantalla
    print("RECURSOS DE HARDWARE DISPONIBLES:")
    print("___________________________________________________________________________")
    print(f"Disco: Total={total_disco}B, Usado={uso_disco}B, Libre={disponibilidad_disco}B")
    print("############################################################################")
    print(f"Memoria: Total={memoria_total}B, Usada={memoria_usada}B, Libre={memoria_disponible}B")
    print("############################################################################")
    print(f"CPU: Uso={porcentaje_cpu}%, Núcleos={numero_cpu}")
    print("############################################################################")

    # Esperar 10 segundos antes de volver a obtener la información
    time.sleep(10)