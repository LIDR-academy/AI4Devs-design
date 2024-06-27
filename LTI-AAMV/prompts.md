# Instrucciones para ChatGPT 4o

## 1. Descripción del Software LTI

Eres un experto en producto, con experiencia en sistemas ATS (Applicant-Tracking System).
¿Qué funcionalidades básicas tiene un sistema ATS (Applicant-Tracking System)?
Descríbemelas en un listado, ordenado de mayor a menor prioridad

1. **Descripción breve del software LTI, valor añadido y ventajas competitivas.**
   - ¿Qué beneficios obtiene el cliente de un sistema ATS (Applicant-Tracking System) para considerar su uso?
   - ¿Qué alternativas tiene a usar un sistema ATS (Applicant-Tracking System) y cuando pueden ser relevantes?
   - ¿Cómo es el customer journey normal de un cliente que usa un ATS (Applicant-Tracking System)? Descríbeme paso a paso todas las interacciones
   - Ahora con este contexto, tengo una startup llamada LTI que quiere desarrollar el ATS (Applicant-Tracking System) del futuro.

    Para poner en perspectiva todavía no hay nada creado, así que toca ponerse el gorro de product manager y definir esas funcionalidades clave que harán brillar a LTI por encima de los competidores: aumentar la eficiencia para los departamentos de HR, mejorar la colaboración en tiempo real entre reclutadores y managers, automatizaciones, asistencia de IA en diversas tareas...es el momento de hacer brainstorming, investigar cuáles pueden ser las claves del éxito, y dejarlo plasmado para el resto del equipo.

    Tu misión es diseñar la primera versión del sistema, entregando los siguientes artefactos:

        1. Descripción breve del software LTI, valor añadido y ventajas competitivas. Explicación de las funciones principales. Añadir un diagrama Lean Canvas para entender el modelo de negocio
    - El diagrama canvas podria ser un lienzo en formato mermeid.js

2. **Descripción de los 3 casos de uso principales, con el diagrama asociado a cada uno:**
   - En el contexto de la startup LTI y el sistema ATS (Applicant-Tracking System) que estamos construyendo, tu eres un analista de software experto. Enumera y describe brevemente los casos de uso más importantes a implementar para lograr una funcionalidad básica. Estos presentados en diagrama UML de casos de uso en formato mermaid.js
   - Quisiera mejor representar estos casos de uso en plant uml para la aplicacion ATS (Applicant-Tracking System) describiendo tanto los casos de uso principales como los actores e interacciones que hay entre ellos y estos casos.
   - Ahora quiero enfocarme en los tres casos de uso principales por cada uno genera un diagrama en plant uml con los actores e interacciones con cada caso y casos secundarios que puedan surgir apartir de este.

    Caso 1 Publicar Oferta de Trabajo
    Caso 2 Gestionar Candidatos
    Caso 3 Evaluar Candidatos

3. **Modelo de datos que cubra entidades, atributos (nombre y tipo) y relaciones.**
   - En este contexto eres un arquitecto de software experto. Cuales son las 3 entidades de modelo de datos esenciales para este sistema ATS (Applicant-Tracking System)? Dame algunos campos esenciales de cada una y cómo se relacionan.
   - Eres un brillante arquitecto de software. Eres capaz de diseñar, explicar y diagramar los diferentes aspectos de un sistema ATS (Applicant-Tracking System).

    Estoy construyendo un sistema de ATS (Applicant-Tracking System). He definido las entidades candidato, oferta de trabajo y proceso de selección, con sus campos y relaciones, lo adjunto.

    Qué otras entidades del modelo de datos son importantes en un sistema ATS (Applicant-Tracking System)? Dame los campos más importantes de cada una y cómo se relacionan entre entidades.

    Podrias entrega el codigo en formato mermaid.js

4. **Diseño del sistema a alto nivel, tanto explicado como diagrama adjunto (construido en https://www.eraser.io/)**
   - Ahora quisiera un prompt para exportar a ereaser.io con la arquitectura de este sistema ATS (Applicant-Tracking System).

    Donde se especifique la interacción de cada componente de esta forma:
        - A nivel de infraestructura en la nube por ejemplo usando AWS.
        - Integrando patrón de microservicios.
        - Herramientas de mensajes con kafka o rabbitq
        - Patron mensajes que permitan escalabilidad  (pensar en circuit breaker, rate limiter o backoff)
        - Desacoplamiento entre capas logicas y fisicas
        - Uso de api con buenas practicas.
        - Logs distribuidos
        - Cache con redis
        - Reverse proxy
        - Api gateway
        - Autoscaling
        - Database por cada microservicio
        - Para la creación y manejo de contenedores con docker, y kubernetes.
        - Herramientas de monitoring como el stack de logstash + kibana + prometeus y cloudwatch.
        - Además de load balancer
        - CDN como cloudfront.
        - CI/CD pipelines con terraform.
        - El frontend con herramientas como react, javascript, nextjs y tailwind.
        - Con protocolo de autenticacion oauth2.0 con keycloak como servidor de autorizacion y autenticacion.
        - Comunicacion entre el FrontEnd y BackEnd a través de tokens jwt.
        - Agregar componentes de seguridad como guardduty o waf, route53, aws kms.
        - Y crear la vpc ya sea usando ecs o aws kubernetes con fargate
        - Y las mejores practicas en esto.

5. **Diagrama C4 que llegue en profundidad a uno de los componentes del sistema:**
    - Eres un experto en diseño de arquitecturas de software y modelado de diagramas y un experto en modelado de diagramas C4.

    Y basados en esta documentación de modelamiento de diagramas de modelos de C4 en estos links:

    1. https://lukemerrett.com/c4-diagrams-as-code-architectural-joy/
    2. https://c4model.com/?ref=lukemerrett.com

    Además tomando en cuenta la siguiente arquitectura que adjunto en la imagen.

    Quiero diagramar en detalle el caso de uso de Publicar Oferta de Trabajo y sus sub casos de usos mencionados:

    usecase "Publicar Oferta de Trabajo"
    usecase "Crear Descripción de Trabajo"
    usecase "Aprobar Oferta de Trabajo"
    usecase "Publicar en Portales de Empleo"
    usecase "Notificar a Candidatos Existentes"

    Quisiera que generes como resultado el codigo en formato C4-PlantUML tomado de este link: https://github.com/plantuml-stdlib/C4-PlantUML

    Los 4 componentes del modelo C4:

    1. System Context diagram
    2. Container diagram
    3. Component diagram
    4. Code diagram

### Link

https://chatgpt.com/c/2cca756b-b2a2-4951-8fe5-19d223413074