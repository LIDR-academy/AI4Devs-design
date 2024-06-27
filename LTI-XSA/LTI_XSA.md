# LTI XSA

## Descripción del Software LTI XSA
LTI XSA es un avanzado Sistema de Seguimiento de Candidatos (ATS) diseñado para optimizar y transformar el proceso de contratación. Nuestra plataforma ofrece una solución integral que abarca desde la publicación de ofertas de empleo hasta la incorporación de nuevos empleados, utilizando inteligencia artificial y automatización para maximizar la eficiencia y mejorar la experiencia tanto de reclutadores como de candidatos.

### Valor Añadido y Ventajas Competitivas
- **Inteligencia Artificial (IA) Integrada**: Utilizamos IA para mejorar la criba de candidatos, sugerir matches ideales y ofrecer análisis predictivos.
- **Automatización Avanzada**: Reducimos las tareas repetitivas mediante automatización, incluyendo la programación de entrevistas y el envío de correos electrónicos personalizados.
- **Colaboración en Tiempo Real**: Facilitamos la comunicación y colaboración entre reclutadores y managers mediante herramientas integradas de mensajería y gestión de tareas.
- **Analíticas y Reportes Detallados**: Ofrecemos informes en tiempo real y métricas detalladas sobre el proceso de contratación.
- **Experiencia del Candidato Mejorada**: Proporcionamos un proceso de aplicación fluido y profesional que mejora la percepción de la empresa.

## Funcionalidades Básicas
1. **Publicación Multicanal**: Publicación de ofertas en múltiples portales y redes sociales desde una única plataforma.
2. **Gestión de Solicitudes**: Centralización y organización de todas las solicitudes recibidas.
3. **Cribado Automático**: Filtrado y clasificación de candidatos mediante IA.
4. **Comunicación y Programación**: Herramientas para la programación automática de entrevistas y comunicación fluida con los candidatos.
5. **Analíticas y Reportes**: Generación de informes detallados sobre el proceso de contratación.
6. **Cumplimiento Legal**: Aseguramiento de que todas las actividades cumplen con las normativas legales.
7. **Integraciones**: Conexión con otros sistemas de recursos humanos, ERPs y redes sociales.

## Beneficios para Nuestros Clientes
- **Aumento de la Eficiencia**: Reducción de tareas administrativas y repetitivas.
- **Mejora en la Calidad de Contrataciones**: Mejor criba y selección de candidatos.
- **Mayor Colaboración**: Facilitación de la comunicación entre los equipos de reclutamiento.
- **Experiencia del Candidato Mejorada**: Procesos más profesionales y ágiles.
- **Decisiones Informadas**: Datos y métricas que permiten tomar decisiones estratégicas.

## Customer Journey
1. **Inicio**: El cliente se registra y configura el sistema según sus necesidades.
2. **Publicación de Vacantes**: Se crean y publican ofertas de empleo en múltiples canales.
3. **Recepción y Cribado**: Se reciben las solicitudes y se realiza un cribado automático.
4. **Evaluación y Entrevistas**: Los reclutadores evalúan a los candidatos y programan entrevistas.
5. **Selección y Contratación**: Se selecciona al candidato adecuado y se realiza la contratación.
6. **Incorporación y Seguimiento**: El candidato es incorporado y se realiza un seguimiento de su integración.

## Lean Canvas

### Problem
1. Procesos de contratación ineficientes.
2. Tareas administrativas repetitivas.
3. Dificultad para encontrar candidatos adecuados.

### Solution
1. IA para cribado y análisis predictivos.
2. Automatización de tareas.
3. Publicación multicanal y gestión centralizada de solicitudes.

### Key Metrics
1. Tiempo de contratación.
2. Tasa de aceptación de ofertas.
3. Satisfacción de los usuarios.

### Unique Value Proposition
- Solución integral y automatizada para la gestión de candidatos.
- IA y analíticas avanzadas.
- Colaboración en tiempo real.

### Unfair Advantage
- Tecnología de IA propietaria.
- Integración fluida con múltiples plataformas.
- Experiencia de usuario optimizada.

### Channels
- Marketing digital.
- Redes sociales.
- Asociaciones con empresas de recursos humanos.

### Customer Segments
1. Empresas medianas y grandes.
2. Agencias de reclutamiento.
3. Startups en crecimiento.

### Cost Structure
- Desarrollo y mantenimiento del software.
- Marketing y ventas.
- Soporte al cliente.

### Revenue Streams
- Suscripciones mensuales/anuales.
- Servicios premium y personalizados.
- Integraciones a medida.

## Casos de Uso Principales

### Caso de Uso 1: Publicación de Vacantes
**Descripción**: El reclutador puede crear y publicar una oferta de empleo en múltiples portales y redes sociales desde una única interfaz.

