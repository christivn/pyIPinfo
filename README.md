# 🌐 DomainInfo

Este módulo permite obtener información detallada sobre un dominio específico en Internet.

### Descripción de los campos devueltos:
- **domain**: El nombre del dominio consultado.
- **ip**: La dirección IP asociada al dominio.
- **asn**: El número de Sistema Autónomo (AS) del dominio.
- **org**: La organización responsable del dominio.
- **country_code**: El código de país asociado con el dominio.
- **ns**: Lista de servidores de nombres (DNS) asociados con el dominio.
- **mx**: Lista de registros de intercambio de correo (Mail Exchange) para el dominio.

<br>

## Uso

Puedes usar el siguiente código para obtener información sobre un dominio:
``` python
from domainInfo import *

# Especifica el dominio del que deseas obtener información
domain = "google.com"

# Llama a la función para obtener la información del dominio
info = getDomainInfo(domain)

# Imprime la información del dominio
print(info)
```

<br>

## Ejemplo de respuesta

Al ejecutar el código anterior, recibirás una respuesta en formato JSON con la información del dominio:
``` json
{
 "domain": "google.com", 
 "ip": "172.217.17.14", 
 "asn": "AS15169", 
 "org": "GOOGLE", 
 "country_code": "US", 
 "ns": [
     "ns3.google.com.", 
     "ns1.google.com.", 
     "ns2.google.com.", 
     "ns4.google.com."
 ], 
 "mx": [
     "smtp.google.com."
 ]
}
```
