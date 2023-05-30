# pasos para ser probado en AWS cloud
# en amazon AWS sudo yum install python3-pip -y
# verificar version python3 --version
# pip3 --version
# sudo yum install git -y
#considerando que nosotros utilizamos la máquian virtual en aws nuestra ruta es /var/log/audit/audit.log en caso de utilizar la máquina de clases es /var/log/secure

import subprocess
import datetime

# Obtener la fecha y hora actual
ahora = datetime.datetime.now()

# Calcular la última hora cerrada
ultima_hora_cerrada = ahora.replace(minute=0, second=0, microsecond=0) - datetime.timedelta(hours=1)

# Obtener la fecha y hora de inicio y finalización del rango
if ultima_hora_cerrada.hour == 0:  # Si la última hora es medianoche
    hora_inicio = ultima_hora_cerrada.replace(hour=23)
    hora_termino = ultima_hora_cerrada
else:
    hora_inicio = ultima_hora_cerrada.replace(hour=ultima_hora_cerrada.hour - 1)
    hora_termino = ultima_hora_cerrada

# Formatear las fechas y horas como cadenas
hora_inicio_str = hora_inicio.strftime("%b %d %H")
hora_termino_str = hora_termino.strftime("%b %d %H")

# Construir el comando grep para filtrar el archivo de registro
busqueda = f"grep 'authentication' /var/log/audit/audit.log | grep '{hora_inicio_str}\|{hora_termino_str}'"

try:
    # Ejecutar el comando grep y contar las líneas de salida
    salida = subprocess.check_output(busqueda, shell=True)
    intentos_fallidos = len(salida.decode().split('\n')) - 1
except subprocess.CalledProcessError:
    # Si no hay coincidencias, establecer la cantidad de intentos fallidos en 0
    intentos_fallidos = 0

# Mostrar el resultado
print(f"Cantidad de intentos fallidos de inicio de sesión en el rango {hora_inicio_str}:00 - {hora_termino_str}:00: {intentos_fallidos}")