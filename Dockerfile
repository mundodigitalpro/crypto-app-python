# Usamos una imagen base de Python oficial
FROM python:3.9-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos el archivo de requisitos (si lo tenemos)
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la aplicación al contenedor
COPY app_crypto_coincap.py .

# Comando para ejecutar la aplicación
CMD ["python", "app_crypto_coincap.py"]