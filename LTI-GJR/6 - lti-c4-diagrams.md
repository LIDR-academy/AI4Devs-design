# Diagramas C4 - Sistema de Matching de Candidatos LTI ATS

## 1. Diagrama de Contexto (Nivel 1)
```mermaid
C4Context
    title Sistema de Matching de Candidatos - Diagrama de Contexto

    Person(recruiter, "Reclutador", "Usuario que busca candidatos")
    Person(candidate, "Candidato", "Usuario que busca trabajo")
    
    System(matchingSystem, "Sistema de Matching", "Core system para matching inteligente de candidatos y posiciones")
    
    System_Ext(jobBoards, "Job Boards", "Plataformas externas de empleo")
    System_Ext(linkedIn, "LinkedIn API", "Datos profesionales")
    System_Ext(emailSystem, "Sistema de Email", "Comunicación con usuarios")

    Rel(recruiter, matchingSystem, "Busca candidatos ideales")
    Rel(candidate, matchingSystem, "Aplica a posiciones")
    Rel(matchingSystem, jobBoards, "Publica y sincroniza ofertas")
    Rel(matchingSystem, linkedIn, "Obtiene datos profesionales")
    Rel(matchingSystem, emailSystem, "Envía notificaciones")
```

## 2. Diagrama de Contenedores (Nivel 2)
```mermaid
C4Container
    title Sistema de Matching de Candidatos - Diagrama de Contenedores

    Person(recruiter, "Reclutador", "Usuario que busca candidatos")
    Person(candidate, "Candidato", "Usuario que busca trabajo")

    Container_Boundary(c1, "Sistema de Matching") {
        Container(webApp, "Web Application", "React", "Interface de usuario")
        Container(apiGateway, "API Gateway", "Node.js", "Gestión de APIs y autenticación")
        Container(matchingService, "Matching Service", "Python/FastAPI", "Lógica core de matching")
        Container(mlEngine, "ML Engine", "Python/TensorFlow", "Procesamiento ML/AI")
        Container(profileService, "Profile Service", "Node.js/NestJS", "Gestión de perfiles")
        Container(searchEngine, "Search Engine", "Elasticsearch", "Búsqueda avanzada")
        ContainerDb(mainDB, "Main Database", "PostgreSQL", "Datos principales")
        ContainerDb(vectorDB, "Vector Database", "Pinecone", "Embeddings y vectores")
    }

    Rel(recruiter, webApp, "Usa", "HTTPS")
    Rel(candidate, webApp, "Usa", "HTTPS")
    Rel(webApp, apiGateway, "API calls", "JSON/HTTPS")
    Rel(apiGateway, matchingService, "Requests", "gRPC")
    Rel(apiGateway, profileService, "Requests", "gRPC")
    Rel(matchingService, mlEngine, "Procesa", "gRPC")
    Rel(matchingService, searchEngine, "Busca", "REST")
    Rel(matchingService, mainDB, "Lee/Escribe", "SQL")
    Rel(mlEngine, vectorDB, "Almacena vectors", "gRPC")
    Rel(profileService, mainDB, "Lee/Escribe", "SQL")
```

## 3. Diagrama de Componentes - Matching Service (Nivel 3)
```mermaid
C4Component
    title Sistema de Matching - Diagrama de Componentes del Matching Service

    Container_Boundary(c1, "Matching Service") {
        Component(matchController, "Matching Controller", "FastAPI", "API endpoints para matching")
        Component(matchEngine, "Match Engine", "Python", "Core matching logic")
        Component(scoringEngine, "Scoring Engine", "Python", "Calcula match scores")
        Component(rankingSystem, "Ranking System", "Python", "Ordena y prioriza matches")
        Component(filterEngine, "Filter Engine", "Python", "Aplica filtros y reglas")
        Component(dataProcessor, "Data Processor", "Python", "Preprocesa datos")
        Component(cacheManager, "Cache Manager", "Python/Redis", "Gestión de caché")
    }

    Container(mlEngine, "ML Engine", "Python/TensorFlow", "ML processing")
    Container(profileService, "Profile Service", "NestJS", "Profile management")
    ContainerDb(mainDB, "Main Database", "PostgreSQL", "Primary data store")
    ContainerDb(vectorDB, "Vector Database", "Pinecone", "Vector storage")
    ContainerDb(cacheDB, "Cache", "Redis", "Performance cache")

    Rel(matchController, matchEngine, "Invoca")
    Rel(matchEngine, scoringEngine, "Calcula scores")
    Rel(matchEngine, rankingSystem, "Ordena resultados")
    Rel(matchEngine, filterEngine, "Aplica filtros")
    Rel(scoringEngine, dataProcessor, "Procesa datos")
    Rel(dataProcessor, cacheManager, "Cachea resultados")
    
    Rel(matchEngine, mlEngine, "Solicita predicciones")
    Rel(matchEngine, profileService, "Obtiene perfiles")
    Rel(dataProcessor, mainDB, "Lee datos")
    Rel(scoringEngine, vectorDB, "Consulta vectors")
    Rel(cacheManager, cacheDB, "Gestiona caché")
```

