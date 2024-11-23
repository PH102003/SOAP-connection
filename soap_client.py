from zeep import Client

client = Client('http://172.17.29.78:8080/?wsdl') 

#pega a funcao 'msg' feita no server soap  

response = client.service.msg("oi")
print(f"Response from server: {response}")
