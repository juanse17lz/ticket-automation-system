# IT Ticket Automation System

## 📌 Descripción
Sistema de gestión de incidencias que permite registrar, organizar y automatizar tickets de soporte técnico.
En el sistema se pueden crear tickets y ver la lista de tickets ya creados.
Los tickets se generan con un id unico, nombre de problema, descriocion del problema, prioridad y fecha y hora.
Una vez creados los tickets se guardan en un archivo.json y ademas el sistema esta conectado a un workflow n8n que guarda los tickets en un GoogleSheets.
En el caso de los tickets de prioridad alta, el workflow ademas envia un mail para notificar la creacion del ticket de prioriodad alta.

## ⚙️ Tecnologías
- Python
- JSON
- n8n
- Requests
- GoogleSheets
- Gmail

## 🚀 Funcionalidades
- Creación de tickets
- Generación de ID único
- Registro en archivo
- Visualización de tickets
- Automatización vía webhook
- Actualizacion automatica en GoogleSheets
- Envio automatico de mail

## ▶️ Cómo usar
1. Ejecutar main.py
2. Crear ticket
3. Ver tickets

## 💡 Objetivo
Automatizar la creacion, visualizacion y notificacion de tickets de soporte tecnico.
