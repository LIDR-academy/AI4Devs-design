Los pasos realizados son:

Paso 1. Para generar el prompt use los artifacts de Claude.

Paso 2. Prompt Original
Eres un ingeniero de software que se maneja con la tecnología actual y debes diseñar un sistema de gestión de candidatos.
Ttu misión será diseñar y documentar un sistema de software siguiendo las fases de investigación y análisis, casos de uso, modelado de datos, y diseño de alto nivel.

La empresa para la que debes trabajar se llama LTI.
LTI es una startup que quiere desarrollar el ATS (Applicant-Tracking System) del futuro. 
Si no sabes lo que es un ATS, adjunto una imagen, que vale más que 1000 palabras:

Todavía no hay nada creado, así que toca ponerse el gorro de product manager y definir esas funcionalidades clave que harán brillar a LTI por encima de los competidores: 
aumentar la eficiencia para los departamentos de HR, mejorar la colaboración en tiempo real entre reclutadores y managers, automatizaciones, asistencia de IA en diversas tareas...
es el momento de hacer brainstorming, investigar cuáles pueden ser las claves del éxito, y dejarlo plasmado para el resto del equipo.

Tu misión es diseñar la primera versión del sistema, entregando los siguientes artefactos:
1. Describir brevemente el software LTI, valor añadido y ventajas competitivas. 
2. Explicar las funciones principales. 
3. Añadir un diagrama Lean Canvas para entender el modelo de negocio, elije el formato que quieras pero debe ser posible cargarlo en una herramienta de generación de diagramas .
4. Descripción de los 3 casos de uso principales, con el diagrama asociado a cada uno, en este caso dame el codigo python para visualizar el diagrama en formato Diagrams(Diagrams as Code).
5. Crear el modelo de datos que cubra entidades, atributos (nombre y tipo) y relaciones.
6. Diseñar del sistema a alto nivel, tanto explicado como diagrama adjunto, en este caso dame el codigo python para visualizar el diagrama en formato Diagrams(Diagrams as Code).
7. Diagrama C4 que llegue en profundidad a uno de los componentes del sistema, el que prefieras.
8. Documenta todo en un único documento markdown (.md) con el nombre LTI-iniciales.

Debes usar lo ultimo de tecnología que ya haya sido validada y la usen los expertos en su campo
Antes de que empieces con el trabajo has las preguntas pertinentes que te permitan realizar el trabajo de la mejor forma.



Paso 3. Preguntas de la IA
Sobre el mercado objetivo:
¿El sistema está orientado a empresas de algún tamaño específico (startups, medianas empresas, grandes corporaciones)?
¿Hay alguna industria o sector particular al que queramos dirigirnos inicialmente?
Respuesta : Es para una startups y da lo mismo el sector

Sobre la diferenciación:
¿Hay algún competidor específico contra el que LTI quiera diferenciarse?
Respuesta: No
¿Hay algún punto débil en los ATS actuales que LTI haya identificado y quiera resolver?
Respuesta: Poca expertise en diseño de software


Sobre requerimientos técnicos:
¿Hay preferencia por una solución cloud-native o on-premise?
Respuesta: La solución que sea mas econónomica, recordar que somo una startup
¿Se requiere integración con alguna plataforma específica (LinkedIn, Indeed, Glassdoor)?
Respuesta: No
¿Hay requisitos específicos de cumplimiento o regulaciones (GDPR, CCPA) que debamos considerar?
Respuesta: No

Sobre la IA:
¿Hay algún área específica donde se quiera priorizar la implementación de IA (screening de CVs, scheduling, análisis predictivo)?
Respuesta: Lo que me recomiendes en base a lo que te he explicado antes.
¿Hay preferencia por desarrollar modelos propios o utilizar servicios de IA existentes?
Respuesta:Utilizar servicios de IA existentes, te dejo libertad para elegir uno gratuito.

Sobre el alcance inicial:
¿Cuál es el timeline esperado para el MVP?
Respuesta: No manejamos timeline, proyecta en base a tu experiencia
¿Hay alguna funcionalidad que deba estar sí o sí en la primera versión?
Respuesta: Todo el analisis y el diseño.


Sobre la escalabilidad:
¿Cuál es el número aproximado de usuarios/empresas que se espera tener en el primer año?
Respuesta: No lo tenemos claro
¿Hay expectativas específicas de crecimiento internacional?
Respuesta: No


Paso 4. Respuesta de la IA
Gracias por las respuestas. 
Dado el contexto de una startup con recursos limitados y enfoque en startups como clientes objetivo, diseñaré una solución cloud-native optimizada en costos, utilizando servicios serverless y pay-as-you-go cuando sea posible.
Procederé a crear los artefactos solicitados. 
Primero, permíteme crear el documento markdown base y luego iré desarrollando cada sección con los diagramas correspondientes.
Este documento representa la primera versión del diseño del sistema LTI-ATS. Está sujeto a revisiones y mejoras basadas en feedback y requisitos adicionales.
He creado un diseño completo del sistema que prioriza:

Bajo costo inicial (arquitectura serverless)
Simplicidad para startups
Automatización inteligente usando servicios de IA existentes
Escalabilidad según necesidad

¿Te gustaría que profundice en alguna sección específica o que ajuste alguna parte del diseño?

Paso 5. Instrucciones posteriores
me parece correcto lo que generaste en el markdown base, así que no cambies esa plantilla y continua con todo el proceso como lo planeaste

Paso 6. Respuesta de la IA
Entendido, mantendré la estructura del markdown que generé y procederé a crear el archivo final con el nombre solicitado.
LTI-AMS.mdClick to open document
He generado el archivo markdown final manteniendo la estructura original y asegurándome de que todos los diagramas y código estén correctamente formateados.
Algunas notas importantes sobre la implementación:

Los diagramas están en formato mermaid y código Python para fácil visualización
El modelo de datos está en SQL estándar
La arquitectura está optimizada para costos usando servicios serverless
Se han mantenido todas las secciones solicitadas en el orden original

¿Necesitas que ajuste algo específico del documento o que profundice en alguna sección?

Paso 7
No, muchas gracias por la ayuda

Paso 8. Respuesta final de la IA
Gracias a ti por permitirme ayudarte con el diseño del sistema ATS. El documento incluye una arquitectura serverless optimizada para startups, con todas las herramientas necesarias para visualizar los diagramas (Mermaid Live Editor, dbdiagram.io, Python Diagrams).
¡Que tengas éxito con la implementación del sistema! Si en el futuro necesitas más ayuda o tienes preguntas adicionales, no dudes en consultarme.
¡Que tengas un excelente día!
