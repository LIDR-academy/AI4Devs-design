# ARTEFACTO 1

## Descripción breve del software LTI

LTI RecruitPro es un Sistema de Seguimiento de Candidatos (ATS) diseñado para optimizar el proceso de reclutamiento y selección en empresas de cualquier tamaño. A través de la automatización de tareas clave y la integración de herramientas de inteligencia artificial, LTI RecruitPro facilita la gestión de candidatos, la colaboración entre equipos y la toma de decisiones basada en datos, proporcionando una experiencia de usuario ágil, colaborativa y eficiente.

## Valor añadido y ventajas competitivas

1. **Eficiencia y Productividad Mejoradas**
   - Automatización de tareas repetitivas
   - Asistencia de IA para análisis de candidatos
   - Reducción significativa del tiempo en tareas de filtrado

2. **Colaboración en Tiempo Real**
   - Herramientas de colaboración integradas
   - Conexión entre reclutadores, managers y stakeholders
   - Evaluación en tiempo real y mejora en la comunicación

3. **Análisis Basado en IA**
   - Evaluación automatizada de currículums
   - Recomendaciones basadas en competencias y experiencia
   - Mayor precisión y velocidad en el proceso de selección

4. **Facilidad de Integración**
   - Conexión con sistemas HRIS
   - Integración con plataformas de nómina
   - Compatibilidad con sistemas de gestión de recursos humanos

5. **Optimización Continua Mediante Datos**
   - Herramientas de análisis de KPIs
   - Generación de informes automatizados
   - Toma de decisiones basada en datos históricos y predicciones

## Funcionalidades principales

### 1. Publicación y Gestión Centralizada de Ofertas de Empleo
- Publicación múltiple en portales y redes sociales
- Gestión centralizada de ofertas activas
- Actualización en tiempo real

### 2. Base de Datos de Candidatos y Captura Automática
- Organización de datos de múltiples fuentes
- Integración con LinkedIn y portales de empleo
- Sistema unificado de información

### 3. Evaluación de Candidatos y Filtros Inteligentes con IA
- Análisis automatizado de currículums
- Sistema de puntuación basado en IA
- Recomendaciones personalizadas

### 4. Pipeline de Reclutamiento
- Seguimiento en tiempo real
- Visualización del progreso de candidatos
- Gestión integral del proceso

### 5. Automatización de Comunicaciones
- Respuestas automáticas
- Actualizaciones de estado
- Sistema de seguimiento

### 6. Colaboración y Comunicación Interna
- Comunicación en tiempo real
- Sistema de comentarios y calificaciones
- Notas compartidas

### 7. Programación de Entrevistas
- Integración con calendarios
- Automatización de agendamiento
- Sistema de recordatorios

### 8. Reportes y Análisis
- Métricas clave de rendimiento
- Análisis predictivo
- Optimización basada en datos

## Lean Canvas

### Problema
- Tareas repetitivas y manuales en el reclutamiento
- Falta de colaboración eficaz en tiempo real
- Dificultad en evaluación de currículums
- Inconsistencia en análisis de candidatos

### Solución
- ATS con automatización e IA
- Dashboard intuitivo centralizado

### Propuesta de Valor
- Reducción del tiempo de contratación
- Asistencia de IA
- Colaboración en tiempo real
- Análisis de KPIs

### Ventaja Competitiva
- IA para análisis predictivo
- Colaboración en tiempo real
- Adaptabilidad empresarial

### Segmento de Clientes
- Empresas medianas y grandes
- Departamentos de recursos humanos
- Empresas enfocadas en eficiencia

### Métricas Clave
- Tiempo medio de contratación
- Tasa de conversión
- Retención de clientes
- Reducción de tareas manuales

### Canales
- Venta directa
- Eventos de RR.HH.
- Marketing digital

### Estructura de Costes
- Desarrollo y mantenimiento
- Infraestructura
- Marketing y ventas
- Soporte al cliente

### Flujo de Ingresos
- Suscripción mensual/anual
- Servicios adicionales

# ARTEFACTO 2

3 casos de uso principales, con el diagrama asociado a cada uno

