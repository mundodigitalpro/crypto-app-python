# Aplicación de Información de Criptomonedas

Esta es una aplicación de línea de comandos simple escrita en Python que proporciona información actualizada sobre criptomonedas utilizando la API de CoinCap.

## Características

- Obtener información detallada de una criptomoneda específica
- Ver las top 10 criptomonedas por capitalización de mercado
- Interfaz de línea de comandos fácil de usar

## Requisitos

- Python 3.7+
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/crypto-app-python.git
   cd crypto-app-python
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar la aplicación, usa el siguiente comando en la terminal:

```
python app_crypto_coincap.py
```

Sigue las instrucciones en pantalla para:
1. Ver información detallada de una criptomoneda específica
2. Ver las top 10 criptomonedas
3. Salir de la aplicación

## Estructura del Proyecto

- `app_crypto_coincap.py`: El script principal de la aplicación
- `requirements.txt`: Lista de dependencias del proyecto
- `Dockerfile`: Configuración para crear un contenedor Docker de la aplicación

## Dockerización

Para ejecutar la aplicación en un contenedor Docker:

1. Construye la imagen:
   ```
   docker build -t app-crypto .
   ```

2. Ejecuta el contenedor:
   ```
   docker run -it app-crypto
   ```

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de hacer un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

Creado por [Tu Nombre] - Siéntete libre de contactarme para cualquier pregunta o sugerencia.