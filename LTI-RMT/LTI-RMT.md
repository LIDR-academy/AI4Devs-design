# LTI - Applicant Tracking System

## Descripción Breve del Software LTI
LTI es un sistema de seguimiento de candidatos (ATS) diseñado para revolucionar el proceso de reclutamiento. Nuestro objetivo es aumentar la eficiencia de los departamentos de recursos humanos, mejorar la colaboración en tiempo real entre reclutadores y managers, y automatizar tareas clave con la asistencia de inteligencia artificial.

## Valor Añadido
LTI ofrece una solución integral que no solo gestiona el proceso de reclutamiento, sino que también proporciona herramientas avanzadas de análisis y automatización. A diferencia de otras soluciones en el mercado, LTI se enfoca en la experiencia del usuario, tanto para los reclutadores como para los candidatos, asegurando un proceso de selección más fluido y eficiente.

## Ventajas Competitivas
- **Automatización Avanzada**: LTI utiliza inteligencia artificial para automatizar tareas repetitivas, permitiendo a los reclutadores centrarse en actividades estratégicas.
- **Colaboración en Tiempo Real**: Herramientas integradas para la colaboración entre equipos, facilitando la comunicación y la toma de decisiones.
- **Análisis y Reportes Detallados**: Generación de informes y análisis detallados para medir la eficiencia del proceso de reclutamiento.
- **Integración Sencilla**: Compatible con múltiples plataformas y sistemas de recursos humanos existentes.
- **Experiencia del Candidato**: Portales y herramientas diseñadas para mejorar la experiencia del candidato durante el proceso de selección.

## Funciones Principales
1. **Gestión de Candidatos**:
   - Almacenamiento y organización de perfiles de candidatos.
   - Seguimiento del estado de cada candidato en el proceso de selección.

2. **Publicación de Ofertas de Trabajo**:
   - Creación y publicación de ofertas de trabajo en múltiples plataformas y portales de empleo.
   - Integración con redes sociales y sitios web de la empresa.

3. **Filtrado y Clasificación de Candidatos**:
   - Herramientas de búsqueda y filtrado para identificar candidatos adecuados.
   - Clasificación automática de candidatos según criterios predefinidos.

4. **Comunicación con Candidatos**:
   - Envío de correos electrónicos y mensajes automáticos a los candidatos.
   - Programación de entrevistas y recordatorios.

5. **Colaboración del Equipo de Reclutamiento**:
   - Herramientas para la colaboración y comunicación entre los miembros del equipo de reclutamiento.
   - Asignación de tareas y seguimiento del progreso.

6. **Integración con Otros Sistemas**:
   - Integración con sistemas de recursos humanos (HRIS) y otras herramientas de gestión.
   - Sincronización con calendarios y sistemas de correo electrónico.

7. **Análisis y Reportes**:
   - Generación de informes y análisis sobre el proceso de selección.
   - Métricas de rendimiento y eficiencia del reclutamiento.

8. **Cumplimiento Legal y Seguridad**:
   - Almacenamiento seguro de datos personales de los candidatos.
   - Cumplimiento con regulaciones de privacidad y protección de datos.

9. **Experiencia del Candidato**:
   - Portales de candidatos para seguimiento de su aplicación.
   - Formularios y encuestas de satisfacción.

10. **Automatización de Procesos**:
    - Automatización de tareas repetitivas y administrativas.
    - Flujos de trabajo personalizados para diferentes tipos de procesos de selección.

## Diagrama Lean Canvas
```mermaid
graph TD
    A[Problemas] -->|1| B[Soluciones]
    A -->|2| C[Propuestas de Valor]
    A -->|3| D[Ventajas Competitivas]
    B -->|4| E[Segmentos de Clientes]
    C -->|5| F[Canales]
    D -->|6| G[Estructura de Costos]
    E -->|7| H[Flujos de Ingresos]
    F -->|8| I[Indicadores Clave]
    G -->|9| J[Recursos Clave]
    H -->|10| K[Actividades Clave]
    I -->|11| L[Socios Clave]
```

