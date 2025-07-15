# 🌌 NicBread: Gestión de Clientes – 2025

**Repositorio del Primer Parcial - Algoritmos y Estructuras de Datos II**  
Grupo B – Instituto Superior de Formación Técnica N.º 151  
📁 `primer_parcial_jose_2025` – by [pmac80](https://github.com/pmac80)

> "Mucho código este proyecto tiene. Funcional es. Claridad trae, sí." – Yoda 🧙‍♂️

---

## 🥖 Descripción

NicBread, panificadora galáctica, necesitaba una app para gestionar sus clientes... y aquí está.  
Una app en Python, hecha con Tkinter + SQLite, usando arquitectura por capas (MVC), como dicta el Consejo Jedi de la POO.

¡No más panes sin dueño!

---

## 🚀 Funcionalidades del Módulo "Clientes"

✅ Dar de alta (Alta hay que dar, joven padawan)  
✅ Eliminar por código (Baja... como Anakin, sí)  
✅ Modificar (Cambiar a tiempo, puede evitar errores)  
✅ Listar todos (Ver la república entera)  
✅ Buscar por código (Un cliente, encontrar debes)  
✅ Logs en consola (Lo que haces... saber debes)

---

## 🧩 Arquitectura del Código

```plaintext
+ main.py             # La fuerza inicial
+ model/
  └── cliente.py      # El ser que representa a un Cliente
+ controller/
  └── cliente_controller.py  # Controla la base de datos, él lo hace
+ view/
  └── app_gui.py      # Interfaz gráfica... ¡hermosa es!
