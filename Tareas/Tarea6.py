#!/usr/bin/python

import xml.etree.ElementTree as ET
import datetime
import hashlib



def obten_hora_inicio(xml):
    with open(xml,'r') as archivo:
        root = ET.fromstring(archivo.read())
        hora_inicio = datetime.datetime.fromtimestamp(int(root.get('start'))).time()
        return hora_inicio

def obten_hashes(xml):
    with open(xml, 'rb') as archivo:
        data = archivo.read()
        md5 = hashlib.md5(data).hexdigest()
        sha1 = hashlib.sha1(data).hexdigest()
        return (md5, sha1)
        

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
            if host.find('.//hostname') is not None:
                host_con_nombre += 1
            
    return [str(elem) for elem in [hosts_encendidos, host_apagados, port22, port53, port80, port443, host_con_nombre]]

def servidores_http(xml):
    apache = 0
    honey = 0
    nginx = 0
    otros = 0
    with open(xml, 'r') as archivo:
        root = ET.fromstring(archivo.read())
        for port in root.findall('.//port'):
            if port.get('portid') == '80':
                service = port.find('service').get('product')
                name = port.find('service').get('name')
                if service is not None and 'Apache' in service:
                    apache += 1
                if service is not None and 'honey' in service or 'honey' in name:
                    honey += 1
                if service is not None and 'nginx' in service:
                    nginx += 1
                else: 
                    otros += 1

    return [str(elem) for elem in [apache, honey, nginx, otros]]

def reporte_archivo(xml):
    with open('reporte.txt','w') as reporte:
        reporte.write('Hora de ejecucion: ' + str(obten_hora_inicio(xml)) + '\n')
        print('Hora de inicio: ' + str(obten_hora_inicio(xml)) + '\n')
        reporte.write('MD5: ' + obten_hashes(xml)[0] +'\nSHA1: ' + obten_hashes(xml)[1] + '\n')
        print('MD5: ' + obten_hashes(xml)[0] +'\nSHA1: ' + obten_hashes(xml)[1] + '\n')
        reporte.write('Hosts encendidos: ' + obten_hosts(xml)[0] + '\n')
        print('Hosts encendidos: ' + obten_hosts(xml)[0] + '\n')
        reporte.write('Hosts apagados: ' + obten_hosts(xml)[1] + '\n')
        print('Hosts apagados: ' + obten_hosts(xml)[1] + '\n')
        reporte.write('Puerto 22: ' + obten_hosts(xml)[2] + '\n')
        print('Puerto 22: ' + obten_hosts(xml)[2] + '\n')
        reporte.write('Puerto 53: ' + obten_hosts(xml)[3] + '\n')
        print('Puerto 53: ' + obten_hosts(xml)[3] + '\n')
        reporte.write('Puerto 80: ' + obten_hosts(xml)[4] + '\n')
        print('Puerto 80: ' + obten_hosts(xml)[4] + '\n')
        reporte.write('Puerto 443: ' + obten_hosts(xml)[5] + '\n')
        print('Puerto 443: ' + obten_hosts(xml)[5] + '\n')
        reporte.write('Hosts con nombre: ' + obten_hosts(xml)[6] + '\n')
        print('Hosts con nombre: ' + obten_hosts(xml)[6] + '\n')
        reporte.write('Apache: ' + servidores_http(xml)[0] + '\n')
        print('Apache: ' + servidores_http(xml)[0] + '\n')
        reporte.write('Honey: ' + servidores_http(xml)[1] + '\n')
        print('Honey: ' + servidores_http(xml)[1] + '\n')
        reporte.write('Nginx: ' + servidores_http(xml)[2] + '\n')
        print('Nginx: ' + servidores_http(xml)[2] + '\n')
        reporte.write('Otros: ' + servidores_http(xml)[3] + '\n')
        print('Otros: ' + servidores_http(xml)[3] + '\n')


reporte_archivo('nmap.xml')