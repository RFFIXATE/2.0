# pasos para ser probado en AWS cloud
# en amazon AWS sudo yum install python3-pip -y
# verificar version python3 --version
# pip3 --version
# sudo yum install git -y
#considerando que nosotros utilizamos la máquian virtual en aws nuestra ruta es /var/log/audit/audit.log en caso de utilizar la máquina de clases es /var/log/secure

import os
import datetime

# Obtener la hora actual
ahora = datetime.datetime.now()

# Obtener la hora de inicio de la última hora cerrada
ultima_hora_cerrada = ahora - datetime.timedelta(hours=1)
hora_inicio = ultima_hora_cerrada.replace(minute=0, second=0, microsecond=0)

# Obtener la hora de fin del intervalo (hora actual redondeada hacia abajo)
hora_termino = ahora.replace(minute=0, second=0, microsecond=0)

# Manejar el cambio de día
dia_actual = ultima_hora_cerrada.strftime('%b %d') + ' - ' + hora_termino.strftime('%b %d')

# Abrir el archivo de registro
with open('/var/log/audit/audit.log', 'r') as archivo:
    # Inicializar contador de intentos fallidos
    contador_intentos_fallidos = 0
    
    # Leer cada línea del archivo
    for linea in archivo:
        # Buscar las líneas que contienen "authentication" y están dentro del rango de tiempo
        if 'authentication' in linea and dia_actual in linea:
            timestamp = linea.split()[1]
            # Obtener la hora de la línea en formato 'HH:MM:SS'
            hora = datetime.datetime.strptime(timestamp, '%H:%M:%S').time()
            # Verificar si la hora está dentro del rango deseado
            if hora_inicio.time() <= hora <= hora_termino.time():
                # Incrementar el contador de intentos fallidos
                contador_intentos_fallidos += 1

# Mostrar el resultado sin segundos
print(f"Cantidad de intentos fallidos de inicio de sesión en el rango {dia_actual} {hora_inicio.strftime('%H:%M')} - {hora_termino.strftime('%H:%M')}: {contador_intentos_fallidos}")