**Caso de Uso 1: Publicación y Gestión de Ofertas de Empleo***
Descripción:
El reclutador puede crear y gestionar ofertas de empleo desde el sistema. Una vez creada, la oferta se publica en múltiples portales de empleo y redes sociales de manera automatizada. El reclutador puede realizar modificaciones en la oferta directamente desde el ATS, y estas se sincronizan en todas las plataformas donde fue publicada.

Flujo del Caso de Uso:

El reclutador accede al módulo de creación de ofertas de empleo.
Completa la información sobre la posición (título, descripción, requisitos, salario).
Selecciona las plataformas de publicación.
Publica la oferta en todas las plataformas.
Puede modificar o cerrar la oferta en cualquier momento.

      +--------------------+
      |     Reclutador     |
      +---------+----------+
                |
                v
      +--------------------+
      | Crear Oferta       |
      +--------------------+
                |
                v
      +--------------------+
      | Publicar en        |
      | Múltiples Plataf.  |
      +--------------------+
                |
                v
      +--------------------+
      | Sincronizar        |
      | Modificaciones     |
      +--------------------+


**Caso de Uso 2: Evaluación de Candidatos con IA**

Descripción:
La IA del sistema ATS evalúa automáticamente los currículums recibidos y califica a los candidatos en función de su coincidencia con los requisitos de la oferta. El sistema proporciona un ranking de candidatos y sugerencias, facilitando el proceso de preselección para el reclutador.

Flujo del Caso de Uso:

El sistema recibe currículums de diferentes fuentes.
La IA analiza y califica cada currículum en base a los requisitos definidos para la oferta.
La IA genera una lista de candidatos ordenados por su adecuación al puesto.
El reclutador revisa el ranking y selecciona a los candidatos más adecuados para la siguiente fase.

      +--------------------+
      |     Reclutador     |
      +---------+----------+
                |
                v
      +--------------------+
      |   Recibir CVs      |
      +--------------------+
                |
                v
      +--------------------+
      |    Evaluación IA   |
      +--------------------+
                |
                v
      +--------------------+
      | Generar Ranking    |
      +--------------------+
                |
                v
      +--------------------+
      | Seleccionar        |
      | Candidatos         |
      +--------------------+

**Caso de Uso 3: Colaboración y Comunicación en Tiempo Real**

Descripción:
El sistema permite que reclutadores y managers colaboren en tiempo real, compartiendo comentarios y calificaciones sobre cada candidato. Los reclutadores y managers pueden ver el estado de cada candidato en el proceso de selección y realizar anotaciones accesibles a todo el equipo.

Flujo del Caso de Uso:

El reclutador o manager accede a la lista de candidatos en proceso.
Revisa el perfil y la evaluación del candidato.
Añade comentarios o calificaciones sobre el candidato.
Los comentarios y calificaciones se muestran en tiempo real a todo el equipo.
Diagrama de Caso de Uso:


      +--------------------+
      | Reclutador/Manager |
      +---------+----------+
                |
                v
      +--------------------+
      | Acceder a Candidatos|
      +--------------------+
                |
                v
      +--------------------+
      | Revisar Perfil     |
      +--------------------+
                |
                v
      +--------------------+
      | Agregar Comentarios|
      | y Calificaciones   |
      +--------------------+
                |
                v
      +--------------------+
      | Visualizar en Tiempo|
      | Real               |
      +--------------------+

# ARTEFACTO 3

## DIAGRAMA ENTIDAD RELACIÓN

### Entidades y Atributos

**JobOffer (Oferta de Empleo)**
- **id (UUID)**: Identificador único de la oferta de empleo.
- **title (String)**: Título del puesto.
- **description (Text)**: Descripción detallada de la posición.
- **requirements (Text)**: Requisitos y cualificaciones requeridos.
- **salaryRange (String)**: Rango salarial.
- **location (String)**: Ubicación del puesto.
- **status (Enum: OPEN, CLOSED)**: Estado de la oferta (abierta o cerrada).
- **postedDate (Date)**: Fecha de publicación de la oferta.

**Relaciones**:
- Relación de uno a muchos con Application.
- Relación de muchos a uno con Recruiter.

**Application (Solicitud de Empleo)**
- **id (UUID)**: Identificador único de la solicitud.
- **submissionDate (Date)**: Fecha de envío de la solicitud.
- **status (Enum: APPLIED, SCREENING, INTERVIEWING, OFFERED, REJECTED)**: Estado actual del candidato en el proceso.
- **score (Float)**: Calificación del candidato, calculada por la IA.

