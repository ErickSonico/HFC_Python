import xml.etree.ElementTree as ET
import csv
from itertools import zip_longest  

ips_encendidas = []
ips_apagadas = []
ips_22 = []
ips_con_nombre = []
ips_honey = []

def host_status(xml, ips_encendidas, ips_apagadas):
    with open(xml, 'r') as archivo:
        root = ET.fromstring(archivo.read())
        for host in root.findall('host'):
            if host.find('status').get('state') == 'down':
                ips_apagadas.append(host.find('address').get('addr'))
            elif host.find('status').get('state') == 'up':
                ips_encendidas .append(host.find('address').get('addr'))

def host_22(xml, ips_22):
    with open(xml, 'r') as archivo:
        root = ET.fromstring(archivo.read())
        for host in root.findall('host'):
            for port in host.findall('.//port'):
                port_id = port.get('portid')
                port_status = port.find('state').get('state') == 'open'
                if port_id == '22' and port_status:
                    ips_22.append(host.find('address').get('addr'))

def host_con_nombre(xml, ips_con_nombre):
    with open(xml, 'r') as archivo:
        root = ET.fromstring(archivo.read())
        for host in root.findall('host'):
                if host.find('.//hostname') is not None:
                    ips_con_nombre.append(host.find('address').get('addr'))

def host_honey(xml, ips_honey):
    with open(xml, 'r') as archivo:
        root = ET.fromstring(archivo.read())
        for host in root.findall('host'):
            for port in host.findall('.//port'):
                service = port.find('service').get('product')
                name = port.find('service').get('name')
                if service is not None and 'honey' in service or 'honey' in name:
                    ips_honey.append(host.find('address').get('addr'))

def genera_csv(ips_encendidas, ips_apagadas, ips_22, ips_con_nombre, ips_honey):
    with open('ips.csv', 'w') as archivo:
        writer = csv.writer(archivo)
        filas = zip_longest(ips_encendidas, ips_apagadas, ips_22, ips_con_nombre, ips_honey, fillvalue=' ')
        writer.writerow(['Hosts encendidos', 'Hosts apagados', 'Hosts con puerto 22 abierto', 'Hosts con nombre', 'Hosts que son honeypot'])
        for fila in filas:
            writer.writerow(fila)

host_status('nmap.xml', ips_encendidas, ips_apagadas)
host_22('nmap.xml', ips_22)
host_con_nombre('nmap.xml', ips_con_nombre)
host_honey('nmap.xml', ips_honey)

genera_csv(ips_encendidas, ips_apagadas, ips_22, ips_con_nombre, ips_honey)