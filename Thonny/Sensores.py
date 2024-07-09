import machine
import time
import urequests
import ujson
import network

# Configura os pinos ADC
prato1 = machine.ADC(machine.Pin(32))
prato2 = machine.ADC(machine.Pin(33))
tambor1 = machine.ADC(machine.Pin(34))
tambor2 = machine.ADC(machine.Pin(35))
tambor3 = machine.ADC(machine.Pin(36))
tambor4 = machine.ADC(machine.Pin(39))
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
        musica = musica3
        
    return musica

# Configura a atenuação para leitura completa de 0-3.3V
# try:
#     prato1.atten(machine.ADC.ATTN_11DB)
#     prato2.atten(machine.ADC.ATTN_11DB)
#     tambor1.atten(machine.ADC.ATTN_11DB)
#     tambor2.atten(machine.ADC.ATTN_11DB)
#     tambor3.atten(machine.ADC.ATTN_11DB)
#     tambor4.atten(machine.ADC.ATTN_11DB)
#     pedal.atten(machine.ADC.ATTN_11DB)
#     
# except ValueError as e:
#     print("Erro ao configurar atenuação:", e)

ultimoPrato1 = 4095
atualPrato1 = 0

ultimoPrato2 = 4095
atualPrato2 = 0

ultimoTambor1 = 4095
atualTambor1 = 0

ultimoTambor2 = 4095
atualTambor2 = 0

ultimoTambor3 = 4095
atualTambor3 = 0

ultimoTambor4 = 4095
atualTambor4 = 0

# ultimoPedal = 4095
# atualPedal = 0

valorPrato1 = 0
valorPrato2 = 0
valorTambor1 = 0
valorTambor2 = 0
valorTambor3 = 0
valorTambor4 = 0
# valorPedal = 0

listaPrato1 = []
listaPrato2 = []
listaTambor1 = []
listaTambor2 = []
listaTambor3 = []
listaTambor4 = []
# listaPedal = []


def pegarValores():
    global ultimoPrato1, valorPrato1, listaPrato1
#     global ultimoPrato2, valorPrato2, listaPrato2
#     global ultimoTambor1, valorTambor1, listaTambor1
#     global ultimoTambor2, valorTambor2, listaTambor2
#     global ultimoTambor3, valorTambor3, listaTambor3
#     global ultimoTambor4, valorTambor4, listaTambor4
    
    prato1Value = prato1.read() #Pegando o valor do sensor
#     prato2Value = prato2.read()
#     tambor1Value = tambor1.read()
#     tambor2Value = tambor2.read()
#     tambor3Value = tambor3.read()
#     tambor4Value = tambor4.read()
#     pedalValue = pedal.read()
    
    atualPrato1 = prato1Value - 150
#     atualPrato2 = prato2Value - 150
#     atualtambor1 = tambor1Value - 150
#     atualTambor2 = tambor2Value - 150
#     atualTambor3 = tambor3Value - 150
#     atualTambor4 = tambor4Value - 150
#     atualPedal = pedalValue - 150
    
    if atualPrato1 > ultimoPrato1:
        print(f"Batida Prato 1: {valorPrato1}")
        print(prato1.read())
        valorPrato1 = 1
        listaPrato1.append(valorPrato1)
    else:
        print(f"Sem batida Prato 1: {valorPrato1}")
        valorPrato1 = 0
        print(prato1.read())
        listaPrato1.append(valorPrato1)
        
    
#     if atualPrato2 > ultimoPrato2:
#         print(f"Batida Prato 2: {valorPrato2}")
#         valorPrato2 = 1
#         listaPrato2.append(valorPrato2)
#     else:
#         print(f"Sem batida Prato 2: {valorPrato2}")
#         valorPrato2 = 0
#         listaPrato2.append(valorPrato2)
#     
#     
#     if atualTambor1 > ultimoTambor1:
#         print(f"Batida Tambor 1: {valorTambor1}")
#         valorTambor1 = 1
#         listaTambor1.append(valorTambor1)
#     else:
#         print(f"Sem batida Tambor 1: {valorTambor1}")
#         valorTambor1 = 0
#         listaTambor1.append(valorTambor1)
#         
#         
#     if atualTambor2 > ultimoTambor2:
#         print(f"Batida Tambor 2: {valorTambor2}")
#         valorTambor2 = 1
#         listaTambor2.append(valorTambor2)
#     else:
#         print(f"Sem batida Tambor 2: {valorTambor2}")
#         valorTambor2 = 0
#         listaTambor2.append(valorTambor2)
#         
#         
#     if atualTambor3 > ultimoTambor3:
#         print(f"Batida Tambor 3: {valorTambor3}")
#         valorTambor3 = 1
#         listaTambor3.append(valorTambor3)
#     else:
#         print(f"Sem batida Tambor 3: {valorTambor3}")
#         valorTambor3 = 0
#         listaTambor3.append(valorTambor3)
#         
#         
#     if atualTambor4 > ultimoTambor4:
#         print(f"Batida Tambor 4: {valorTambor4}")
#         valorTambor4 = 1
#         listaTambor4.append(valorTambor4)
#     else:
#         print(f"Sem batida Tambor 4: {valorTambor4}")
#         valorTambor4 = 0
#         listaTambor4.append(valorTambor4)
#         
    print("\n")     
#     if atualPedal > ultimoPedal:
#         print(f"Batida Pedal: {sensorValue}")
#         valorPedal = 1
#         listaPedal.append(valorPedal)
#     else:
#         print(f"Sem batida Pedal: {sensorValue}")
#         valorPedal = 0
#         listaPedal.append(valorPedal)
        
        
    ultimoPrato1 = atualPrato1 + 150
#     ultimoPrato2 = atualPrato2 + 150
#     ultimoTambor1 = atualTambor1 + 150
#     ultimoTambor2 = atualTambor2 + 150
#     ultimoTambor3 = atualTambor3 + 150
#     ultimoTambor4 = atualTambor4 + 150
#     ultimoPedal = atualPedal + 150
    
    time.sleep(0.7)

time1 = 0
musica = pegarMusica()
# musica = musica3
while time1 <= musica:
    pegarValores()
    time1 += 1
    
informacao = {
#     "Nome": nome,
    "Musica": musica,
    "Prato1": listaPrato1,
#     "Prato2": listaPrato2,
#     "Tambor1": listaTambor1,
#     "Tambor2": listaTambor2,
#     "Tambor3": listaTambor3,
#     "Tambor4": listaTambor4,
#     "Pedal": listaPedal
}

enviarFire(informacao)
    