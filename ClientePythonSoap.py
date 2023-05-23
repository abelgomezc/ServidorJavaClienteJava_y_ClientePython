from zeep import Client

#Crear el cliente.

cliente = Client('http://localhost:28901/ServicioWebSOAP/WSOperaciones?WSDL')


#priner metodo
if cliente.service.Login("abelgomez","contrasegura"):
  print("Iniciando sesion......")

else:
    print("Datos incorectos.")

#segundo metodo 
if cliente.service.procesarPago(300,6000)>=0:
    print("pago realizado.")

else:
    print("No se realizao el Pago.")


    