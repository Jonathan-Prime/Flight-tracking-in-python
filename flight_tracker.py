from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# URL del vuelo
url = "URL DEL VUELO GOOGLE FLIGHT"

# Umbral de precio (por debajo de este precio se enviará una alerta)
price_threshold = 280000  # 250,000 COP

# Configurar el navegador para Selenium
options = Options()
options.headless = True  # Ejecutar en segundo plano
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Función para obtener el precio de la página
def get_price():
    driver.get(url)
    time.sleep(5)  # Esperar a que la página cargue

    try:
        # Busca el precio del vuelo en el DOM de la página
        price_element = driver.find_element(By.XPATH, "//span[@class='hXU5Ud']")
        price_text = price_element.text
        price = int(price_text.replace("COP", "").replace(",", "").strip())
        return price
    except Exception as e:
        print(f"Error al obtener el precio: {e}")
        return None

# Función para enviar un correo electrónico
def send_email(price):
    sender_email = "CORREO_PROVIDER"  # Cambia con tu email de Titan
    password = "PASSWORD_PROVIDER"  # Cambia con tu contraseña de Titan

    receiver_email = "EMAIL_PERSONAL"  # Cambia con el destinatario
   
    
    # Configurar el correo
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Alerta de precio de vuelo"
    
    body = f"¡El precio del vuelo ha bajado a {price} COP!"
    message.attach(MIMEText(body, "plain"))
    
    try:
        # Enviar el correo usando SMTP
        with smtplib.SMTP_SSL("SMTP_SSL", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# Función principal para verificar el precio
def check_price():
    price = get_price()
    if price is not None:
        print(f"Precio actual: {price} COP")
        if price <= price_threshold:
            send_email(price)
            print("Precio bajo el umbral. Deteniendo el script.")
            driver.quit()  # Cierra el navegador
            exit()  # Detiene el script
        else:
            print(f"El precio sigue siendo alto: {price} COP")
    else:
        print("No se pudo obtener el precio.")

# Ejecutar el script de forma continua
if __name__ == "__main__":
    while True:
        check_price()
        time.sleep(30)  # Verificar el precio cada 30 segundos