**Relaciones**:
- Relación de muchos a uno con Candidate.
- Relación de muchos a uno con JobOffer.
- Relación de uno a muchos con Comment.

**Candidate (Candidato)**
- **id (UUID)**: Identificador único del candidato.
- **firstName (String)**: Nombre del candidato.
- **lastName (String)**: Apellido del candidato.
- **email (String)**: Correo electrónico.
- **phoneNumber (String)**: Número de teléfono.
- **resume (Text/Blob)**: Currículum vitae del candidato en formato de texto o archivo.

**Relaciones**:
- Relación de uno a muchos con Application.

**Comment (Comentario)**
- **id (UUID)**: Identificador único del comentario.
- **content (Text)**: Texto del comentario.
- **timestamp (DateTime)**: Fecha y hora en que se hizo el comentario.

**Relaciones**:
- Relación de muchos a uno con Application.
- Relación de muchos a uno con User (puede ser Recruiter o Manager).

**User (Usuario)**
- **id (UUID)**: Identificador único del usuario.
- **username (String)**: Nombre de usuario.
- **passwordHash (String)**: Hash de la contraseña para autenticación.
- **email (String)**: Correo electrónico.
- **role (Enum: RECRUITER, MANAGER)**: Rol del usuario en el sistema.

**Relaciones**:
- Relación de uno a muchos con Comment.

**Recruiter (Reclutador, subentidad de Usuario)**
- **id (UUID)**: Identificador único del reclutador (hereda de User).

**Relaciones**:
- Relación de uno a muchos con JobOffer.

**Manager (Gerente, subentidad de Usuario)**
- **id (UUID)**: Identificador único del gerente (hereda de User).

**Relaciones**:
- Relación de muchos a muchos con JobOffer (acceso para revisar y aprobar).

### Relaciones entre Entidades

**JobOffer y Application**:
- Relación uno a muchos, ya que cada oferta de empleo puede tener varias solicitudes asociadas.

**Application y Candidate**:
- Relación muchos a uno, ya que cada solicitud está asociada a un solo candidato, pero un candidato puede aplicar a múltiples ofertas.

**Application y Comment**:
- Relación uno a muchos, ya que cada solicitud puede tener múltiples comentarios de los reclutadores o managers.

**User y Comment**:
- Relación uno a muchos, donde un usuario (ya sea reclutador o gerente) puede hacer múltiples comentarios en diferentes solicitudes.

**JobOffer y Recruiter**:
- Relación muchos a uno, ya que un reclutador puede gestionar varias ofertas de empleo.

**JobOffer y Manager**:
- Relación muchos a muchos, dado que varios managers pueden revisar una oferta de empleo, y un manager puede tener acceso a múltiples ofertas.


El diagrama se encuentra en la siguiente ruta: /home/abelacco/33-ai4devs/AI4Devs-design-1/LTI-AAC/DER.png


# ARTEFACTO 4

1. Arquitectura General del Sistema
El sistema se basa en una arquitectura multicapa para separar responsabilidades y permitir una mejor mantenibilidad y escalabilidad. Las capas principales incluyen:

- **Capa de Presentación (Frontend)**: Donde los usuarios interactúan con el sistema a través de una interfaz web.
- **Capa de Lógica de Negocio (Backend)**: Donde se maneja toda la lógica de negocio y las reglas del sistema, con servicios de IA para procesamiento de currículums y puntuación de candidatos.
- **Capa de Persistencia (Base de Datos)**: Donde se almacenan y gestionan los datos de candidatos, solicitudes, ofertas de empleo, comentarios y usuarios.
- **Servicios Externos e Integración**: Incluye servicios de IA, integración con portales de empleo y sistemas de calendario.

2. Componentes Principales

- **Frontend (Interfaz de Usuario)**
  - **UI Web**: Aplicación web diseñada con componentes modernos (React, Angular o Vue) para facilitar la interacción de usuarios (reclutadores, managers) con el sistema.
  - **UX para Reclutamiento**: Funciones de búsqueda y filtros avanzados, pipeline visual de candidatos, calificaciones y comentarios en tiempo real.
  - **Interfaz de Colaboración en Tiempo Real**: Herramientas para la comunicación y colaboración entre reclutadores y managers.

