from cv_converter.models import CurriculumVitae

class HiberusTextGenerator:
    """
    Clase encargada exclusivamente de generar la representación visual
    del CV en formato texto plano/Markdown.
    """
    
    def generate(self, cv: CurriculumVitae) -> str:
        # 1. Cabecera Corporativa
        output = []
        output.append("============================================================")
        output.append("                 HIBERUS TECHNOLOGY - PERFIL                ")
        output.append("============================================================")
        
        # 2. Datos Personales
        output.append(f"NOMBRE:   {cv.nombre_completo.upper()}")
        output.append(f"PERFIL:   {cv.perfil_profesional}")
        output.append(f"EMAIL:    {cv.contacto.email}")
        if cv.contacto.linkedin:
            output.append(f"LINKEDIN: {cv.contacto.linkedin}")
            
        output.append("-" * 60)
        
        # 3. Stack Tecnológico
        tech_str = " | ".join(cv.tech_stack)
        output.append(f"TECH STACK: [{tech_str}]")
        
        output.append("-" * 60)
        output.append("EXPERIENCIA LABORAL:")
        
        # 4. Bucle para experiencias
        for exp in cv.experiencia_laboral:
            header_exp = f"* {exp.empresa} | {exp.rol} ({exp.fecha_inicio} - {exp.fecha_fin or 'Actualidad'})"
            output.append(header_exp)
            output.append(f"  > {exp.descripcion}")
            output.append("") 
            
        output.append("============================================================")
        
        return "\n".join(output)