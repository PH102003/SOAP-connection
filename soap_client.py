from zeep import Client

client = Client('http://192.168.56.1:8080/?wsdl')  # ip do eth0  no mininet
response = client.service.add(5, 3)
print(f"Resultado da soma: {response}")