## Casos de Uso Principales

### Caso de Uso 1: Publicación de Ofertas de Trabajo
**Descripción**: El reclutador crea y publica una oferta de trabajo en múltiples plataformas y portales de empleo.

```mermaid
sequenceDiagram
    participant R as Reclutador
    participant ATS as Sistema ATS
    participant P as Plataformas de Empleo

    R->>ATS: Crear oferta de trabajo
    ATS-->>R: Confirmación de creación
    ATS->>P: Publicar oferta de trabajo
    P-->>ATS: Confirmación de publicación
    ATS-->>R: Notificación de publicación
```

### Caso de Uso 2: Filtrado y Clasificación de Candidatos
**Descripción**: El sistema filtra y clasifica automáticamente a los candidatos según criterios predefinidos.

```mermaid
sequenceDiagram
    participant C as Candidato
    participant ATS as Sistema ATS
    participant R as Reclutador

    C->>ATS: Enviar solicitud
    ATS-->>C: Confirmación de recepción
    ATS->>ATS: Filtrar y clasificar candidatos
    ATS-->>R: Notificación de candidatos clasificados
```

### Caso de Uso 3: Programación de Entrevistas
**Descripción**: El reclutador programa entrevistas con los candidatos seleccionados y envía recordatorios automáticos.

```mermaid
sequenceDiagram
    participant R as Reclutador
    participant ATS as Sistema ATS
    participant C as Candidato

    R->>ATS: Programar entrevista
    ATS-->>R: Confirmación de programación
    ATS->>C: Enviar invitación a entrevista
    C-->>ATS: Confirmación de asistencia
    ATS-->>R: Notificación de confirmación
    ATS->>C: Enviar recordatorio automático
```

## Modelo de Datos

### Entidades y Atributos

#### Candidate
- **ID**: int
- **Name**: string
- **Email**: string
- **Phone**: string
- **CV**: string (URL to the file)
- **Status**: string (e.g., "Applied", "In Process", "Rejected", "Hired")

#### Job Offer
- **ID**: int
- **Title**: string
- **Description**: string
- **Publication Date**: date
- **Status**: string (e.g., "Open", "Closed")

#### Interview
- **ID**: int
- **CandidateID**: int (relation to Candidate)
- **DateTime**: datetime
- **RecruiterID**: int (relation to Recruiter)
- **Status**: string (e.g., "Scheduled", "Completed", "Cancelled")

#### Recruiter
- **ID**: int
- **Name**: string
- **Email**: string
- **Phone**: string

### Relationships

- **Candidate** applies to **Job Offer** (1:N)
- **Interview** is associated with **Candidate** (1:N)
- **Interview** is associated with **Recruiter** (1:N)
- **Recruiter** publishes **Job Offer** (1:N)

## Entity-Relationship Diagram (ERD)
```mermaid
erDiagram
    CANDIDATE {
        int ID
        string Name
        string Email
        string Phone
        string CV
        string Status
    }
    JOB_OFFER {
        int ID
        string Title
        string Description
        date Publication_Date
        string Status
    }
    INTERVIEW {
        int ID
        int CandidateID
        datetime DateTime
        int RecruiterID
        string Status
    }
    RECRUITER {
        int ID
        string Name
        string Email
        string Phone
    }

    CANDIDATE ||--o{ JOB_OFFER: applies_to
    CANDIDATE ||--o{ INTERVIEW: has
    RECRUITER ||--o{ INTERVIEW: schedules
    RECRUITER ||--o{ JOB_OFFER: publishes
```

## Diseño del Sistema a Alto Nivel

### Descripción
El sistema LTI (Applicant Tracking System) está diseñado utilizando una arquitectura de microservicios para gestionar el proceso de reclutamiento de manera eficiente y escalable. A continuación se describen los componentes principales del sistema y sus interacciones:

