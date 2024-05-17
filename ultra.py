import RPi.GPIO as GPIO
import time

# Definir los pines GPIO
GPIO_TRIGGER = 23
GPIO_ECHO = 24

# Configurar los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def medir_distancia():
    # Enviar una señal de pulso al pin Trig
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)  # Pulso de 10us
    GPIO.output(GPIO_TRIGGER, False)

    # Medir el tiempo de ida y vuelta del pulso
    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()

    # Calcular la duración del pulso
    tiempo_transito = stop_time - start_time

    # Calcular la distancia (velocidad del sonido = 34300 cm/s)
    distancia = (tiempo_transito * 34300) / 2

    return distancia

try:
    while True:
        dist = medir_distancia()
        print("Distancia medida: {:.2f} cm".format(dist))
        time.sleep(1)

except KeyboardInterrupt:
    print("Medición interrumpida por el usuario")

finally:
    GPIO.cleanup()