## 4. Diagrama de Código - Scoring Engine (Nivel 4)
```mermaid
classDiagram
    class ScoringEngine {
        -weightCalculator: WeightCalculator
        -similarityProcessor: SimilarityProcessor
        -scoreNormalizer: ScoreNormalizer
        +calculateMatchScore(candidateProfile, jobRequirements)
        +updateWeights(newWeights)
        -normalizeScores()
    }

    class WeightCalculator {
        -weights: Dictionary
        +calculateWeights(features)
        +updateWeightMatrix()
        -normalizeWeights()
    }

    class SimilarityProcessor {
        -vectorizer: Vectorizer
        -similarityMetrics: List
        +calculateSimilarity(vector1, vector2)
        +processBatch(vectors)
        -normalizeVectors()
    }

    class ScoreNormalizer {
        -normalizationParams: Dictionary
        +normalizeScore(rawScore)
        +batchNormalize(scores)
        -calculateParameters()
    }

    class MatchScore {
        +candidateId: String
        +jobId: String
        +score: Float
        +confidence: Float
        +matchFactors: List
        +timestamp: DateTime
    }

    ScoringEngine --> WeightCalculator
    ScoringEngine --> SimilarityProcessor
    ScoringEngine --> ScoreNormalizer
    ScoringEngine ..> MatchScore
```

## Detalles Técnicos del Sistema de Matching

### 1. Componentes Principales

#### Matching Controller
- Gestión de endpoints REST
- Validación de requests
- Rate limiting
- Response formatting

#### Match Engine
- Orquestación del proceso
- Gestión de workflows
- Optimización de queries
- Distribución de carga

#### Scoring Engine
- Cálculo de match scores
- Ponderación de factores
- Normalización de resultados
- Calibración automática

#### Ranking System
- Ordenamiento multifactorial
- Priorización contextual
- Agrupamiento inteligente
- Personalización de rankings

#### Filter Engine
- Aplicación de reglas de negocio
- Filtros dinámicos
- Validación de requisitos
- Exclusiones automáticas

#### Data Processor
- Normalización de datos
- Transformación de formatos
- Validación de integridad
- Enriquecimiento de datos

#### Cache Manager
- Gestión de caché distribuida
- Invalidación inteligente
- Precarga predictiva
- Optimización de memoria

### 2. Flujos Principales

#### A. Matching Process Flow
1. Recepción de request
2. Validación de parámetros
3. Preprocesamiento de datos
4. Cálculo de scores
5. Aplicación de filtros
6. Ranking de resultados
7. Formateo de respuesta

#### B. Scoring Flow
1. Extracción de features
2. Vectorización de datos
3. Cálculo de similitud
4. Ponderación de factores
5. Normalización de scores
6. Agregación de resultados
7. Validación final

### 3. Consideraciones Técnicas

#### Escalabilidad
- Diseño stateless
- Procesamiento distribuido
- Caching multinivel
- Sharding de datos

#### Performance
- Optimización de queries
- Batch processing
- Async operations
- Index optimization

#### Resiliencia
- Circuit breakers
- Retry policies
- Fallback strategies
- Error handling

#### Monitoreo
- Métricas en tiempo real
- Logging distribuido
- Alerting inteligente
- Performance tracking

---
*Documento generado para LTI - Versión 1.0*
