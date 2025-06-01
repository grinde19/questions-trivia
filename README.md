# 🧠 Questions Trivia API

Una API REST completa para gestionar preguntas de trivia construida con Flask, PostgreSQL y Docker.

## 🚀 Instalación Rápida

### Prerrequisitos

- Docker
- Docker Compose

### Ejecutar el proyecto

1. **Clona el repositorio:**

```bash
git clone questions-trivia.git
cd questions-trivia
```

2. **Ejecuta con Docker:**

```bash
docker-compose up --build
```

3. **¡Listo!** La API estará disponible en:

```
http://localhost:5000
```

La aplicación se configurará automáticamente:

- ✅ Base de datos PostgreSQL
- ✅ Migraciones aplicadas automáticamente
- ✅ Todas las tablas creadas
- ✅ API lista para usar

## 📊 Estructura de la Base de Datos

El sistema incluye las siguientes entidades:

- **Users** - Usuarios del sistema
- **Roles** - Roles de usuario
- **Levels** - Niveles de dificultad
- **Questions** - Preguntas de trivia
- **Answers** - Respuestas a las preguntas
- **Trivias** - Conjunto de preguntas
- **User_Roles** - Relación usuarios-roles
- **User_Trivia** - Relación usuarios-trivias

## 🛠️ Tecnologías Utilizadas

- **Flask** - Framework web de Python
- **PostgreSQL** - Base de datos
- **SQLAlchemy** - ORM para Python
- **Flask-Migrate** - Manejo de migraciones
- **Marshmallow** - Serialización/Deserialización
- **Docker** - Containerización
- **Docker Compose** - Orquestación de contenedores

## 📁 Estructura del Proyecto

```
questions-trivia/
├── app/
│   ├── __init__.py          # Factory de la aplicación
│   ├── models/              # Modelos de BD
│   ├── controllers/         # Controladores
│   ├── schemas/             # Schemas
│   ├── services/            # Servicios que ejecutan la lógica de negocios
│   ├── database.py          # Configuración de la base de datos
│   ├── config.py            # Configuraciones
│   └── routes/              # Blueprints de rutas
├── migrations/              # Migraciones de la base de datos
├── migrate.py               # Script que corre las migraciones
├── run.py                   # Punto de entrada de la aplicación
├── requirements.txt         # Dependencias de Python
├── Dockerfile               # Configuración de Docker
├── docker-compose.yml       # Orquestación de servicios
├── entrypoint.sh            # Script que valida si la carpeta migrations existe antes de ejecutar las migraciones
├── wait-for-it.sh           # Script que hará que espera al contenedor de la DB antes de arrancar flask
└── README.md                # Este archivo
```

## 🔧 Comandos Útiles

### Desarrollo con migraciones automáticas:

```bash
docker-compose up
```

### Desarrollo sin ejecutar migraciones:

```bash
SKIP_MIGRATIONS=true docker-compose up
```

### Reiniciar completamente (eliminar datos):

```bash
docker-compose down -v
docker-compose up --build
```

## 🌐 Endpoints de la API

### Ruta principal

- `GET /` - Estado de la API

### Usuarios

- `GET /api/users` - Obtener todos los usuarios
- `POST /api/users` - Crear un nuevo usuario
- `GET /api/users/<id>` - Obtener usuario por ID
- `PUT /api/users/<id>` - Actualizar usuario
- `DELETE /api/users/<id>` - Eliminar usuario
- `PUT /api/users/<id>/roles` - Asignar roles a un usuario (lista de IDs de roles)

- Ejemplo de body para POST /api/users/

```bash
{
  "username": "Player 1",
  "email": "player@gmail.com",
  "password":"1234"
}
```

- Ejemplo de body para PUT /api/users/<user_id>/roles/

```bash
{
 "role_ids": [1, 2, 5]
}
```

### Preguntas

- `GET /api/questions` - Obtener todas las preguntas
- `POST /api/questions` - Crear una nueva pregunta
- `GET /api/questions/<id>` - Obtener pregunta por ID
- `PUT /api/questions/<id>` - Actualizar pregunta
- `DELETE /api/questions/<id>` - Eliminar pregunta
- `GET /api/levels/<level_id>/questions/` - lista preguntas por tipo de dificultad
- `GET /api/trivias/<level_id>/questions/` - Lista preguntas por cada trivia

