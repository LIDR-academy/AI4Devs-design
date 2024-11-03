# USER STORIES

# Flujo 1: Creación y Publicación de Ofertas de Trabajo

## 1.1 Reclutador
- **User Story**: Como reclutador, quiero crear y publicar una oferta de trabajo para atraer candidatos relevantes y cubrir la vacante de manera eficiente.
- **Descripción**: Permite al reclutador crear, editar y publicar ofertas de trabajo en múltiples plataformas desde un solo lugar.
- **Criterios de Aceptación**:
  - Dado que soy un reclutador en el sistema, cuando accedo a la sección de creación de ofertas de trabajo, entonces puedo ver un formulario para ingresar los detalles de la oferta.
  - Dado que he completado los campos requeridos del formulario, cuando guardo la oferta, entonces esta se almacena en el sistema y queda lista para publicación.
  - Dado que la oferta está lista para publicarse, cuando selecciono las plataformas deseadas, entonces la oferta se distribuye y está visible en dichas plataformas.
- **Notas adicionales**:
  - Los campos requeridos incluyen título, descripción, requisitos y tipo de empleo.
  - La oferta debe ser editable hasta el momento de su publicación.
- **Tareas**:
  - Diseñar el formulario de creación de ofertas.
  - Implementar la lógica de guardado y edición.
  - Integrar con plataformas externas para la publicación.

## 1.2 Administrador
- **User Story**: Como administrador, quiero revisar y aprobar ofertas de trabajo antes de su publicación para asegurar que cumplan con las políticas de la empresa.
- **Descripción**: El administrador puede revisar, aprobar o rechazar las ofertas de trabajo creadas por los reclutadores.
- **Criterios de Aceptación**:
  - Dado que el reclutador envió una oferta para su publicación, cuando el administrador accede a la sección de revisión, entonces puede ver los detalles completos de la oferta.
  - Dado que el administrador revisa una oferta, cuando aprueba la publicación, entonces la oferta se distribuye a las plataformas seleccionadas.
  - Dado que el administrador rechaza una oferta, cuando deja comentarios, entonces el reclutador puede ver estos comentarios y hacer los ajustes necesarios.
- **Notas adicionales**:
  - La revisión y aprobación son necesarias para ofertas de trabajo con ciertas características según la política de la empresa.
- **Tareas**:
  - Crear interfaz de revisión para administradores.
  - Implementar lógica de aprobación y rechazo con comentarios.
  - Notificar al reclutador sobre el estado de la aprobación.

# Flujo 2: Recepción y Seguimiento de Aplicaciones

## 2.1 Reclutador
- **User Story**: Como reclutador, quiero hacer seguimiento de las aplicaciones recibidas para mantener un control sobre el proceso de selección.
- **Descripción**: Centraliza las aplicaciones y permite al reclutador organizar y visualizar el estado de cada solicitud.
- **Criterios de Aceptación**:
  - Dado que la oferta está publicada, cuando un candidato envía su solicitud, entonces esta se muestra en la lista de aplicaciones del reclutador.
  - Dado que reviso una aplicación, cuando actualizo el estado a "En Revisión", entonces el sistema registra el cambio y notifica al candidato.
- **Notas adicionales**:
  - El reclutador debe poder etiquetar las aplicaciones y añadir notas.
- **Tareas**:
  - Configurar la vista de seguimiento de aplicaciones.
  - Añadir funcionalidad de cambio de estado.
  - Implementar notificaciones automáticas para candidatos.

## 2.2 Candidato
- **User Story**: Como candidato, quiero ver el estado de mi aplicación para entender en qué etapa del proceso me encuentro.
- **Descripción**: El candidato puede consultar el estado de sus aplicaciones, proporcionando transparencia en el proceso.
- **Criterios de Aceptación**:
  - Dado que el candidato ha enviado su solicitud, cuando accede a su perfil, entonces puede ver el estado actual de su aplicación.
  - Dado que el reclutador cambia el estado de la aplicación, cuando se actualiza, entonces el candidato recibe una notificación con el nuevo estado.
- **Notas adicionales**:
  - Los candidatos deben poder ver un historial de cambios en el estado de su solicitud.
