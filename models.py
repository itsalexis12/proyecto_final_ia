from typing import List
from pydantic import BaseModel, Field

# 1. Algoritmo Genético
class GeneticoRequest(BaseModel):
    mensaje_oculto: str
    tam_poblacion: int = Field(..., gt=10, le=500)
    max_generaciones: int = Field(..., gt=1, le=1000)
    prob_cruce: float = Field(..., ge=0.0, le=1.0)
    prob_mutacion: float = Field(..., ge=0.0, le=0.5)

class GeneticoResponse(BaseModel):
    estado: str
    mensaje_oculto_objetivo: str
    solucion_obtenida: str
    aptitud_alcanzada: int
    generaciones_ejecutadas: int
    convergencia: bool
    historial_fitness_max: List[int]

# 2. Árbol de Decisión

# 3. Clustering K-Means
class ClusterRequest(BaseModel):
    k_clusters: int = Field(..., ge=2, le=10)
    max_iteraciones: int = Field(..., gt=5, le=500)
    datos: List[List[float]]

class ClusterResponse(BaseModel):
    estado: str
    k_utilizado: int
    num_muestras: int
    centroides_finales: List[List[float]]
    etiquetas_asignadas: List[int]
    inercia_wcss: float