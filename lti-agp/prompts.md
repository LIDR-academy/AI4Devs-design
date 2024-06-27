chatGPT 4 + diagramGPT
# 1.
Eres un experto en producto. Necesitas modelar un sistema ATS (Applicant Tracking System), cuyo objetivo basico es el siguiente:

- aumentar la eficiencia para los departamentos de HR
- mejorar la colaboración en tiempo real entre reclutadores y managers
- automatizaciones
- asistencia de IA en diversas tareas

Las funcionalidades basicas las encuentras visitando esta URL. de imagen --> https://media1-production-mightynetworks.imgix.net/asset/62a578e5-90e4-40a1-a09f-c86209424fe1/1713970482103.png?ixlib=rails-4.2.0&fm=jpg&q=75&auto=format
----------------
Empecemos por una Descripción breve del software, valor añadido y ventajas competitivas.
Para ello necesito una explicación de las funciones principales, en un listado, ordenado de mayor a menor prioridad.
Luego una tabla comparativa entre mi software y los 3 principales ATS lideres del mercado. Compáralos en función de las 5 funcionalidades mas demandadas por reclutadores y managers.

# 2
genera un diagrama Lean Canvas para entender el modelo de negocio y que recoja todo lo anterior de manera visual conforme al Lean Canvas.

# 3
Eres un analista de software experto. Enumera y describe brevemente los 3 casos de uso más importantes a implementar para el producto anterior

# 4 
Representa estos casos de uso en el tipo de diagrama más adecuado usando el formato plantUML. Acorde a la sintaxis y buenas prácticas UML, define y describe lo que sea necesario

# 5
Eres un brillante arquitecto de software. Eres capaz de diseñar, explicar y diagramar los diferentes aspectos de un sistema de software.
Identifica las entidades principales para diseñar el modelo de datos del producto anterior

# 6 
In diagramGPT, I used this to generate the architecture diagram:
- a monolith architecture, using React in the frontend, nodeJS in the backend (serverless Lambda) and PostgreSQL as the DB
- There is a web application in React, and a mobile app using Electron from the React codebase
- There are 2 BFF in graphQL to serve each of the 2 apps.
- Use AWS resources
- We will use AWS Cognito for Auth
- Implement all security practices
# 7 
in chatGPT
Now implement a C4 diagram for the above system

