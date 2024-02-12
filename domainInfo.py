import socket
import dns.resolver
import geoip2.database

def getIP(domain):
    return socket.gethostbyname(domain.strip())

def getNS(domain):
    nsArr = []
    for x in dns.resolver.resolve(domain, 'NS'):
        nsArr.append(x.to_text())
    return nsArr

def getMX(domain):
    mxArr = []
    for x in dns.resolver.resolve(domain, 'NS'):
        mxArr.append(x.to_text())
    return mxArr

def getASN(ip):
    with geoip2.database.Reader('./GeoLite2-ASN.mmdb') as reader:
        return "AS"+str(reader.asn(ip).autonomous_system_number)

def getOrg(ip):
    with geoip2.database.Reader('./GeoLite2-ASN.mmdb') as reader:
        return reader.asn(ip).autonomous_system_organization

def getCountry(ip):
    with geoip2.database.Reader('./GeoLite2-Country.mmdb') as reader:
        return reader.country(ip).country.iso_code
    
def getDomainInfo(domain):
    obj = {
        "domain": "",
        "ip": "",
        "asn": "",
        "org": "",
        "country_code": "",
        "ns": [],
        "mx": []
    }

    

    return obj