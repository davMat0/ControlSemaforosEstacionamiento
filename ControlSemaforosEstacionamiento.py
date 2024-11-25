import threading
import time
import random

semaforo = threading.Semaphore(3)

def accederEstacionamiento(idVehiculo):
    semaforo.acquire()
    print(f"Vehículo {idVehiculo} ha entrado al estacionamiento")
    time.sleep(random.uniform(1,3))
    print(f"Vehículo {idVehiculo} ha salido del estacionamiento")
    semaforo.release()

vehiculos = 10

hilos = []
for i in range(10):
    hilo = threading.Thread(target=accederEstacionamiento, args=(i,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()

