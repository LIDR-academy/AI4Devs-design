# Caso de Uso 1: Creación y Publicación de Ofertas de Trabajo

Resumen de la funcionalidad: Permite a los reclutadores crear descripciones de puestos de trabajo, definir requisitos específicos y publicarlos en múltiples plataformas (job boards, redes sociales, sitio web).

**Alcance:** Desde la creación de una nueva oferta hasta su publicación en los canales seleccionados.
**Problemas a resolver:**
Facilitar la creación centralizada de ofertas.
Asegurar la correcta difusión de las vacantes en múltiples plataformas sin duplicación de esfuerzos.


## Diagrama

@startuml
actor Reclutador
actor PlataformaExterna as Plataforma

Reclutador -> ATS : Crear nueva oferta de trabajo
ATS -> Reclutador : Solicitar detalles del puesto
Reclutador -> ATS : Proveer detalles del puesto
ATS -> Reclutador : Confirmar detalles de la oferta
Reclutador -> ATS : Confirmar publicación
ATS -> Plataforma : Publicar oferta en job boards, redes sociales, sitio web
Plataforma --> ATS : Confirmación de publicación
ATS --> Reclutador : Notificación de publicación exitosa
@enduml

# Caso de Uso 2: Revisión y Filtro de Candidatos

**Resumen de la funcionalidad:**Permite a los reclutadores revisar las aplicaciones, filtrar candidatos según criterios definidos (experiencia, habilidades) y avanzar solo con los perfiles más relevantes.

**Alcance:** Desde la recepción de aplicaciones hasta la preselección de candidatos.

**Problemas a resolver:**
Reducir el tiempo de revisión de aplicaciones mediante filtros avanzados.
Priorizar candidatos que cumplen con los requisitos para una selección eficiente.

## Diagrama
@startuml
actor Reclutador

Reclutador -> ATS : Revisar aplicaciones
ATS -> ATS : Filtrar candidatos según criterios (experiencia, habilidades)
ATS -> Reclutador : Mostrar candidatos filtrados
Reclutador -> ATS : Seleccionar candidatos relevantes
ATS -> Reclutador : Marcar candidatos seleccionados para la siguiente etapa
@enduml


# Caso de Uso 3: Gestión de Entrevistas

Resumen de la funcionalidad: Coordina y gestiona las entrevistas entre candidatos y reclutadores, incluyendo la programación automática, envío de recordatorios y reprogramación si es necesario.

**Alcance:** Desde la programación de entrevistas hasta el seguimiento y recordatorios.

**Problemas a resolver:**
Simplificar la coordinación de horarios entre múltiples participantes.
Minimizar cancelaciones y olvidos mediante recordatorios automáticos.

## Diagrama 

@startuml
actor Reclutador
actor Candidato

Reclutador -> ATS : Programar entrevista
ATS -> Candidato : Enviar invitación a entrevista
Candidato --> ATS : Confirmar disponibilidad
ATS -> Reclutador : Notificar confirmación
ATS -> Candidato : Enviar recordatorio de entrevista
ATS -> Reclutador : Enviar recordatorio de entrevista
Reclutador -> Candidato : Realizar entrevista
@enduml

### Diagrama completo

@startuml
actor Reclutador
actor Candidato
actor PlataformaExterna as Plataforma

Reclutador -> ATS : Crear nueva oferta de trabajo
ATS -> Reclutador : Solicitar detalles del puesto
Reclutador -> ATS : Proveer detalles del puesto
ATS -> Reclutador : Confirmar detalles de la oferta
Reclutador -> ATS : Confirmar publicación
ATS -> Plataforma : Publicar oferta en job boards, redes sociales, sitio web
Plataforma --> ATS : Confirmación de publicación
ATS --> Reclutador : Notificación de publicación exitosa

== Revisión y Filtro de Candidatos ==
Candidato -> ATS : Enviar aplicación
ATS -> Reclutador : Notificación de nueva aplicación
Reclutador -> ATS : Revisar aplicaciones
ATS -> ATS : Filtrar candidatos según criterios (experiencia, habilidades)
ATS -> Reclutador : Mostrar candidatos filtrados
Reclutador -> ATS : Seleccionar candidatos relevantes
ATS -> Reclutador : Marcar candidatos seleccionados para la siguiente etapa

== Gestión de Entrevistas ==
Reclutador -> ATS : Programar entrevista con candidato seleccionado
ATS -> Candidato : Enviar invitación a entrevista
Candidato --> ATS : Confirmar disponibilidad
ATS -> Reclutador : Notificar confirmación de entrevista
ATS -> Candidato : Enviar recordatorio de entrevista
ATS -> Reclutador : Enviar recordatorio de entrevista
Reclutador -> Candidato : Realizar entrevista
@enduml
