from pydantic import BaseModel, Field
from typing import List, Optional

class Experiencia(BaseModel):
    empresa: str = Field(..., min_length=2)
    rol: str = Field(..., description="Ej: Fullstack developer")
    fecha_inicio: str = Field(..., pattern=r"^\d{4}$")
    fecha_fin: Optional[str] = None
    descripcion: str

class Contacto(BaseModel):
    email: str
    telefono: Optional[str] = None
    linkedin: Optional[str] = None

class CurriculumVitae(BaseModel):
    nombre_completo: str = Field(..., min_length=2)
    perfil_profesional: str
    tech_stack: List[str] = []
    contacto: Contacto
    experiencia_laboral: List[Experiencia] = []