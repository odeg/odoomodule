# 🧩 Odoo Modules

Este proyecto contiene un entorno de desarrollo Odoo 17 con módulos personalizados desarrollados como prueba técnica. Incluye Docker, configuración, y módulos listos para instalar.

---

## 🌐 Demo en línea

Podés ver el resultado funcionando directamente en este enlace:

👉 [https://odoo-ford.fly.dev](https://odoo-ford.fly.dev)

- Ingresá a los módulos de **Inventario** y **Cotizaciones**
- Explorá cómo se visualizan las funciones implementadas:
  - Productos Personalizados
  - Campo `Tipo de Cotización`
  - Validación de facturas vencidas

---

## 🚀 Módulos incluidos

- `producto_personalizado`: Gestión básica de productos personalizados con nombre, descripción, precio y stock.
- `cotizacion_heredada`: Extiende el modelo `sale.order` con un campo adicional y validaciones de negocio.

---

## ⚙️ Requisitos

- Docker
- Docker Compose

---

## 📦 Instalación local

### 1. Cloná el repositorio:
```bash
git clone https://github.com/odeg/odoomodule.git
cd odoomodule
```

### 2. Verificá la estructura

```
├── docker-compose.yml
├── odoo.conf
├── addons/
│   ├── producto_personalizado/
│   ├── cotizacion_heredada/
└── db/
    └── data/
```

### 3. Levantá los servicios:

```bash
docker compose up -d
```

### 4. Accedé a Odoo localmente:

👉 http://localhost:8079

---

## 🛠️ Configuración inicial

1. Crear una nueva base de datos desde el navegador
2. **Desactivar** la opción de "Demo data"
3. Activar el **modo desarrollador**:

👉 http://localhost:8079/web?debug=1

4. Desde el menú desarrollador:  
   **Actualizar la lista de aplicaciones**

---

## ✅ Instalación de módulos

### Primero, instalá estos módulos nativos de Odoo:

- **Ventas** – “De cotizaciones a facturas”
- **Inventario** – “Gestione sus actividades de inventario y logística”

### Luego, instalá los módulos personalizados:

- `Producto Personalizado`
- `Cotización Heredada`
- `Reporte Producto Personalizado`

---

## 🧪 Pruebas funcionales

### Producto Personalizado
![alt text](/assets/image.png)

![alt text](/assets/image-1.png)

- Vista tipo lista y formulario
- Campos: nombre, descripción, precio y stock

### Cotización Heredada

- Normal
![alt text](/assets/image-2.png)

- Promocion
![alt text](/assets/image-3.png)

- Facturas Vencidas
![alt text](/assets/image-4.png)

- Campo nuevo: `Tipo de Cotización`
- Si el tipo es **Promoción** y el cliente tiene **facturas vencidas**, no se puede confirmar la cotización



## 👨‍💻 Autor

Desarrollado por Oscar Estigarribia 

---

## 📄 Licencia

Uso educativo y demostrativo.