```plaintext
+-------------+
|  Reclutador |
+-------------+
       |
       v
+-------------------+
| Crear Vacante     |
+-------------------+
       |
       v
+-------------------------+
| Seleccionar Canales     |
+-------------------------+
       |
       v
+---------------------------+
| Publicar en Canales       |
+---------------------------+

### Caso de Uso 2: Cribado Automático de Candidatos
**Descripción**: El sistema realiza un cribado automático de los candidatos recibidos, clasificándolos según criterios predefinidos.

+-------------------+
| Solicitudes       |
+-------------------+
       |
       v
+------------------------+
| Cribado Automático     |
+------------------------+
       |
       v
+-------------------------+
| Lista de Candidatos     |
+-------------------------+

### Caso de Uso 3: Programación de Entrevistas
**Descripción**: El sistema permite programar entrevistas automáticamente entre los candidatos y los reclutadores.

+-------------+
|  Reclutador |
+-------------+
       |
       v
+-------------------+
| Seleccionar Fecha |
+-------------------+
       |
       v
+-------------------------+
| Enviar Invitación       |
+-------------------------+
       |
       v
+---------------------------+
| Confirmación del Candidato|
+---------------------------+

## Modelo de datos

### Entidades y atributos
#### Candidato
- **ID**: `UUID`
- **Nombre**: `String`
- **Email**: `String`
- **Teléfono**: `String`
- **CV**: `Texto/Documento`
- **Estado**: `Enumerado` (Aplicado, Cribado, Entrevista, Contratado, Rechazado)
- **Fecha de Aplicación**: `Fecha`

#### Vacante
- **ID**: `UUID`
- **Título**: `String`
- **Descripción**: `Texto`
- **Requisitos**: `Texto`
- **Fecha de Publicación**: `Fecha`
- **Estado**: `Enumerado` (Abierta, Cerrada)

#### Entrevista
- **ID**: `UUID`
- **Fecha**: `Fecha y Hora`
- **CandidatoID**: `UUID`
- **ReclutadorID**: `UUID`
- **Estado**: `Enumerado` (Programada, Realizada, Cancelada)

#### Reclutador
- **ID**: `UUID`
- **Nombre**: `String`
- **Email**: `String`
- **Departamento**: `String`

### Relaciones:
- Un Candidato puede aplicar a múltiples Vacantes.
- Una Vacante puede tener múltiples Candidatos.
- Un Candidato puede tener múltiples Entrevistas.
- Un Reclutador puede tener múltiples Entrevistas.

## Diseño del Sistema a Alto Nivel

**Componentes del Sistema:**
- **Frontend:** Interfaz de usuario para reclutadores y candidatos.
- **Backend:** Lógica de negocio y APIs.
- **Base de Datos:** Almacenamiento de datos de candidatos, vacantes, entrevistas y reclutadores.
- **Módulo de IA:** Algoritmos de cribado y análisis predictivos.
- **Módulo de Integraciones:** Conexiones con portales de empleo, redes sociales y otros sistemas de HR.

**Diagrama de Arquitectura de Alto Nivel:**

+---------------------+
|     Frontend        |
+---------------------+
         |
         v
+---------------------+
|       Backend       |
+---------------------+
     |        |        |
     v        v        v
+--------+ +--------+ +--------+
|  DB    | |  IA    | |  Integr|
+--------+ +--------+ +--------+

## Diagrama C4 en Profundidad

### Contexto (C1)

+-------------+
|  Usuario    |
+-------------+
       |
       v
+----------------+
| LTI XSA System |
+----------------+

### Contenedor (C2)

+-------------------------------------------------+
|               LTI XSA System                    |
+-------------------------------------------------+
| +--------------------------------------------+ |
| |                  Backend                   | |
| +--------------------------------------------+ |
| +--------------------------------------------+ |
| |                  Frontend                  | |
| +--------------------------------------------+ |
| +--------------------------------------------+ |
| |                   DB                       | |
| +--------------------------------------------+ |
| +--------------------------------------------+ |
| |                   IA                       | |
| +--------------------------------------------+ |
| +--------------------------------------------+ |
| |               Integraciones                | |
| +--------------------------------------------+ |
+-------------------------------------------------+

### Componente (C3): Backend

+----------------------------------------+
|                Backend                 |
+----------------------------------------+
| +------------------------------------+ |
| |       API de Gestión de Vacantes   | |
| +------------------------------------+ |
| +------------------------------------+ |
| |       API de Gestión de Candidatos | |
| +------------------------------------+ |
| +------------------------------------+ |
| |       API de Gestión de Entrevistas| |
| +------------------------------------+ |
| +------------------------------------+ |
| |           Módulo de IA             | |
| +------------------------------------+ |
+----------------------------------------+


### Código (C4): API de Gestión de Candidatos

+--------------------------------------------+
|        API de Gestión de Candidatos        |
+--------------------------------------------+
| - getCandidate()                           |
| - createCandidate()                        |
| - updateCandidate()                        |
| - deleteCandidate()                        |
+--------------------------------------------+

