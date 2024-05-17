import RPi.GPIO as GPIO
import time

# Definir el pin GPIO
FLOW_SENSOR_PIN = 18

# Configurar el pin GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Inicializar variables
global contador_pulsos
contador_pulsos = 0

# Definir la función de callback
def contar_pulsos(channel):
    global contador_pulsos
    contador_pulsos += 1

# Configurar la interrupción
GPIO.add_event_detect(FLOW_SENSOR_PIN, GPIO.FALLING, callback=contar_pulsos)

# Parámetros del sensor
factor_calibracion = 7.5  # Número de pulsos por litro

try:
    while True:
        inicio_tiempo = time.time()
        contador_pulsos = 0
        time.sleep(1)
        duracion_tiempo = time.time() - inicio_tiempo

        # Calcular el flujo
        flujo_litros_por_minuto = (contador_pulsos / factor_calibracion) / (duracion_tiempo / 60)
        print("Flujo: {:.2f} L/min".format(flujo_litros_por_minuto))

except KeyboardInterrupt:
    print("Medición interrumpida por el usuario")

finally:
    GPIO.cleanup()
