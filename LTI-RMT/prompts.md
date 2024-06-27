### Prompt 1

Eres un experto en producto, con experiencia en ATS (Applicant-Tracking system)
¿Qué funcionalidades básicas tiene un ATS?
Descríbemelas en un listado, ordenado de mayor a menor prioridad. Aqui una imagen que describe que es un ATS @https://media1-production-mightynetworks.imgix.net/asset/62a578e5-90e4-40a1-a09f-c86209424fe1/1713970482103.png?ixlib=rails-4.2.0&fm=jpg&q=75&auto=format 

### Prompt 2

Me creas tu mismo el diagrama LEAN Canvas en mermaid y me lo adjuntas al LTI-RMT/README.md

### Prompt 3

Describe los 3 casos de uso principales, con el diagrama asociado a cada uno en mermaid

### Prompt 4

Ahora necesito el modelo de datos que cubra entidades, atributos (nombre y tipo) y relaciones

### Prompt 5

Puedes darmelo en ingles? A partir de ahora, todo lo relacionado con codigo o base de datos en inglés, la documentación en castellano como hasta ahora

### Prompt 6

Quiero que me expliques el diseño del sistema a alto nivel y que me lo diagramatices

### Prompt 7

Quiero que el diseño sea usando una arquitectura de microservicios, con buenas practicas de desarrollo de estos

### Propmt 8

I want to create a diagram based in this mermaid, using AWS technologies

graph TD
    subgraph Frontend
        A[Portal de Reclutadores]
        B[Portal de Candidatos]
    end

    subgraph API Gateway
        C[API Gateway]
    end

    subgraph Microservices
        D[Candidate Management Service]
        E[Job Posting Service]
        F[Interview Service]
        G[Notification Service]
        H[Analytics and Reporting Service]
    end

    subgraph Databases
        I[(Candidate DB)]
        J[(Job Posting DB)]
        K[(Interview DB)]
        L[(Notification DB)]
        M[(Analytics DB)]
    end

    subgraph External Services
        N[Job Platforms]
        O[Email Services]
        P[HRIS]
    end

    A -->|Requests| C
    B -->|Requests| C
    C -->|Routes| D
    C -->|Routes| E
    C -->|Routes| F
    C -->|Routes| G
    C -->|Routes| H
    D -->|CRUD Operations| I
    E -->|CRUD Operations| J
    F -->|CRUD Operations| K
    G -->|CRUD Operations| L
    H -->|CRUD Operations| M
    D -->|Integrations| N
    A -->|Solicitudes| C
    B -->|Solicitudes| C
    C -->|Operaciones| D
    D -->|Consultas y Actualizaciones| E
    D -->|Integraciones| F
    D -->|Notificaciones| G
    D -->|Sincronización| H

### Prompt 9

Quiero que me hagas un diagrama C4 el caso de uso 1