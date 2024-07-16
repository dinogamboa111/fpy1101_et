from random import *
import csv
import os

def limpiarpantalla():
    os.system("cls")

limpiarpantalla()

ciclo = 1
sueldorand = []
trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", 
                "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
sueldos = [["Nombres    ", "      Sueldo"]]
valordatos = []
reporte= [["Nombre", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"]]

def limpiarpantalla():
    os.system("cls")

def asignarsueldos():
    for trabajador in trabajadores:
        sueldo = randint(300000, 2500000)
        sueldos.append([trabajador, sueldo])
        valordatos.append(sueldo)
    print("Se han asignado los sueldos de forma correcta.")
    
def clasificarsueldos():
    sueldomenor = [["Nombres    ", "      Sueldo"]]
    sueldointer = [["Nombres    ", "      Sueldo"]]
    sueldomayor = [["Nombres    ", "      Sueldo"]]
    for fila in sueldos[1:]:
        trabajador, sueldo = fila
        if sueldo < 800000:
            sueldomenor.append([trabajador, sueldo])
        elif sueldo >= 800000 or sueldo <= 2000000:
            sueldointer.append([trabajador, sueldo])
        elif sueldo > 2000000:
            sueldomayor.append([trabajador, sueldo])
    
    cantsueldomenor = int(len(sueldomenor))
    print(f"Sueldos menores a $800.000\nTOTAL: {cantsueldomenor-1}")
    for i in sueldomenor:
        print(i)
    print("")
    cantsueldointer = int(len(sueldointer))
    print(f"Sueldos entre $800.000 y $2.000.000\nTOTAL: {cantsueldointer-1}")
    for f in sueldointer:
        print(f)
    print("")
    cantsueldomayor = int(len(sueldomayor))   
    print(f"Sueldos superiores a $2.000.000\nTOTAL: {cantsueldomayor-1}")
    print("")
    totalsueldo = sum(valordatos)
    print(f"TOTAL SUELDOS: ${totalsueldo}")
    

def mediageo(data):
    producto = 1
    for valor in data:
        producto *= valor
    return producto ** (1-len(data))
    

def verestadisticas():
    totalsueldo = sum(valordatos)
    sueldomasalto = max(valordatos)
    sueldomasbajo= min(valordatos)
    sueldopromedio= totalsueldo / int(len(valordatos))

    print(f"El sueldo mas alto en  nuestra plantilla es de: ${sueldomasalto}")
    print(f"El sueldo mas bajo en nuestra plantilla es de: ${sueldomasbajo}")
    print(f"El Promedio de nuestros sueldos es de : ${sueldopromedio}")
    print(f"Nuestra media geometica es de :{mediageo(valordatos):>4f}")
    print("")
  
def reportesueldos():
    for fila in sueldos[1:]:
        nombre, sueldobase = fila
        descsalud = round(sueldobase*0.07)
        descafp = round(sueldobase*0.12)
        sueldoliq = sueldobase-descsalud-descafp
        reporte.append([nombre, sueldobase, descsalud, descafp, sueldoliq])
    for fila1 in reporte:
        print(f"{fila1[0]:<18} {fila1[1]:<13} {fila1[2]:<13} {fila1[3]:<13} {fila1[4]:<13}")
    print("")
    with open ( 'reporte_sueldos.csv','w',newline='' ) as report_csv:
        escritor_csv = csv.writer(report_csv)
        escritor_csv.writerows(reporte)
    print("Se ha guardado el reporte en un archivo reporte_sueldos.csv ")
    print("")

def salir():
    print("Finalizando Programa...\nDesarrollado por Dino Gamboa\nRUT 19.173.228-6")
    print("")
    
while ciclo == 1:
    try:
        menu = int(input("""Menu de seleccion:
                        1. Asignar sueldos aleatorios.
                        2. Clasificar sueldos.
                        3. Ver estadisticas.
                        4. Reporte de sueldos.
                        5. Salir del programa.
                        indique su seleccion: """))
        print("")
    except ValueError:
        print("Debe indicar un valor numerico entre 1 y 5.")
        continue
    if  menu == 1:
        asignarsueldos()
    elif menu == 2:
        clasificarsueldos()
    elif menu == 3:
        verestadisticas() 
    elif menu == 4:
        reportesueldos()  
    elif menu == 5:
        salir()
        break
    else:
        print("Debe indicar un valor numerico entre 1 y 5.")