- Ejemplo de body para POST /api/questions/

```bash
{
  "text": "Donde Nacio Jesús",
  "level_id": 1,
	"trivia_id": 1
}
```

### Respuestas

- `GET /api/answers` - Obtener todas las respuestas
- `GET /api/answers/<id>` - Obtener respuesta por ID
- `PUT /api/answers/<id>` - Actualizar respuesta
- `DELETE /api/answers/<id>` - Eliminar respuesta

- `GET /api/questions/<question_id>/answers/` - Lista respuesta por pregunta
- `POST /api/questions/<question_id>/answers/` - Crea respuesta por pregunta

- Ejemplo de body para POST api/questions/<question_id>/answers

```bash
{
  "text": "Venezuela",
  "is_correct": false
}
```

### Niveles

- `GET /api/levels` - Obtener todos los niveles
- `POST /api/levels` - Crear un nuevo nivel
- `GET /api/levels/<id>` - Obtener nivel por ID
- `PUT /api/levels/<id>` - Actualizar nivel
- `DELETE /api/levels/<id>` - Eliminar nivel

- Ejemplo de body para POST /api/levels/

```bash
{
"text": "Facil"
}
```

### Trivias

- `GET /api/trivias` - Obtener todas las trivias
- `POST /api/trivias` - Crear una nueva trivia
- `GET /api/trivias/<id>` - Obtener trivia por ID
- `PUT /api/trivias/<id>` - Actualizar trivia
- `DELETE /api/trivias/<id>` - Eliminar trivia

- `GET /api/trivias/<trivia_id>/users` - Listar los usuarios por trivia
- `POST /api/trivias/<trivia_id>/users` - Listar los usuarios por trivia

- Ejemplo de body para POST /api/trivias/

```bash
{
  "text": "Preguntas de Historia"
}
```

- Ejemplo de body para POST /api/trivias/<trivia_id>/users

```bash
{
	    "user_ids": [1,2]
}
```

### Roles

- `GET /api/roles` - Obtener todos los roles
- `POST /api/roles` - Crear un nuevo rol
- `GET /api/roles/<id>` - Obtener rol por ID
- `PUT /api/roles/<id>` - Actualizar rol
- `DELETE /roles/<id>` - Eliminar rol

- Ejemplo de body para POST /api/roles/

```bash
{
  "text": "Administrador"
}
```

### USER_ANSWER

- `GET api/user-answer/trivias/<trivia_id>/stats/` - Obtiene los resultados de trivia por cada usuario
- `POST /api/user-answer/` - Guarda los resultados de las trivias por cada usuario

- Ejemplo de body para POST /api/user-answer/

```bash
{
	"user_id": 2,
	"trivia_id": 1,
	"responses": [
		{
		 "question_id": 1,
		"answer_id": 1
	 },
	 {
		 "question_id": 1,
		"answer_id": 2
	 },
	 {
		 "question_id": 1,
		"answer_id": 5
	 },
		{
		 "question_id": 2,
		"answer_id": 3
	 },
	 {
		 "question_id": 1,
		"answer_id": 4
	 },
	 {
		 "question_id": 1,
		"answer_id": 6
	 }
	]
}
```

- Ejemplo de respuesta para GET api/user-answer/trivias/<trivia_id>/stats/

```bash
[
	{
		"answered_questions": 2,
		"correct_answers": 4,
		"total_points": 4,
		"total_questions": 2,
		"user_id": 2,
		"wrong_answers": 8
	}
]
```

## 🔍 Testing

Para probar que la API funciona:

```bash
# Probar endpoint principal
curl http://localhost:5000

# Respuesta esperada:
{
  "message": "API Flask funcionando correctamente!",
  "status": "success"
}
```

### 🎯 Estado del Proyecto

**Este proyecto le falta:**

- Optimizar algunos endpoints
- Mejor validación de errores
- La tabla donde se guardan los resultados por usuario puede ser optimizada
- Arreglar los resultados en el API /api/user-answer/, no esta haciendo las cuentas de forma correcta.
