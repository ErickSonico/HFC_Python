#!/usr/bin/python

import xml.etree.ElementTree as ET
import datetime

def obten_hora_inicio(xml):
    with open(xml,'r') as archivo:
        root = ET.fromstring(archivo.read())
        hora_inicio = datetime.datetime.fromtimestamp(int(root.get('start'))).time()
        return hora_inicio

def obten_md5(xml):
    with open(xml, 'r') as archivo:
        root = ET.fromstring(archivo.read())
        md5 = root.get
        pass

def obten_hosts(xml):
    hosts_encendidos = host_apagados = 0
    port22 = port53 = port80 = port443 = 0
    host_con_nombre = 0

    with open(xml, 'r') as archivo:
        root = ET.fromstring(archivo.read())

        for host in root.findall('host'):
            if host.find('status').get('state') == 'up':
                hosts_encendidos += 1
            else:
                host_apagados += 1

        for port in root.findall('.//port'):
            port_id = port.get('portid')
            port_status = port.find('state').get('state') == 'open'

            if port_id == '22' and port_status:
                port22 += 1
            elif port_id == '53' and port_status:
                port53 += 1
            elif port_id == '80' and port_status:
                port80 += 1
            elif port_id == '443' and port_status: 
                port443 += 1

        for host in root.findall('host'):
            nombre_de_host = host.find('hostnames')
            if nombre_de_host is not None:
                host_con_nombre += 1
            
    return [hosts_encendidos, host_apagados, port22, port53, port80, port443, host_con_nombre]





#print(obten_hora_inicio('nmap.xml'))
print(obten_hosts('nmap.xml'))