1. **Frontend**: La interfaz de usuario que interactúa con los reclutadores y candidatos. Incluye:
   - **Portal de Reclutadores**: Donde los reclutadores pueden publicar ofertas de trabajo, gestionar candidatos, programar entrevistas y colaborar con otros miembros del equipo.
   - **Portal de Candidatos**: Donde los candidatos pueden buscar y aplicar a ofertas de trabajo, y seguir el estado de sus aplicaciones.

2. **Microservicios**: Cada microservicio maneja una funcionalidad específica del sistema. Incluye:
   - **Servicio de Gestión de Candidatos**: Maneja la creación, actualización y seguimiento de candidatos.
   - **Servicio de Publicación de Ofertas**: Maneja la creación y publicación de ofertas de trabajo.
   - **Servicio de Entrevistas**: Maneja la programación y seguimiento de entrevistas.
   - **Servicio de Notificaciones**: Maneja el envío de correos electrónicos y notificaciones.
   - **Servicio de Análisis y Reportes**: Genera informes y análisis sobre el proceso de selección.

3. **API Gateway**: Actúa como un punto de entrada único para todas las solicitudes del frontend, redirigiéndolas a los microservicios correspondientes.

4. **Base de Datos**: Cada microservicio tiene su propia base de datos para asegurar la independencia y escalabilidad.

5. **Servicios Externos**: Integraciones con servicios de terceros, como plataformas de empleo, servicios de correo electrónico, y sistemas de recursos humanos (HRIS).

### Diagrama de Alto Nivel
![Diagrama de Alto Nivel](diagram.png)

## Diagrama C4 para el Caso de Uso 1: Publicación de Ofertas de Trabajo

### Diagrama de Contexto
```mermaid
graph TD
    User[Reclutador] -->|Crea Oferta de Trabajo| APIGateway
    APIGateway -->|Redirige Solicitud| JobPostingService
    JobPostingService -->|Almacena Oferta de Trabajo| JobPostingDB
    JobPostingService -->|Publica Oferta de Trabajo| JobPlatforms
```

### Diagrama de Contenedores
```mermaid
graph TD
    subgraph Frontend
        User[Reclutador]
    end

    subgraph API Gateway
        APIGateway
    end

    subgraph Microservicios
        JobPostingService
    end

    subgraph Bases de Datos
        JobPostingDB[(Base de Datos de Ofertas de Trabajo)]
    end

    subgraph Servicios Externos
        JobPlatforms[Plataformas de Empleo]
    end

    User -->|Crea Oferta de Trabajo| APIGateway
    APIGateway -->|Redirige Solicitud| JobPostingService
    JobPostingService -->|Almacena Oferta de Trabajo| JobPostingDB
    JobPostingService -->|Publica Oferta de Trabajo| JobPlatforms
```

### Diagrama de Componentes para el Servicio de Publicación de Ofertas
```mermaid
graph TD
    subgraph JobPostingService
        Controller[Controlador de Publicación de Ofertas]
        Service[Servicio de Publicación de Ofertas]
        Repository[Repositorio de Publicación de Ofertas]
    end

    Controller -->|Recibe Solicitud| Service
    Service -->|Interactúa con| Repository
    Repository -->|Almacena Oferta de Trabajo| JobPostingDB[(Base de Datos de Ofertas de Trabajo)]
    Service -->|Publica Oferta de Trabajo| JobPlatforms[Plataformas de Empleo]
```

### Diagrama de Código para el Servicio de Publicación de Ofertas
```mermaid
classDiagram
    class JobPostingController {
        +createJobOffer()
    }

    class JobPostingService {
        +createJobOffer()
    }

    class JobPostingRepository {
        +save()
    }

    JobPostingController --> JobPostingService
    JobPostingService --> JobPostingRepository
```