- **Tareas**:
  - Crear una vista de estado en el perfil del candidato.
  - Implementar notificaciones automáticas de estado.
  - Configurar el historial de actualizaciones.

# Flujo 3: Revisión y Filtro de Candidatos

## 3.1 Reclutador
- **User Story**: Como reclutador, quiero filtrar y revisar las aplicaciones por habilidades y experiencia para enfocarme en los candidatos más calificados.
- **Descripción**: Permite al reclutador aplicar filtros específicos para reducir el tiempo de selección.
- **Criterios de Aceptación**:
  - Dado que existen varias aplicaciones, cuando aplico filtros por habilidades o experiencia, entonces solo los candidatos que cumplen con estos criterios se muestran.
  - Dado que selecciono un candidato para revisión, cuando lo marco como "preseleccionado", entonces el sistema refleja el cambio.
- **Notas adicionales**:
  - Los criterios de filtro deben incluir años de experiencia y competencias específicas.
- **Tareas**:
  - Implementar filtros avanzados en la vista de aplicaciones.
  - Configurar opciones de preselección.
  - Crear un panel con los criterios de búsqueda y selección.

## 3.2 Administrador
- **User Story**: Como administrador, quiero acceder a métricas de filtrado para monitorear el rendimiento de los criterios y ajustar procesos de selección.
- **Descripción**: El administrador puede revisar estadísticas sobre los filtros aplicados y el volumen de candidatos.
- **Criterios de Aceptación**:
  - Dado que el administrador accede al panel de métricas, cuando selecciona una oferta, entonces puede ver estadísticas del número de candidatos y filtros aplicados.
  - Dado que selecciona un filtro, cuando consulta el rendimiento, entonces puede ver la efectividad del criterio en la selección de candidatos.
- **Notas adicionales**:
  - Las métricas permiten ajustar los filtros para mejorar la eficiencia de selección.
- **Tareas**:
  - Crear un panel de métricas de filtrado.
  - Configurar filtros específicos y su registro.
  - Implementar visualización de estadísticas.

# Flujo 4: Gestión de Entrevistas

## 4.1 Reclutador
- **User Story**: Como reclutador, quiero programar entrevistas para candidatos preseleccionados para organizar el proceso de selección y asegurar la asistencia.
- **Descripción**: Permite programar entrevistas y enviar invitaciones a candidatos y entrevistadores.
- **Criterios de Aceptación**:
  - Dado que un candidato ha sido preseleccionado, cuando el reclutador programa una entrevista, entonces el candidato y el entrevistador reciben una invitación.
  - Dado que la entrevista está confirmada, cuando se acerca la fecha, entonces se envían recordatorios automáticos a ambas partes.
- **Notas adicionales**:
  - Las entrevistas deben poder sincronizarse con calendarios externos.
- **Tareas**:
  - Implementar la programación de entrevistas.
  - Configurar invitaciones y recordatorios automáticos.
  - Integrar con calendarios externos (Google, Outlook).

## 4.2 Candidato
- **User Story**: Como candidato, quiero confirmar mi disponibilidad para una entrevista para asegurar que puedo asistir en el horario propuesto.
- **Descripción**: El candidato puede confirmar o solicitar reprogramación de la entrevista.
- **Criterios de Aceptación**:
  - Dado que el candidato recibe una invitación, cuando accede a su perfil, entonces puede confirmar o solicitar un cambio de horario.
  - Dado que la entrevista está confirmada, cuando se acerca la fecha, entonces el candidato recibe un recordatorio automático.
- **Notas adicionales**:
  - El candidato debe poder ver toda la información de la entrevista en su perfil.
- **Tareas**:
  - Crear una interfaz de confirmación para candidatos.
  - Configurar opciones de reprogramación.
  - Implementar recordatorios automáticos para candidatos.

# Flujo 5: Comunicación con Candidatos

