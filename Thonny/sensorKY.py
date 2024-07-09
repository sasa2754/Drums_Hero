from machine import Pin
import urequests
import ujson
import network
import time

# Configura os pinos ADC
prato1 = Pin(13, Pin.IN)
prato2 = Pin(14, Pin.IN)
tambor1 = Pin(27, Pin.IN)
tambor2 = Pin(26, Pin.IN)
tambor3 = Pin(25, Pin.IN)
tambor4 = Pin(33, Pin.IN) 
# pedal = machine.ADC(machine.Pin(34))

musica1 = 252
musica2 = 219
musica3 = 122

#Credenciais do WIFI
nome = "Celofone da Sasá"
senha = "sasa12345"


# Endereço do firebase
FIREBASE_URL = "https://iiot-7276b-default-rtdb.firebaseio.com/"
SECRET_KEY = ""

def conectarWifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando no WiFi...")
        wlan.connect(nome, senha)
        while not wlan.isconnected():
            pass
    print("Wifi conectado... IP: {}".format(wlan.ifconfig()[0]))
    
conectarWifi()

def enviarFire(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + SECRET_KEY
    }
    url = FIREBASE_URL + "Sabrina.json"  # Coloque o seu nome

    response = urequests.put(url, data=ujson.dumps(data), headers=headers)
    print("Firebase Response:", response.text)
    response.close()
    
musica = 0

def pegarMusica():
#     Colocar pra pegar o nome dps q essa parte funcionar
    url = 'https://iiot-7276b-default-rtdb.firebaseio.com/.json'
    
    data = ujson.loads(urequests.get(url).content)['Sabrina']
#     print(f"Firebase Response get: {data}\n")
    
    if data['Musica'] == 1:
        musica = musica1
    elif data['Musica'] == 2:
        musica = musica2
    elif data['Musica'] == 3:
        musica = musica3
    else:
        print("Musica com valor incorreto")
        
    return musica

valorPrato1 = 0
valorPrato2 = 0
valorTambor1 = 0
valorTambor2 = 0
valorTambor3 = 0
valorTambor4 = 0

listaPrato1 = []
listaPrato2 = []
listaTambor1 = []
listaTambor2 = []
listaTambor3 = []
listaTambor4 = []

def getBatidas():
    
    prato1Value = prato1.read()
    prato2Value = prato2.read()
    tambor1Value = tambor1.read()
    tambor2Value = tambor2.read()
    tambor3Value = tambor3.read()
    tambor4Value = tambor4.read()

    if prato1Value == 0:
        print(f"Batida Prato 1: {prato1Value}")
        valorPrato1 = 1
        listaPrato1.append(valorPrato1)
    else:
        print(f"Batida Prato 1: {prato1Value}")
        valorPrato1 = 0
        listaPrato1.append(valorPrato1)
        
        
    if prato2Value == 0:
        print(f"Batida Prato 2: {prato2Value}")
        valorPrato2 = 1
        listaPrato2.append(valorPrato2)
    else:
        print(f"Batida Prato 2: {prato2Value}")
        valorPrato2 = 0
        listaPrato2.append(valorPrato2)
        
        
    if tambor1Value == 0:
        print(f"Batida tambor 1: {tambor1Value}")
        valorTambor1 = 1
        listaTambor1.append(valorTambor1)
    else:
        print(f"Batida tambor 1: {tambor1Value}")
        valorTambor1 = 0
        listaTambor1.append(valorTambor1)


    if tambor2Value == 0:
        print(f"Batida tambor 2: {tambor2Value}")
        valorTambor2 = 1
        listaTambor2.append(valorTambor2)
    else:
        print(f"Batida tambor 2: {tambor2Value}")
        valorTambor2 = 0
        listaTambor2.append(valorTambor2)
        
        
    if tambor3Value == 0:
        print(f"Batida tambor 3: {tambor3Value}")
        valorTambor3 = 1
        listaTambor3.append(valorTambor3)
    else:
        print(f"Batida tambor 3: {tambor3Value}")
        valorTambor3 = 0
        listaTambor3.append(valorTambor3)
        
        
    if tambor4Value == 0:
        print(f"Batida tambor 4: {tambor4Value}")
        valorTambor4 = 1
        listaTambor4.append(valorTambor4)
    else:
        print(f"Batida tambor 4: {tambor4Value}")
        valorTambor4 = 0
        listaTambor4.append(valorTambor4)
        
    time.sleep(0.5)
    
timeMusica = 0
musica = pegarMusica()

while timeMusica <= musica:
    getBatidas()
    timeMusica += 1
    
informacao = {
#     "Nome": nome,
    "Musica": musica,
    "Prato1": listaPrato1,
    "Prato2": listaPrato2,
    "Tambor1": listaTambor1,
    "Tambor2": listaTambor2,
    "Tambor3": listaTambor3,
    "Tambor4": listaTambor4
#     "Pedal": listaPedal
}

enviarFire(informacao)

