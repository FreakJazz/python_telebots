import telebot

# Reemplaza este token con el tuyo
TOKEN_BOT = '7597701644:AAGIdJVqk7KoelPcvRXU2TupDEF6kUakYRo'

# Crea una instancia del bot
bot = telebot.TeleBot(TOKEN_BOT)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "¡Hola! Bienvenido, escribe 'paquetes' para ver los servicios disponibles.")

# Si el usuario escribe 'paquetes', se muestran las opciones
@bot.message_handler(func=lambda m: m.text.lower() == "paquetes")
def mostrar_paquetes(message):
    opciones_texto = (
        "Estos son los paquetes que tenemos:\n"
        "1. Manicure\n"
        "2. Corte de cabello\n"
        "3. Pedicure\n"
        "Escribe el número del paquete que deseas:"
    )
    bot.send_message(message.chat.id, opciones_texto)
    bot.register_next_step_handler(message, procesar_opcion)

# Procesar respuesta del usuario
def procesar_opcion(message):
    seleccion = message.text.strip()
    if seleccion == "1":
        respuesta = "Has seleccionado: Manicure 💅"
    elif seleccion == "2":
        respuesta = "Has seleccionado: Corte de cabello 💇"
    elif seleccion == "3":
        respuesta = "Has seleccionado: Pedicure 🦶"
    else:
        respuesta = "Opción no válida. Por favor escribe 1, 2 o 3."
    
    bot.send_message(message.chat.id, respuesta)

# Ejecutar el bot
if __name__ == '__main__':
    print("Está ejecutándose el bot...")
    bot.infinity_polling()
