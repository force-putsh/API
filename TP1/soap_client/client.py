from zeep import Client

wsdl_url = 'http://www.dneonline.com/calculator.asmx?wsdl'
client = Client(wsdl=wsdl_url)

# Exemple d’appel
result = client.service.Add(10, 5)
print("Addition Result:", result)

result = client.service.Multiply(4, 6)
print("Multiplication Result:", result)
