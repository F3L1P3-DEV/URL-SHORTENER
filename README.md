# ✂️ URL Shortener (Acortador de Enlaces)

Un acortador de enlaces web sencillo, rápido y funcional desarrollado con **Python (Flask)** para la lógica del servidor y **HTML/CSS** para la interfaz de usuario. 

Este proyecto demuestra cómo conectar el backend con el frontend, procesar peticiones HTTP (GET y POST), generar códigos aleatorios únicos y manejar redirecciones en tiempo real.

---

## 🚀 Características

* **Interfaz Web Limpia:** Diseño simple y responsivo con HTML y CSS.
* **Generación Aleatoria:** Crea códigos únicos de 5 caracteres para cada URL de forma dinámica.
* **Redirección Automática:** Al acceder al enlace corto, el servidor te redirige instantáneamente a la página web original.
* **Manejo de Errores:** Mensaje de advertencia si un usuario intenta ingresar a un código que no existe.

---

## 🛠️ Tecnologías Utilizadas

* **Python 3.x**
* **Flask** (Micro-framework de Python para desarrollo web)
* **HTML5 y CSS3** (Estructura y diseño visual)

---

## 📂 Estructura del Proyecto

```text
├── app.py               # Servidor Flask y lógica de acortamiento
└── templates/           # Vistas HTML
    ├── index.html       # Página principal (Formulario)
    └── resultado.html   # Página de éxito (Enlace generado)
