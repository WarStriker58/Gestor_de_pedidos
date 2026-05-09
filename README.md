# 📦 OrderFlow API – Gestor de Pedidos

OrderFlow API es una aplicación desarrollada con Django y Django REST Framework que permite administrar **clientes** y **pedidos** de manera sencilla mediante una API REST.  
El proyecto implementa CRUD completo para ambas entidades, así como la relación entre ellas, cumpliendo con los requisitos del laboratorio.

---

## 🛠 Tecnologías Utilizadas
- Python 3.x  
- Django 5.x  
- Django REST Framework  
- SQLite3 (por defecto)  
- Postman / DRF Browsable API para pruebas  

---

## ▶️ Instrucciones para Ejecutar el Proyecto

### 1. Clonar el repositorio  
```bash
git clone <URL-del-repositorio>
cd orderflow_api
```

### 2. Crear y activar un entorno virtual
```bash
python -m venv venv

Windows: 
venv\Scripts\activate
Linux / MacOS: 
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Ejecutar el servidor
```bash
python manage.py runserver
```

El proyecto se ejecutará en:
http://127.0.0.1:8000/

---

## 📚 Endpoints Disponibles

### Entidad Clientes:

#### GET
![GET](imgs/get_cliente.png)

![DB_GET_CLIENTE](imgs/db_get_cliente.png)

#### POST
![POST](imgs/post_cliente.png)

![DB_POST_CLIENTE](imgs/db_post_cliente.png)

#### PUT
![PUT](imgs/put_cliente.png)

![DB_PUT_CLIENTE](imgs/db_put_cliente.png)

#### DELETE
![DELETE](imgs/delete_cliente.png)

![DB_DELETE_CLIENTE](imgs/db_delete_cliente.png)



### Entidad Pedidos:

#### GET
![GET](imgs/get_pedido.png)

![DB_GET_PEDIDO](imgs/db_get_pedido.png)

#### POST
![POST](imgs/post_pedido.png)

![DB_POST_PEDIDO](imgs/db_post_pedido.png)

#### PUT
![PUT](imgs/put_pedido.png)

![DB_PUT_PEDIDO](imgs/db_put_pedido.png)

#### DELETE
![DELETE](imgs/delete_pedido.png)

![DB_DELETE_PEDIDO](imgs/db_delete_pedido.png)



### Entidad Productos:

#### GET
![GET](imgs/get_producto.png)

![DB_GET_PRODUCTO](imgs/db_get_producto.png)

#### POST
![POST](imgs/post_producto.png)

![DB_POST_PRODUCTO](imgs/db_post_producto.png)

#### PUT
![PUT](imgs/put_producto.png)

![DB_PUT_PRODUCTO](imgs/db_put_producto.png)

#### DELETE
![DELETE](imgs/delete_producto.png)

![DB_DELETE_PRODUCTO](imgs/db_delete_producto.png)

## 📹 Video Explicativo

https://www.youtube.com/watch?v=ZoUKkjPuOwo