from threading import Thread
import time

def carro1(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} Km: {}'.format(piloto, trajeto))
def carro2(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} Km: {}'.format(piloto, trajeto))
#carro1(10)
#carro2(20)

t_carro1 = Thread(target=carro1, args=[1, 'Python'])
t_carro2 = Thread(target=carro2, args=[1.5, 'C'])

t_carro1.start()
t_carro2.start()