
# 🛫 Flight Price Tracker

Este proyecto es un script en Python que utiliza Selenium para automatizar la verificación del precio de un vuelo en Google Flights. Si el precio del vuelo está por debajo de un umbral definido, el script envía una alerta por correo electrónico.

---

## 📋 Prerrequisitos

Antes de ejecutar este script, asegúrate de tener lo siguiente instalado:

1. **Python 3.7 o superior**: Puedes descargarlo desde [python.org](https://www.python.org/).
2. **Google Chrome**: El script requiere el navegador Chrome para funcionar.
3. **Pip**: El gestor de paquetes de Python. Normalmente se incluye con Python.
4. **ChromeDriver**: Se administrará automáticamente con `webdriver-manager`.

---

## 📦 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Jonathan-Prime/flight-price-tracker.git
   cd flight-price-tracker
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

4. Actualiza la variable `url` en el script con el enlace del vuelo en Google Flights.

---

## 🔧 Configuración

- **Archivo `requirements.txt`:** Contiene todas las dependencias del proyecto.
- **Umbral de precio:** Cambia la variable `price_threshold` en el script para establecer el límite de alerta.

---

## 🚀 Uso

1. Ejecuta el script:
   ```bash
   python flight_tracker.py
   ```

2. El script verificará el precio cada 30 segundos y enviará una alerta por correo si el precio es menor o igual al umbral configurado.

---

## 🛠 Tecnologías utilizadas

- **Python**
- **Selenium**: Para automatizar la navegación web.
- **webdriver-manager**: Para gestionar ChromeDriver automáticamente.
- **smtplib**: Para el envío de correos electrónicos.

---

## 📌 Notas importantes

1. El script utiliza una conexión SSL para enviar correos. Asegúrate de que tu proveedor de correo permita el acceso SMTP.

---