- **API Gateway**
  - Gestiona todas las solicitudes entrantes y distribuye las peticiones al servicio correspondiente en la capa de backend. También maneja autenticación y autorización.

- **Servicios de Backend**
  - **Servicio de Gestión de Ofertas de Empleo**: Gestiona la creación, publicación y modificación de ofertas de empleo. Coordina con servicios externos para la publicación en diferentes portales.
  - **Servicio de Solicitudes de Empleo**: Maneja el proceso de creación y estado de las solicitudes de candidatos, gestionando la evaluación y clasificación.
  - **Servicio de Evaluación de Candidatos (IA)**: Realiza análisis de currículums y asigna puntuaciones a los candidatos. Este servicio utiliza modelos de IA para evaluar y calificar en función de palabras clave, experiencia y requisitos específicos.
  - **Servicio de Colaboración y Comentarios**: Permite a los usuarios agregar comentarios y calificaciones en tiempo real y gestiona la comunicación interna.
  - **Servicio de Notificaciones y Programación de Entrevistas**: Envía notificaciones a candidatos y usuarios internos y gestiona la programación de entrevistas mediante integración con calendarios externos.

- **Base de Datos**
  - **Base de Datos Relacional**: Almacena datos estructurados de candidatos, solicitudes, ofertas y usuarios. Un ejemplo de tecnología sería PostgreSQL o MySQL.
  - **Almacenamiento de Archivos**: Utiliza almacenamiento en la nube (como S3) para guardar currículums y otros documentos.

- **Servicios Externos e Integración**
  - **Servicios de IA**: Modelo de análisis de texto y currículums para evaluar candidatos.
  - **Integración con Portales de Empleo**: APIs de portales como LinkedIn y Indeed para publicar y actualizar ofertas de empleo.
  - **Integración de Calendarios**: Sincronización con Google Calendar o Microsoft Outlook para automatizar la programación de entrevistas.
  - **Servicios de Autenticación**: Integración con sistemas de autenticación como OAuth para manejar el acceso seguro.

**Resumen**
Este diseño de alto nivel organiza el sistema en componentes y servicios modulares que funcionan en conjunto para ofrecer una plataforma ATS completa y eficiente. La arquitectura multicapas facilita la escalabilidad y mantiene separadas las responsabilidades, asegurando que los servicios de backend, almacenamiento y frontend trabajen de manera coherente. Además, la integración de IA y servicios externos mejora la automatización y efectividad del sistema.

# ARTEFACTO 5

Diagrama C4 del Sistema ATS (Backend)
1. Nivel 1: Diagrama de Contexto
Este nivel muestra la vista general de los actores externos y el sistema LTI RecruitPro, y cómo interactúan entre sí.

plaintext
Copiar código
+----------------------+
|      Reclutador      |                       +---------------------------+
|  Usuario del sistema |                       |   Sistema de Calendarios  |
+----------------------+                       |  (Google Calendar, Outlook)|
            |                                   +---------------------------+
            |                                                ^
            v                                                |
+----------------------+       +----------------------+       |
|      LTI RecruitPro  | <----|      Candidato       |       |
|         (ATS)        |       | Usuario externo     |       |
+----------------------+       +----------------------+       |
            |                                                |
            v                                                |
+---------------------------+                       +------------------------+
|        Portales de        |                       |       Servicios de IA  |
|       Empleo Externos     |                       +------------------------+
+---------------------------+
Reclutador y Candidato son los usuarios principales que interactúan con el sistema LTI RecruitPro. El reclutador accede a través del frontend para gestionar ofertas de empleo y candidatos, mientras que el candidato puede enviar solicitudes.
El sistema LTI RecruitPro se integra con Servicios de IA (para evaluar currículums), Portales de Empleo Externos (para publicación de ofertas), y Sistemas de Calendario (para la programación de entrevistas).


2. Nivel 2: Diagrama de Contenedores
Aquí se detallan los contenedores principales dentro del sistema LTI RecruitPro, mostrando los servicios backend y cómo interactúan.

plaintext
Copiar código
+-----------------------+
|    UI Web (Frontend)  |
+-----------------------+
            |
            v
+-----------------------------+       +------------------------+
|        API Gateway          |       |   Sistema de IA Externo|
+-----------------------------+       +------------------------+
            |                                  ^
            v                                  |