## 5.1 Reclutador
- **User Story**: Como reclutador, quiero comunicarme con los candidatos para actualizar su estado para mantener una buena experiencia del candidato y transparencia.
- **Descripción**: Permite al reclutador enviar notificaciones automáticas y mensajes personalizados.
- **Criterios de Aceptación**:
  - Dado que el reclutador cambia el estado de un candidato, cuando selecciona un nuevo estado, entonces se envía una notificación al candidato.
  - Dado que el reclutador envía un mensaje personalizado, cuando el candidato accede a su perfil, entonces puede ver el mensaje en su bandeja de entrada.
- **Notas adicionales**:
  - Los mensajes deben seguir una plantilla para mantener consistencia.
- **Tareas**:
  - Configurar mensajes automáticos de cambio de estado.
  - Crear plantillas para mensajes personalizados.
  - Implementar bandeja de entrada en el perfil del candidato.

## 5.2 Candidato
- **User Story**: Como candidato, quiero recibir notificaciones sobre el estado de mi solicitud para mantenerme informado sin tener que consultar el sistema constantemente.
- **Descripción**: Los candidatos reciben notificaciones automáticas sobre actualizaciones de estado y mensajes importantes.
- **Criterios de Aceptación**:
  - Dado que el candidato recibe una notificación de actualización de estado, cuando revisa su perfil, entonces puede ver un historial completo de las notificaciones.
  - Dado que el candidato recibe un mensaje personalizado, cuando accede a la bandeja de entrada, entonces puede ver el mensaje y cualquier nota adjunta.
- **Notas adicionales**:
  - Los candidatos deben poder acceder a un historial de notificaciones en su perfil.
- **Tareas**:
  - Crear historial de notificaciones para candidatos.
  - Configurar bandeja de entrada para mensajes.
  - Desarrollar lógica de actualización de estado.


# TASKS detalladas para el Flujo 4: Gestión de Entrevistas

# Ticket 1: Programación de Entrevista por Reclutador

**Título**: Programación de Entrevista por el Reclutador

**Descripción**:

- **Propósito**: Permitir que el reclutador programe entrevistas con los candidatos seleccionados, optimizando la organización y el seguimiento de las entrevistas.
- **Detalles Específicos**:
  - El reclutador debe poder seleccionar una fecha y hora específica y asignar a uno o más entrevistadores.
  - Se debe enviar una notificación automática al candidato con los detalles de la entrevista y un enlace de confirmación.

**Criterios de Aceptación**:

- Dado que el reclutador selecciona una fecha y hora para la entrevista, cuando confirma la programación, entonces se debe almacenar la información de la entrevista en el sistema.
- Dado que se programa una entrevista, cuando se confirma la cita, entonces el candidato debe recibir una notificación automática con los detalles y un enlace de confirmación.

**Pruebas de Validación**: Validar que la información de la entrevista se almacena correctamente en la base de datos y que el candidato recibe la notificación.

**Prioridad**: Alta (crucial para la gestión del proceso de selección)

**Estimación de Esfuerzo**: 5 puntos (interfaz y lógica de programación)

**Asignación**: Equipo de Backend (gestión de datos) y Equipo de Frontend (UI para programación)

**Etiquetas**: #reclutador #programación #entrevista #notificación

**Comentarios y Notas**:

- Validar que la fecha y hora seleccionadas no choquen con otras entrevistas ya programadas.
- Confirmar que el candidato recibe la notificación correctamente.

**Enlaces o Referencias**:

- Documentación de integración con API de notificaciones.
- Requisitos de IU del flujo de programación de entrevista.

**Historial de Cambios**:

- [Fecha] - Creación del ticket.

---

# Ticket 2: Confirmación de Entrevista por Candidato

**Título**: Confirmación de Entrevista por el Candidato

**Descripción**:

- **Propósito**: Permitir que el candidato confirme su disponibilidad para la entrevista, asegurando una correcta coordinación entre ambas partes.
- **Detalles Específicos**:
  - El candidato debe recibir una notificación con un enlace para confirmar la entrevista.
  - Al hacer clic en el enlace de confirmación, el sistema debe registrar la respuesta y enviar una notificación de confirmación al reclutador.

**Criterios de Aceptación**:

