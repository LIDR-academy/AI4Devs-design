# Entidades y relaciones

## JobPosting (Publicación de Oferta)
****Descripción::** Representa cada puesto de trabajo creado y publicado en el sistema. Incluye toda la información necesaria para que los candidatos puedan entender la oferta y postularse.
**Campos Esenciales:**
id (UUID): Identificador único de la oferta.
title (String): Título del puesto.
description (Text): Descripción completa del trabajo y responsabilidades.
requirements (Text): Requisitos necesarios para el puesto (habilidades, experiencia).
status (Enum): Estado de la oferta (Abierta, Cerrada, Archivada).
created_at (Timestamp): Fecha de creación de la oferta.
updated_at (Timestamp): Última actualización de la oferta.
****Relaciones:**
1 a N con Application: Cada oferta puede recibir múltiples aplicaciones.
1 a N con Interview: Una oferta puede tener varias entrevistas asociadas a sus candidatos.

## 2. Application (Aplicación)

****Descripción::** Representa la postulación de un candidato a una oferta de trabajo específica. Contiene los detalles del candidato y su estatus en el proceso de selección.
**Campos Esenciales:**
id (UUID): Identificador único de la aplicación.
job_posting_id (UUID, Foreign Key): Referencia a la oferta a la cual aplica el candidato.
candidate_name (String): Nombre del candidato.
candidate_email (String): Email del candidato.
resume_url (String): Enlace al CV del candidato (si está subido en el sistema).
status (Enum): Estado de la aplicación (Pendiente, Preseleccionado, Entrevistado, Contratado, Rechazado).
submitted_at (Timestamp): Fecha de presentación de la aplicación.
****Relaciones:**
N a 1 con JobPosting: Cada aplicación está asociada a una única oferta de trabajo.
1 a N con Interview: Una aplicación puede tener múltiples entrevistas agendadas.


## 3. Interview (Entrevista)
****Descripción::** Representa las entrevistas programadas para cada candidato en el proceso de selección, vinculadas a una aplicación y una oferta de trabajo específica.
**Campos Esenciales:**
id (UUID): Identificador único de la entrevista.
application_id (UUID, Foreign Key): Referencia a la aplicación para la cual se agenda la entrevista.
job_posting_id (UUID, Foreign Key): Referencia a la oferta de trabajo.
scheduled_date (Timestamp): Fecha y hora programada de la entrevista.
interviewer_name (String): Nombre del entrevistador asignado.
status (Enum): Estado de la entrevista (Pendiente, Completada, Cancelada).
feedback (Text, opcional): Comentarios o evaluación del entrevistador.
****Relaciones:**
N a 1 con Application: Cada entrevista está vinculada a una aplicación específica.
N a 1 con JobPosting: Cada entrevista está vinculada a una oferta específica para contexto y referencia.

# Relación General entre Entidades
JobPosting tiene una relación 1 a N con Application: una oferta puede tener múltiples aplicaciones.
Application tiene una relación 1 a N con Interview: una aplicación puede tener múltiples entrevistas.
JobPosting también está relacionado indirectamente con Interview a través de Application para dar contexto a la entrevista en relación con el puesto.

## Resumen de Relación entre Entidades
JobPosting ← 1 a N → Application
Application ← 1 a N → Interview
JobPosting ← 1 a N (indirecta) → Interview a través de Application

Estas tres entidades constituyen el núcleo del modelo de datos del ATS, capturando las relaciones principales y flujos críticos desde la publicación de una oferta hasta la gestión de entrevistas. ¿Te gustaría que expandamos en algún detalle adicional o en las relaciones entre estas entidades?


