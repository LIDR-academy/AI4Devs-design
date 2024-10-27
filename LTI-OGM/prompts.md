## Prompts

### 1 - Inicio del análisis
Eres un experto product manager. Necesito diseñar y documentar un sistema de software siguiendo las fases de investigación y análisis, casos de uso, modelado de datos, y diseño de alto nivel de LTI (Leaders.Technology.Impact), una startup que quiere desarrollar el ATS (Applicant-Tracking System) del futuro.

Mis objetivos principales son aumentar la eficiencia para los departamentos de HR, mejorar la colaboración en tiempo real entre reclutadores y managers, automatizaciones y asistencia de IA en diversas tareas. Si tienes alguna idea más la podemos incorporar. 

Quiero generar un documento que contenga:
- Descripción breve del software LTI, valor añadido y ventajas competitivas. Explicación de las funciones principales. Añadir un diagrama Lean Canvas para entender el modelo de negocio
- Descripción de los 3 casos de uso principales, con el diagrama asociado a cada uno 
- Modelo de datos que cubra entidades, atributos (nombre y tipo) y relaciones. 
- Diseño del sistema a alto nivel, tanto explicado como diagrama adjunto 
- Los diagramas C4 en profundidad de uno de los componentes (más adelante te indicaré cuál).

Vayamos por partes; empecemos por el primer punto. ¿Tienes alguna pregunta antes de empezar?

> ### Preguntas
> 1. **Público objetivo**: ¿Este ATS está orientado a empresas de algún sector específico o de cualquier tamaño? Es decir, ¿se enfocará en startups, empresas medianas o grandes corporativos, o será adaptable a todas?
> 2. **Automatización e IA**: Ya que uno de tus objetivos es mejorar la eficiencia mediante automatizaciones e IA, ¿tienes en mente algún tipo específico de asistencias de IA (p. ej., redacción de descripciones de trabajo, filtros automáticos de currículums, sugerencias de candidatos, predicción de rotación)?
> 3. **Colaboración en tiempo real**: ¿Qué tan profunda debe ser la colaboración? ¿Te refieres a funciones como chat integrado, revisión colaborativa de perfiles, toma de decisiones en tiempo real, o algo más específico?
> 4. **Análisis de métricas y reporting**: ¿Es importante que la plataforma tenga capacidades avanzadas de análisis de datos para ofrecer reportes personalizados, predicciones de contratación o rendimiento de procesos? Esto podría aumentar mucho el valor diferencial si forma parte de la visión.
> 5. **Integraciones con otros sistemas**: ¿Se espera que el sistema ATS sea capaz de integrarse con otras herramientas de HR, como plataformas de payroll, gestión de empleados o ERPs, o con redes sociales y sitios de empleo? Esto podría impactar el diseño y el modelo de datos.

### 2 - Clarificación del público objetivo y funcionalidades principales
1) Enfoqúemonos en PYMES
2) Usa la IA para hacer la evaluación inicial y el filtrado de los candidatos
3) Usa un chat integrado que permita hacer evaluaciones y decisiones colaborativas en tiempo real.
4) Incluye analíticas de métricas del rendimiento de los procesos.
5) Intégralo con LinkedIn para extraer perfiles de candidatos y contactar con ellos, y con un ERP para la gestión de las contrataciones. 
 
Toma la decisión de qué ERP utilizar, y refiérelo de ahora en adelante.

### 3 - Solicitud de casos de uso y diagramas
Continuemos con el siguiente punto: Casos de uso. Usa plantUML para generar los diagramas.

### 4 - Ajustes en el primer caso de uso
En el primer caso de uso, los CV se deberían procesar y filtrar automáticamente, sin la necesidad del reclutador. 

Este interactuará solamente con los candidatos que hayan pasado el cribaje inicial de la IA.

### 5 - Ajustes en el segundo caso de uso
En el segundo caso, los actores deberían poder tener acceso a la grabación, transcripción con timestamps y puntos clave de la entrevista con el candidato, para poder analizarlos colaborativamente a tiempo real.

Indica los actores participantes en la entrevista: el candidato y el recruiter.

### 6 - Solicitud de modelo de datos
El tercer caso de uso ya me parece correcto. Pasemos al modelo de datos. De ahora en adelante con PlantUML, siempre que puedas incluir un diagrama, usa PlantUML.

### 7 - Ajustes en el modelo de datos
Echo en falta: 
- Puntos clave en la entrevista
- Estado de la entrevista (en curso, transcripción pendiente, revisión pendiente, completada) 
- Estado del candidato. Define todos los que consideres necesarios.

Los estados pueden servir para gestionar notificaciones a los actores correspondientes.

### 8 - Solicitud del diseño del sistema a alto nivel
Continúa con el siguiente paso.

### 9 - Análisis en detalle del módulo de evaluaciones y notificaciones usando C4
De acuerdo, analicemos el módulo de evaluaciones y notificaciones en detalle con los diagramas C4. Vayamos nivel por nivel para poder ir haciendo correcciones.

### 10 - Ajustes en el nivel 1 del diagrama C4
Me faltaría la interacción con el módulo de entrevistas, así como los módulos en el frontend. Haz que estos sustituyan a los actores, pues los actores interactúan a través de dichos módulos.

### 11 - Ajustes en la gestión de grabaciones en el diagrama C4 Nivel 1
Creo que las grabaciones las debería gestionar el módulo del chat a tiempo real, no el de evaluaciones. El de evaluaciones debería recibir el resultado con la decisión del recruiter y el manager.

### 12 - Solicitud de análisis completo actualizado del Nivel 1 (Contexto)
Devuélveme el análisis. Siempre que te lo pida, asegúrate de que esté completo, listo para que yo pueda guardarlo con el resto de la documentación.

### 13 - Avance al Nivel 2 del análisis C4 (Contenedor)
Continuemos con el nivel 2.

### 14 - Ajustes en el Servicio de Gestión de Estados y notificaciones
- Cambia el nombre del servicio de gestión de estados a gestión de candidatos. 
- Los sistemas de gestión de candidatos y de evaluaciones deberían, de manera independiente, actualizar el estado del candidato, basado en los inputs que reciba cada uno de ellos.
- El sistema de notificaciones debería reaccionar a las actualizaciones de los otros dos sistemas.

### 15 - Avance al Nivel 3 (Componente)
Pasemos al siguiente nivel.

### 16 - Solicitud de clases y funciones para el diagrama de Nivel 4
Todo en orden, pasemos al siguiente nivel. ¿Me puedes proporcionar las clases y sus funciones en un diagrama?

### 17 - Confirmación final de que el análisis está completo
Todo listo! ¿Puedes darme todos los prompts que he usado hasta ahora?
