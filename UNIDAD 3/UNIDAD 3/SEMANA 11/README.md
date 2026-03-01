# 🏬 Control de Inventario " Tienda "

Sistema desarrollado en Python para la administración eficiente de artículos, cumpliendo con estándares de POO y manejo de archivos planos.

---

##  Especificaciones de Implementación

---
### 1. Optimización con Colecciones
Se ha integrado un **Diccionario** como estructura de datos central para organizar los artículos de la tienda.

* **Acceso Directo:** La elección del diccionario permite localizar cualquier artículo mediante su ID de forma instantánea, optimizando el rendimiento del sistema.
* **Gestión Dinámica:** Gracias a métodos como `.pop()`, el sistema maneja la eliminación de ítems de forma segura, evitando errores de ejecución.
* **Escalabilidad:** Esta estructura permite que el inventario crezca sin degradar notablemente la velocidad de respuesta del menú.

---

### 2. Almacenamiento en Archivos Planos (.txt)
Para la persistencia de los datos, se diseñó un sistema de lectura y escritura de archivos:

* **Escritura:** Los datos se almacenan siguiendo un formato de valores separados por comas (CSV), lo que permite que el archivo sea ligero y fácil de auditar.
* **Lectura:** El programa incluye una función de carga automática que procesa el archivo línea por línea al iniciar, recuperando todo el stock guardado previamente.

---