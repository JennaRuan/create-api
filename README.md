Estructura del proyecto
--------------------

create-api/  
├── app/  
│   ├── __init__.py  
│   ├── main.py              # Punto de entrada de la aplicación  
│   ├── database.py          # Configuración de SQLite  
│   ├── models.py            # Modelos de la base de datos  
│   ├── routes/  
│   │   └── tasks.py         # Endpoints de la API  
│   └── tests/               # Pruebas unitarias  
├── instance/  
│   └── tasks.db             # Base de datos SQLite (se crea al ejecutar)  
├── Dockerfile               # Configuración para Docker   
├── requirements.txt         # Dependencias de Python  
└── README.md                # Documentación del proyecto

Pruebas automatizadas
--------------------

Ejecutar con tests unitarios

```bash
python -m pytest app/tests/
```

Probar con script PowerShell (Windows)  
    
```powershell
.\test_api.ps1
``` 

Retos de aprendizaje
--------------------

## 1. **Aprendiendo Swagger**

Pasos tomados:
- Leí la documentación oficial de Swagger UI y Flask-RESTx.
- Implementé anotaciones @api.doc() y modelos en main.py.
- Probé la interfaz en /swagger-ui para validar la documentación.

## 2. **Resolviendo dudas sobre Docker**

Yo ya estaba familiarizado con Docker, pero aún no con Docker Compose, lo cual al utilizar por ahora SQLite no fue necesario. Pero si fuera el caso, utilizaria recursos como:
- La documentación oficial de Docker Compose para su realización.

## 3. **Desafios encontrados**

- Importar correctamente las librerías de Flask y SQLite.
- Configurar correctamente la base de datos SQLite y las rutas de la API.
- Manejar errores y excepciones en la API.
- Definir los modelos exactos para las respuestas HTTP.

## 4. **Mejoras pendiente**

- La parte de la seguridad, añadir autenticación con JWT.
- Cubrir más casos de error en la parte del testeo.
- CI/CD: Configurar GitLab CI pero el único acceso que tenía era por parte de la empresa en la que me encuentro trabajando, por lo que no pude realizarlo.