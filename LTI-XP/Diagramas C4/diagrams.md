## Diagrama C4 - Nivel 1: Contexto

**Este diagrama representa una vista de alto nivel del sistema ATS, mostrando cómo interactúan los usuarios (reclutadores y candidatos) con el sistema y sus principales servicios en AWS.**

@startuml
actor Recruiter as R
actor Candidate as C

package "ATS System" {
  rectangle "Job Service" as JobService
  rectangle "Application Service" as ApplicationService
  rectangle "Interview Service" as InterviewService
  rectangle "Notification Service" as NotificationService
  rectangle "User Management Service" as UserService
  rectangle "Audit & Activity Log Service" as AuditService
  cloud "ElastiCache" as Cache
  storage "AWS S3 (Document Storage)" as S3
  node "Load Balancer" as LB
}

R --> JobService : Creates Job Postings
C --> ApplicationService : Applies to Job Postings
R --> InterviewService : Manages Interviews
JobService --> Cache : Uses caching for jobs
ApplicationService --> S3 : Stores candidate documents
NotificationService --> R : Sends notifications
AuditService --> UserService : Tracks user actions
LB --> JobService : Routes traffic
@enduml



## Diagrama C4 - Nivel 2: Contenedores

**Este nivel muestra los contenedores individuales del sistema ATS y cómo interactúan a través de API Gateway y el Load Balancer. Cada microservicio tiene su propia base de datos y conecta al almacenamiento compartido de AWS S3 y ElastiCache.**

@startuml
actor Recruiter as R
actor Candidate as C

node "Load Balancer" as LB
node "API Gateway" as APIGW

package "ATS System" {
  node "Job Service" as JobService
  database "Job Database" as JobDB

  node "Application Service" as ApplicationService
  database "Application Database" as AppDB

  node "Interview Service" as InterviewService
  database "Interview Database" as IntDB

  node "Notification Service" as NotificationService
  database "Notification Database" as NotifDB

  node "User Management Service" as UserService
  database "User Database" as UserDB

  node "Audit & Activity Log Service" as AuditService
  database "Audit Database" as AuditDB

  cloud "ElastiCache" as Cache
  storage "AWS S3" as S3
}

R --> LB
C --> LB
LB --> APIGW
APIGW --> JobService : Job Management
APIGW --> ApplicationService : Application Management
APIGW --> InterviewService : Interview Management
APIGW --> NotificationService : Sends Notifications
APIGW --> UserService : User Authentication
APIGW --> AuditService : Logs Activity

JobService --> JobDB
ApplicationService --> AppDB
InterviewService --> IntDB
NotificationService --> NotifDB
UserService --> UserDB
AuditService --> AuditDB

JobService --> Cache : Caches frequently accessed jobs
ApplicationService --> S3 : Stores documents
@enduml


## Diagrama C4 - Nivel 3: Componentes
**Aquí se muestra la estructura interna de los principales microservicios. Por ejemplo, el Application Service y Interview Service manejan la lógica y almacenamiento de aplicaciones y entrevistas, y el Notification Service gestiona notificaciones de actualizaciones para reclutadores y candidatos.**

@startuml
package "Application Service" as ApplicationService {
  component "API Handler" as APIHandler_App
  component "Business Logic" as BusinessLogic_App
  component "Database Connector" as DBConnector_App
  database "Application Database" as AppDB
}

package "Interview Service" as InterviewService {
  component "API Handler" as APIHandler_Int
  component "Business Logic" as BusinessLogic_Int
  component "Database Connector" as DBConnector_Int
  database "Interview Database" as IntDB
}

package "Notification Service" as NotificationService {
  component "API Handler" as APIHandler_Notif
  component "Message Queue" as Queue_Notif
  component "Database Connector" as DBConnector_Notif
  database "Notification Database" as NotifDB
}

APIHandler_App --> BusinessLogic_App
BusinessLogic_App --> DBConnector_App
DBConnector_App --> AppDB

APIHandler_Int --> BusinessLogic_Int
BusinessLogic_Int --> DBConnector_Int
DBConnector_Int --> IntDB

APIHandler_Notif --> Queue_Notif
Queue_Notif --> DBConnector_Notif
DBConnector_Notif --> NotifDB
@enduml


## Diagrama unificado

@startuml
actor Recruiter as R
actor Candidate as C

node "Load Balancer" as LB
node "API Gateway" as APIGW

package "ATS System" {
  
  package "Job Service" as JobService {
    component "API Handler" as APIHandler_Job
    component "Business Logic" as BusinessLogic_Job
    component "Database Connector" as DBConnector_Job
    database "Job Database" as JobDB
  }
  
  package "Application Service" as ApplicationService {
    component "API Handler" as APIHandler_App
    component "Business Logic" as BusinessLogic_App
    component "Database Connector" as DBConnector_App
    database "Application Database" as AppDB
  }
  
  package "Interview Service" as InterviewService {
    component "API Handler" as APIHandler_Int
    component "Business Logic" as BusinessLogic_Int
    component "Database Connector" as DBConnector_Int
    database "Interview Database" as IntDB
  }
  
  package "Notification Service" as NotificationService {
    component "API Handler" as APIHandler_Notif
    component "Message Queue" as Queue_Notif
    component "Database Connector" as DBConnector_Notif
    database "Notification Database" as NotifDB
  }

  package "User Management Service" as UserService {
    component "API Handler" as APIHandler_User
    component "Business Logic" as BusinessLogic_User
    component "Database Connector" as DBConnector_User
    database "User Database" as UserDB
  }

  package "Audit & Activity Log Service" as AuditService {
    component "API Handler" as APIHandler_Audit
    component "Business Logic" as BusinessLogic_Audit
    component "Database Connector" as DBConnector_Audit
    database "Audit Database" as AuditDB
  }

  cloud "ElastiCache" as Cache
  storage "AWS S3 (Document Storage)" as S3
}

R --> LB : Accesses ATS
C --> LB : Accesses ATS
LB --> APIGW : Routes traffic to ATS services

APIGW --> APIHandler_Job : Job Management
APIGW --> APIHandler_App : Application Management
APIGW --> APIHandler_Int : Interview Management
APIGW --> APIHandler_Notif : Notification Management
APIGW --> APIHandler_User : User Management
APIGW --> APIHandler_Audit : Logs Activity

APIHandler_Job --> BusinessLogic_Job
BusinessLogic_Job --> DBConnector_Job
DBConnector_Job --> JobDB

APIHandler_App --> BusinessLogic_App
BusinessLogic_App --> DBConnector_App
DBConnector_App --> AppDB
BusinessLogic_App --> S3 : Stores candidate documents

APIHandler_Int --> BusinessLogic_Int
BusinessLogic_Int --> DBConnector_Int
DBConnector_Int --> IntDB

APIHandler_Notif --> Queue_Notif
Queue_Notif --> DBConnector_Notif
DBConnector_Notif --> NotifDB

APIHandler_User --> BusinessLogic_User
BusinessLogic_User --> DBConnector_User
DBConnector_User --> UserDB

APIHandler_Audit --> BusinessLogic_Audit
BusinessLogic_Audit --> DBConnector_Audit
DBConnector_Audit --> AuditDB

JobService --> Cache : Caches frequently accessed jobs
@enduml