- Dado que el candidato recibe la notificación de la entrevista, cuando hace clic en el enlace de confirmación, entonces el sistema debe registrar su respuesta como "confirmada".
- Dado que el candidato confirma la entrevista, cuando se almacena la respuesta, entonces el reclutador debe recibir una notificación automática de confirmación.

**Pruebas de Validación**: Verificar que la respuesta del candidato se almacena correctamente y que el reclutador recibe la notificación.

**Prioridad**: Alta (es esencial para la coordinación)

**Estimación de Esfuerzo**: 3 puntos (notificación y lógica de confirmación)

**Asignación**: Equipo de Backend (gestión de datos) y Equipo de Frontend (UI para confirmación)

**Etiquetas**: #candidato #confirmación #entrevista #notificación

**Comentarios y Notas**:

- Asegurar que el estado de la entrevista se actualice automáticamente en la base de datos.
- Confirmar que el reclutador recibe la notificación en tiempo real.

**Enlaces o Referencias**:

- Documentación sobre el flujo de notificaciones.

**Historial de Cambios**:

- [Fecha] - Creación del ticket.

---

# Ticket 3: Envío de Recordatorios para Entrevista

**Título**: Envío de Recordatorios para Entrevista

**Descripción**:

- **Propósito**: Asegurar que tanto el reclutador como el candidato reciban recordatorios antes de la entrevista para minimizar ausencias o retrasos.
- **Detalles Específicos**:
  - El sistema debe enviar un recordatorio al candidato y al reclutador 24 horas y 1 hora antes de la entrevista.
  - El recordatorio debe incluir todos los detalles necesarios y un enlace para revisar la programación.

**Criterios de Aceptación**:

- Dado que la entrevista está programada, cuando faltan 24 horas y 1 hora para la cita, entonces se debe enviar un recordatorio automático tanto al candidato como al reclutador.

**Pruebas de Validación**: Verificar que los recordatorios se envían en el momento correcto y que contienen todos los detalles de la entrevista.

**Prioridad**: Media (mejora la organización y puntualidad)

**Estimación de Esfuerzo**: 5 puntos (programación de recordatorios y notificaciones)

**Asignación**: Equipo de Backend (lógica de recordatorios) y Equipo de Frontend (visualización de recordatorios)

**Etiquetas**: #recordatorio #notificación #entrevista

**Comentarios y Notas**:

- Confirmar que los recordatorios se envíen independientemente del estado de confirmación del candidato.
- Asegurar que los enlaces proporcionen acceso directo a los detalles de la entrevista.

**Enlaces o Referencias**:

- Requisitos para integración con servicios de calendario.

**Historial de Cambios**:

- [Fecha] - Creación del ticket.

---

# Ticket 4: Registro de Feedback post-Entrevista (Reclutador)

**Título**: Registro de Feedback post-Entrevista por el Reclutador

**Descripción**:

- **Propósito**: Facilitar al reclutador el registro de evaluaciones o comentarios sobre el desempeño del candidato durante la entrevista.
- **Detalles Específicos**:
  - El reclutador debe poder completar un formulario de feedback tras la entrevista.
  - Este feedback debe quedar registrado y accesible en el sistema para futuras referencias.

**Criterios de Aceptación**:

- Dado que el reclutador completa la entrevista, cuando envía su feedback, entonces el sistema debe almacenar la evaluación de forma segura y asociarla con el candidato correspondiente.

**Pruebas de Validación**: Validar que el feedback queda correctamente registrado y es accesible para los administradores.

**Prioridad**: Alta (clave para la selección del candidato)

**Estimación de Esfuerzo**: 5 puntos (formulario y lógica de almacenamiento)

**Asignación**: Equipo de Backend (gestión de datos de feedback) y Equipo de Frontend (UI para feedback)

**Etiquetas**: #reclutador #feedback #entrevista

**Comentarios y Notas**:

- Confirmar que el feedback quede vinculado a la entrevista específica y al perfil del candidato.
- El feedback debe ser editable hasta que el proceso de selección esté cerrado.

**Enlaces o Referencias**:

- Documentación sobre evaluación de candidatos.

**Historial de Cambios**:

- [Fecha] - Creación del ticket.