+-----------------------------+       +------------------------+
|        Backend (ATS)        | <---->| Integración de Calendario|
+-----------------------------+       +------------------------+
|  - Servicio de Ofertas      |       |                        |
|  - Servicio de Solicitudes  |       |                        |
|  - Servicio de Evaluación   |       |                        |
|  - Servicio de Notificación |       +------------------------+
+-----------------------------+
            |
            v
+---------------------------+
|       Base de Datos       |
+---------------------------+
API Gateway: Punto de acceso que recibe todas las solicitudes desde el frontend y distribuye las peticiones a los servicios adecuados.
Backend (ATS): Contiene servicios específicos para gestionar ofertas, solicitudes, evaluación de candidatos y notificaciones.
Sistema de IA Externo: Interfaz con modelos de IA para evaluación automática de candidatos.
Integración de Calendario: Conexión con sistemas de calendario como Google Calendar o Outlook para automatizar la programación de entrevistas.
Base de Datos: Almacena toda la información relevante, incluidos los datos de candidatos, ofertas de trabajo y solicitudes.

3. Nivel 3: Diagrama de Componentes (Backend ATS)
A continuación, desglosamos el Backend en sus componentes para mostrar cómo se estructura internamente.

plaintext
Copiar código
+-----------------------------+
|         API Gateway         |
+-----------------------------+
            |
            v
+---------------------------------------------------------------+
|                         Backend ATS                           |
|---------------------------------------------------------------|
|  +------------------------+     +------------------------+    |
|  | Servicio de Ofertas    |     | Servicio de Solicitudes|    |
|  +------------------------+     +------------------------+    |
|  | - Crear Oferta         |     | - Crear Solicitud      |    |
|  | - Modificar Oferta     |     | - Actualizar Estado    |    |
|  | - Publicar Oferta      |     | - Obtener Solicitudes  |    |
|  +------------------------+     +------------------------+    |
|                                                               |
|  +------------------------+     +------------------------+    |
|  | Servicio de Evaluación |     | Servicio de Notificación|   |
|  +------------------------+     +------------------------+    |
|  | - Calificar Candidatos |     | - Notificar Reclutador |    |
|  | - IA para CVs          |     | - Notificar Candidato  |    |
|  +------------------------+     +------------------------+    |
+---------------------------------------------------------------+
            |
            v
+---------------------------+
|       Base de Datos       |
|---------------------------|
|  +---------------------+  |
|  | Tabla de Candidatos |  |
|  | Tabla de Solicitudes|  |
|  | Tabla de Ofertas    |  |
|  | Tabla de Usuarios   |  |
+-------------------------+  |
+---------------------------+
Servicio de Ofertas: Gestiona el ciclo de vida de una oferta de trabajo, desde su creación hasta su publicación y modificación. Se conecta con portales de empleo para publicar ofertas.
Servicio de Solicitudes: Administra las solicitudes de los candidatos y su estado a lo largo del proceso de selección. Proporciona métodos para crear, actualizar y recuperar solicitudes.
Servicio de Evaluación: Realiza la evaluación y calificación de candidatos. Utiliza IA para analizar los currículums y asignar una puntuación en función de los criterios de la oferta.
Servicio de Notificación: Envía notificaciones a candidatos y reclutadores en función de los eventos, como cambios de estado en el proceso de solicitud o confirmación de entrevistas.
Base de Datos: Almacena todas las entidades del sistema, incluidas tablas específicas para candidatos, solicitudes, ofertas y usuarios.


Explicación del Nivel 3 (Componentes)
API Gateway recibe solicitudes desde el frontend y direcciona estas peticiones a los servicios internos del backend.
Backend ATS contiene los componentes principales (servicios) que llevan a cabo la lógica del negocio:
Servicio de Ofertas: Facilita la gestión de las ofertas de empleo.
Servicio de Solicitudes: Administra las solicitudes y su progreso en el pipeline de reclutamiento.
Servicio de Evaluación: Conecta con la IA para calificar y ordenar a los candidatos según sus perfiles.
Servicio de Notificación: Gestiona todas las notificaciones relevantes para el proceso de contratación, tanto para candidatos como para reclutadores.
Base de Datos almacena toda la información estructurada y es el repositorio de los datos críticos del sistema.