## Diagrama mermaid
erDiagram
    JobPosting {
        UUID id
        String title
        Text description
        Text requirements
        Enum status
        Timestamp created_at
        Timestamp updated_at
    }
    
    Application {
        UUID id
        UUID job_posting_id
        String candidate_name
        String candidate_email
        String resume_url
        Enum status
        Timestamp submitted_at
    }
    
    Interview {
        UUID id
        UUID application_id
        UUID job_posting_id
        Timestamp scheduled_date
        String interviewer_name
        Enum status
        Text feedback
    }
    
    JobPosting ||--o{ Application : "1 a N"
    Application ||--o{ Interview : "1 a N"
    JobPosting ||--o{ Interview : "1 a N (indirecta)"


-----

# Entidades y relaciones adicionales
## 1. User (Usuario)
****Descripción::** Representa a los distintos usuarios del sistema (reclutadores, administradores, y otros roles) que interactúan con el ATS.
**Campos Básicos:**
id (UUID): Identificador único del usuario.
name (String): Nombre completo del usuario.
email (String): Correo electrónico del usuario, utilizado para el inicio de sesión.
role (Enum): Rol del usuario (Admin, Reclutador, Entrevistador).
password_hash (String): Hash de la contraseña para autenticación.
created_at (Timestamp): Fecha de creación del usuario.
**Relaciones:**
1 a N con JobPosting: Los reclutadores pueden ser responsables de varias ofertas de trabajo.
1 a N con Interview: Los entrevistadores pueden estar asignados a múltiples entrevistas.
## 2. Candidate (Candidato)
**Descripción::** Representa a los candidatos que aplican a las ofertas de trabajo y permite centralizar su información de perfil y aplicaciones.
**Campos Básicos:**
id (UUID): Identificador único del candidato.
name (String): Nombre completo del candidato.
email (String): Correo electrónico del candidato.
phone_number (String): Número de teléfono del candidato.
address (String): Dirección de residencia.
created_at (Timestamp): Fecha en la que el candidato fue añadido al sistema.
**Relaciones:**
1 a N con Application: Un candidato puede tener varias aplicaciones para diferentes ofertas.

## 3. Document (Documento)
**Descripción::** Representa los documentos adicionales subidos por candidatos o reclutadores, como certificados, cartas de recomendación, entre otros.
**Campos Básicos:**
id (UUID): Identificador único del documento.
candidate_id (UUID, Foreign Key): Referencia al candidato al que pertenece el documento.
url (String): Enlace al documento almacenado.
document_type (Enum): Tipo de documento (CV, Certificado, Carta de Recomendación).
uploaded_at (Timestamp): Fecha de carga del documento.
**Relaciones:**
N a 1 con Candidate: Cada documento está asociado con un único candidato.

## 4. Evaluation (Evaluación)
**Descripción::** Almacena las evaluaciones y feedback que los entrevistadores dan después de cada entrevista, permitiendo un análisis estructurado de cada candidato.
**Campos Básicos:**
id (UUID): Identificador único de la evaluación.
interview_id (UUID, Foreign Key): Referencia a la entrevista evaluada.
interviewer_id (UUID, Foreign Key): Referencia al entrevistador que realiza la evaluación.
rating (Integer): Puntuación del candidato en la entrevista.
comments (Text): Comentarios adicionales del entrevistador.
created_at (Timestamp): Fecha en que se realizó la evaluación.
**Relaciones:**
N a 1 con Interview: Cada evaluación está asociada con una entrevista específica.
N a 1 con User: El entrevistador que realiza la evaluación.

## 5. Notification (Notificación)
**Descripción::** Registra notificaciones que se envían a los usuarios para mantenerlos informados de actualizaciones importantes en el sistema (nueva aplicación, recordatorio de entrevista).
**Campos Básicos:**
id (UUID): Identificador único de la notificación.
user_id (UUID, Foreign Key): Referencia al usuario que recibe la notificación.
message (Text): Mensaje de la notificación.
type (Enum): Tipo de notificación (Nueva aplicación, Recordatorio, Actualización).
read (Boolean): Estado de la notificación (leída o no leída).
created_at (Timestamp): Fecha de creación de la notificación.
**Relaciones:**
N a 1 con User: Cada notificación está dirigida a un usuario específico.

## 6. ActivityLog (Registro de Actividad)
**Descripción::** Guarda un historial de las acciones realizadas por los usuarios en el sistema, útil para auditoría y seguimiento de cambios.
**Campos Básicos:**
id (UUID): Identificador único del registro de actividad.
user_id (UUID, Foreign Key): Referencia al usuario que realizó la acción.
action (String): Descripción de la acción (Ej. "Creó nueva oferta", "Actualizó estado de aplicación").
timestamp (Timestamp): Fecha y hora en que se realizó la acción.
**Relaciones:**
N a 1 con User: Cada registro de actividad está asociado con un usuario específico.


## Relación General entre las Entidades Nuevas y las Principales
User interactúa con JobPosting, Interview, ActivityLog, y Notification.
Candidate centraliza la información de cada persona que aplica, relacionándose con Application y Document.
Document almacena documentos adicionales para Candidate.
Evaluation permite registrar el feedback de una Interview, enriqueciendo el proceso de selección.
Notification mantiene informados a los Users sobre eventos importantes en el sistema.
ActivityLog permite rastrear acciones de cada User para fines de auditoría y seguimiento.


# Diagrama Mermaid

erDiagram
    JobPosting {
        UUID id
        String title
        Text description
        Text requirements
        Enum status
        Timestamp created_at
        Timestamp updated_at
    }
    
    Application {
        UUID id
        UUID job_posting_id
        UUID candidate_id
        Enum status
        Timestamp submitted_at
    }
    
    Interview {
        UUID id
        UUID application_id
        UUID job_posting_id
        Timestamp scheduled_date
        String interviewer_name
        Enum status
        Text feedback
    }
    
    User {
        UUID id
        String name
        String email
        Enum role
        String password_hash
        Timestamp created_at
    }
    
    Candidate {
        UUID id
        String name
        String email
        String phone_number
        String address
        Timestamp created_at
    }
    
    Document {
        UUID id
        UUID candidate_id
        String url
        Enum document_type
        Timestamp uploaded_at
    }
    
    Evaluation {
        UUID id
        UUID interview_id
        UUID interviewer_id
        Integer rating
        Text comments
        Timestamp created_at
    }
    
    Notification {
        UUID id
        UUID user_id
        Text message
        Enum type
        Boolean read
        Timestamp created_at
    }
    
    ActivityLog {
        UUID id
        UUID user_id
        String action
        Timestamp timestamp
    }

    %% Relaciones principales
    JobPosting ||--o{ Application : "1 a N"
    Application ||--o{ Interview : "1 a N"
    JobPosting ||--o{ Interview : "1 a N (indirecta)"

    %% Relaciones con nuevas entidades
    User ||--o{ JobPosting : "1 a N"
    User ||--o{ Interview : "1 a N"
    User ||--o{ Notification : "1 a N"
    User ||--o{ ActivityLog : "1 a N"
    Candidate ||--o{ Application : "1 a N"
    Candidate ||--o{ Document : "1 a N"
    Interview ||--o{ Evaluation : "1 a N"
