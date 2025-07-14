from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes,
    filters, ConversationHandler
)
from mailjet_rest import Client
import os
import requests
import re
import sqlite3
from datetime import datetime
from dotenv import load_dotenv, find_dotenv


dotenv_path = find_dotenv()
if dotenv_path == "":
    print("❌ No se encontró el archivo .env")
else:
    print(f"✔ Archivo .env cargado desde: {dotenv_path}")

load_dotenv(dotenv_path)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
print(f"BOT_TOKEN = {BOT_TOKEN!r}")
MAILJET_API_KEY = os.getenv("MAILJET_API_KEY")
MAILJET_SECRET_KEY = os.getenv("MAILJET_SECRET_KEY")
MAILJET_URL = os.getenv("MAILJET_URL")
MAILJET_FROM_NAME = os.getenv("MAILJET_FROM_NAME")
EMAIL_FROM = os.getenv("EMAIL_FROM")

MENU, DATOS, AUTORIZACION, CONFIRMAR = range(4)

SERVICIOS = {
    "1. Branding": 500,
    "2. Desarrollo Web": 1000,
    "3. Marketing Digital": 800,
    "4. Fotografía y Video": 700,
    "5. Diseño Gráfico": 600
}

conn = sqlite3.connect("clientes_diisign.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    username TEXT,
    servicio TEXT,
    datos TEXT,
    fecha TEXT
)
""")
conn.commit()

def guardar_cliente(update: Update, servicio="", datos=""):
    user = update.effective_user
    timestamp = datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO clientes (user_id, username, servicio, datos, fecha)
        VALUES (?, ?, ?, ?, ?)
    """, (user.id, user.username or "Sin username", servicio, datos, timestamp))
    conn.commit()

def extraer_email(texto):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', texto)
    return match.group(0) if match else None

def enviar_mailjet(destinatario, asunto, contenido):
    data = {
        "Messages": [
            {
                "From": {
                    "Email": EMAIL_FROM,
                    "Name": MAILJET_FROM_NAME
                },
                "To": [
                    {
                        "Email": destinatario,
                        "Name": "Cliente"
                    }
                ],
                "Subject": asunto,
                "TextPart": contenido
            }
        ]
    }
    try:
        response = requests.post(
            MAILJET_URL,
            json=data,
            auth=(MAILJET_API_KEY, MAILJET_SECRET_KEY)
        )
        print(f"📤 Estado del envío: {response.status_code}")
        print(f"📨 Respuesta Mailjet: {response.text}")

        if response.status_code != 200:
            print("❌ Algo falló al enviar el correo. Revisa la respuesta de Mailjet.")

        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error crítico al enviar correo: {e}")
        return False

# Conversaciones

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[s] for s in SERVICIOS.keys()]
    await update.message.reply_text(
        "🙌 Hola, soy el bot de *Diisign Studio*.\n\n¿En qué servicio estás interesado?",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True),
        parse_mode="Markdown"
    )
    return MENU

async def seleccionar_servicio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    servicio = update.message.text
    if servicio not in SERVICIOS:
        await update.message.reply_text("❌ Opción inválida. Usa el menú.")
        return MENU
    context.user_data["servicio"] = servicio
    await update.message.reply_text("📝 Por favor escribe:\nNombre - Correo - Descripción del proyecto")
    return DATOS

async def recibir_datos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    email = extraer_email(texto)
    if not email:
        await update.message.reply_text("❌ El correo no es válido. Intenta de nuevo.")
        return DATOS
    context.user_data["datos"] = texto
    keyboard = [["✅ Sí", "❌ No"]]
    await update.message.reply_text("¿Autorizas el uso de tus datos para contactarte?", 
                                    reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True))
    return AUTORIZACION

async def autorizacion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respuesta = update.message.text.lower()
    if "sí" in respuesta or "si" in respuesta or "✅" in respuesta:
        servicio = context.user_data["servicio"]
        precio = SERVICIOS[servicio]
        keyboard = [["✅ Confirmar", "❌ Cancelar"]]
        await update.message.reply_text(
            f"✅ Servicio: *{servicio}*\n💵 Precio: *${precio}*\n\n¿Confirmas tu pedido?",
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True),
            parse_mode="Markdown"
        )
        return CONFIRMAR
    else:
        await update.message.reply_text("🚫 No podemos continuar. Escribe /start para comenzar de nuevo.")
        return ConversationHandler.END

async def confirmar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    if "confirmar" in texto or "✅" in texto:
        servicio = context.user_data["servicio"]
        datos = context.user_data["datos"]
        email = extraer_email(datos)
        guardar_cliente(update, servicio, datos)
        enviado = enviar_mailjet(email, "Confirmación de pedido Diisign Studio", f"Gracias por solicitar {servicio}.\n\nDatos: {datos}")
        if enviado:
            await update.message.reply_text("✅ Pedido confirmado. ¡Revisa tu correo!")
        else:
            await update.message.reply_text("⚠️ El correo no se pudo enviar, pero tu pedido fue registrado.")
    else:
        await update.message.reply_text("❌ Pedido cancelado.")
    return ConversationHandler.END

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, seleccionar_servicio)],
            DATOS: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_datos)],
            AUTORIZACION: [MessageHandler(filters.TEXT & ~filters.COMMAND, autorizacion)],
            CONFIRMAR: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirmar)],
        },
        fallbacks=[]
    )

    app.add_handler(conv_handler)
    print("🚀 Bot de Diisign Studio en ejecución...")
    app.run_polling()

def revisar_base_de_datos():
    print("\n📦 Datos almacenados en la base de datos:")
    for row in cursor.execute("SELECT * FROM clientes"):
        print(row)


if __name__ == "__main__":
    main()
    revisar_base_de_datos()