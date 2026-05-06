# 🛒 Coffee Cart - SPA Backend (Etapa 1)

## Alumno: Luis Calegari.
## Fecha: 06/05/2026.

🌍 *[Read this in English](#english-version)*

## 📝 Descripción del proyecto
Este proyecto es la primera etapa del trabajo práctico "Desarrollo de Aplicación Web SPA" para la materia **Programación Web 2**. Consiste en el desarrollo de un servidor backend que expone una serie de APIs RESTful para gestionar un carrito de compras, inspirado en la aplicación "Coffee Cart".

## 📌 Estado del proyecto

- Etapa 1 (Backend): ✔ Completada
- Etapa 2 (Frontend SPA): ⏳ En progreso
- Etapa 3 (Integración final): ⏳ Pendiente

## 🎯 Objetivo de la Etapa 1
El objetivo principal de esta etapa es implementar el servidor backend inicial con una persistencia de datos en memoria (sin base de datos real por ahora) y documentar sus APIs. 

**Requerimientos cumplidos:**
- Endpoints para listar productos, agregar/eliminar productos del carrito y calcular el total.
- Persistencia en memoria.
- Documentación de las APIs con Swagger/OpenAPI.
- Tests unitarios de los endpoints principales.

## 🛠️ Tecnologías usadas
- **Lenguaje:** Python 3
- **Framework Web:** Flask
- **CORS:** Flask-CORS (preparado para la Etapa 2 con el frontend)
- **Documentación API:** Flasgger (Swagger UI) / OpenAPI 3.0.0
- **Testing:** Pytest & Pytest-Flask

## 📦 Requisitos previos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

## 🚀 Cómo correr el backend

1. **Clonar el repositorio y navegar a la carpeta del proyecto**
2. **Crear y activar un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```
3. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```
   *El servidor se iniciará en `http://localhost:5000`.*

## 🧪 Cómo correr los tests

Para ejecutar las pruebas unitarias y asegurar que los endpoints funcionen correctamente, utiliza el siguiente comando:
```bash
pytest
```
*Las pruebas se encuentran en el directorio `tests/`.*

## 📂 Estructura del proyecto

```text
tp-spa-backend/
├── app.py                 # Punto de entrada de la aplicación y configuración de Flask/Swagger
├── requirements.txt       # Dependencias del proyecto
├── controllers/           # Lógica de los controladores
├── data/                  # Almacenamiento en memoria (productos, carrito)
├── docs/
│   └── openapi.yaml       # Archivo de especificación de la API (OpenAPI 3.0)
├── routes/                # Definición de rutas (Blueprints: products.py, cart.py)
├── services/              # Lógica de negocio
└── tests/                 # Pruebas unitarias (Pytest)
    ├── conftest.py
    ├── test_cart.py
    └── test_products.py
```

## 📖 Documentación Swagger

La API está completamente documentada utilizando Swagger UI. Una vez que el backend esté en ejecución, puedes acceder a la documentación interactiva visitando:

🔗 **[http://localhost:5000/apidocs/](http://localhost:5000/apidocs/)**

### Endpoints principales expuestos:
- `GET /products`: Listar todos los productos disponibles.
- `POST /cart/add`: Agregar un producto al carrito indicando ID y cantidad.
- `DELETE /cart/{product_id}`: Eliminar un producto del carrito.
- `GET /cart/total`: Obtener el costo total de la compra.

## 👤 Autor

**Luis Calegari**  
Estudiante de Licenciatura en Informática
GitHub: https://github.com/Calegaris

## 📄 Licencia

Este proyecto es de uso académico.

---
---

<a name="english-version"></a>
# 🛒 Coffee Cart - SPA Backend (Stage 1)

🇪🇸 *[Leer en Español](#-coffee-cart---spa-backend-etapa-1)*

## 📝 Project Description
This project is the first stage of the "SPA Web Application Development" assignment for the **Web Programming 2** course. It consists of developing a backend server that exposes a series of RESTful APIs to manage a shopping cart, inspired by the "Coffee Cart" application.

## 📌 Project Status

- Stage 1 (Backend): ✔ Completed
- Stage 2 (Frontend SPA): ⏳ In Progress
- Stage 3 (Final Integration): ⏳ Pending

## 🎯 Stage 1 Objective
The main objective of this stage is to implement the initial backend server with in-memory data persistence (no real database for now) and document its APIs.

**Completed Requirements:**
- Endpoints to list products, add/remove products from the cart, and calculate the total.
- In-memory persistence.
- API documentation with Swagger/OpenAPI.
- Unit testing for main endpoints.

## 🛠️ Technologies Used
- **Language:** Python 3
- **Web Framework:** Flask
- **CORS:** Flask-CORS (ready for Stage 2 frontend integration)
- **API Documentation:** Flasgger (Swagger UI) / OpenAPI 3.0.0
- **Testing:** Pytest & Pytest-Flask

## 📦 Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Git (for cloning the repository)

## 🚀 How to Run the Backend

1. **Clone the repository and navigate to the project folder**
2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**
   ```bash
   python app.py
   ```
   *The server will start at `http://localhost:5000`.*

## 🧪 How to Run Tests

To execute the unit tests and ensure the endpoints are working correctly, use the following command:
```bash
pytest
```
*Tests are located in the `tests/` directory.*

## 📂 Project Structure

```text
tp-spa-backend/
├── app.py                 # Application entry point & Flask/Swagger configuration
├── requirements.txt       # Project dependencies
├── controllers/           # Controller logic
├── data/                  # In-memory storage (products, cart data)
├── docs/
│   └── openapi.yaml       # API specification file (OpenAPI 3.0)
├── routes/                # Route definitions (Blueprints: products.py, cart.py)
├── services/              # Business logic
└── tests/                 # Unit tests (Pytest)
    ├── conftest.py
    ├── test_cart.py
    └── test_products.py
```

## 📖 Swagger Documentation

The API is fully documented using Swagger UI. Once the backend is running, you can access the interactive documentation by visiting:

🔗 **[http://localhost:5000/apidocs/](http://localhost:5000/apidocs/)**

### Main Endpoints exposed:
- `GET /products`: List all available products.
- `POST /cart/add`: Add a product to the cart (requires product ID and quantity).
- `DELETE /cart/{product_id}`: Remove a product from the cart.
- `GET /cart/total`: Get the total cost of the purchase.

## 👤 Author

**Luis Calegari** 
Computer Science Student
GitHub: https://github.com/Calegaris

## 📄 License

This project is for academic use.