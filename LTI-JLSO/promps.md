# Prompts utilizados para el diseño del sistema ATS para LTI

Cada prompt va a estar enumerado según los puntos de solicitados para el diseño: 

    1. Descripción breve del software LTI, valor añadido y ventajas competitivas. Explicación de las funciones principales. Añadir un diagrama Lean Canvas para entender el modelo de negocio
    2. Descripción de los 3 casos de uso principales, con el diagrama asociado a cada uno
    3. Modelo de datos que cubra entidades, atributos (nombre y tipo) y relaciones
    4. Diseño del sistema a alto nivel, tanto explicado como diagrama adjunto
    5. Diagrama C4 que llegue en profundidad a uno de los componentes del sistema, el que prefieras


## Prompts
1. Eres un experto en producto, con experiencia en sistemas de gestión de candidatos, ATS (Applicant-Tracking System). Primero descríbeme que es un ATS y ¿Qué funcionalidades básicas tiene?. Descríbemelas en un listado, ordenado de mayor a menor prioridad

2. Eres un analista de software experto. Estoy construyendo un sistema de ATS. Enumera y describe brevemente los 3 casos de uso más importantes a implementar para lograr una funcionalidad básica y genera un diagrama mermeid para cada uno de los casos de uso.

3. Crea un Modelo de datos que cubra entidades, atributos (nombre y tipo) y relaciones, para el sistema ATS (Applicant-Tracking System). 
    Usa el formato plantuml para generar el modelo de datos

4. 
    4.1 Generate a microservice architecture for an online ATS (applicant-Tracking system) system:
        Each ms has its owm database
        Use slq databases
        Use aws as cloud provider
        Include load balancer
        Use cache like redis
        Use CDN
    
    4.2 Explícame el siguiente codigo de este diagrama de architectura del sistema ATS: title Online ATS Microservice Architecture

    ```Frontend [icon: monitor] {
    CDN [icon: aws-cloudfront]
    }

    Load Balancer [icon: aws-elb]

    // Microservices
    User Service [color: blue, icon: user] {
    User API [icon: aws-ec2, label: "API"] // entry point
    User DB [icon: aws-rds, label: "DB"]
    }

    Job Service [color: green, icon: briefcase] {
    Job API [icon: aws-ec2, label: "API"] // entry point
    Job DB [icon: aws-rds, label: "DB"]
    }

    Application Service [color: orange, icon: file-text] {
    Application API [icon: aws-ec2, label: "API"] // entry point
    Application DB [icon: aws-rds, label: "DB"]
    }

    // Shared Services
    Analytics Service [icon: bar-chart] {
    Analytics API [icon: aws-ec2, label: "API"] // entry point
    Analytics DB [icon: aws-rds, label: "DB"]
    }

    Cache [icon: aws-elasticache, label: "Redis"]

    // Connections
    CDN > Load Balancer
    Load Balancer > User API
    Load Balancer > Job API
    Load Balancer > Application API
    Load Balancer > Analytics API
    User API <> User DB
    Job API <> Job DB
    Application API <> Application DB
    Analytics API <> Analytics DB
    User API <> Cache
    Job API <> Cache
    Application API <> Cache


5. 
    5.1 Crea un system context diagram para un sistema ATS(Applicant-Tracking System)

    5.2 Crea un container diagram para un sistema ATS(Applicant-Tracking System)

    5.3 Has zoom in sobre el container "user service" y crea un diagrama de componentes. recuerda que estamos diagramando un sistema ATS

    5.4  Crea un diagrama uml en plantuml para las vista de code diagram para un sistema ATS, para el componente de user controller