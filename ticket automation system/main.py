import json
import requests
from utils.ticket_generator import create_ticket
from utils.validador import validar_no_vacio

def guardar_ticket(ticket):
    try:
        with open("tickets.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    data.append(ticket)

    with open("tickets.json", "w") as file:
        json.dump(data,file,indent=4)

def mostrar_tickets():
    with open ("tickets.json", "r") as file:
        data = json.load(file)

    print("\n Tickets: ")
    for i in data:
        print(f"{i['id']} - {i['problema']} ({i['prioridad']})")

def enviar_a_n8n(ticket):
    url = "https://juanlopez.app.n8n.cloud/webhook-test/7b1299f5-4145-4095-bf45-0ab326236df8"
    
    try:
        response = requests.post(url, json=ticket)
        print("Enviado a n8n: ",response.status_code)
    except Exception as e:
        print("Error enviando a n8n: ", e)

def main():
    while True:
        print("\n1- Crear ticket")
        print("2- Ver tickets")
        print("3- Salir")

        seleccion = input("Elegir opcion: ")
        match seleccion:
            case "1":
                while True:
                    nombre = input("Nombre: ")
                    if validar_no_vacio(nombre, "Nombre"):
                        break

                while True:
                    problema = input("Problema: ")
                    if validar_no_vacio(problema, "Problema"):
                        break
    
                while True:
                    opcion = input("Prioridad del ticket\n1-Alta\n2-Media\n3-Baja\nSeleccione una opcion: ")
                    match opcion:
                        case "1":
                            prioridad = "alta"
                            break
                        case "2":
                            prioridad = "media"
                            break
                        case "3":
                            prioridad = "baja"
                            break
                        case _:
                            print("Seleccione una opccion valida.")
                            continue

                ticket = create_ticket(nombre, problema, prioridad)
                guardar_ticket(ticket)
                enviar_a_n8n(ticket)

                print("\nTicket creado")
                print(ticket)
            case "2":
                mostrar_tickets()
            case "3":
                break
            case _:
                print("Seleccione una opccion valida.")
    
if __name__ == "__main__":
    main()