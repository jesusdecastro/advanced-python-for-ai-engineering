import argparse
import sys
import logging  # <--- NUEVO: Biblioteca estándar para trazas
from cv_converter.readers import JSONReader
from cv_converter.models import CurriculumVitae
from cv_converter.generators import HiberusTextGenerator
from pydantic import ValidationError

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),  # Sale por terminal
        logging.FileHandler("app.log")      # Se guarda en un archivo de log
    ]
)
logger = logging.getLogger(__name__)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Conversor de CVs a formato Hiberus")
    parser.add_argument("input_file", type=str, help="Ruta del archivo JSON")
    parser.add_argument("--output", "-o", type=str, default="cv_generado.txt", help="Archivo de salida")
    return parser.parse_args()

def main():
    args = parse_arguments()
    logger.info("Iniciando proceso de conversión...") 

    try:
        reader = JSONReader()
        datos_raw = reader.read(args.input_file)
        logger.info(f"Archivo {args.input_file} cargado con éxito.")

        cv = CurriculumVitae(**datos_raw)
        logger.info(f"Validación exitosa para: {cv.nombre_completo}")

        generator = HiberusTextGenerator()
        texto_final = generator.generate(cv)

        with open(args.output, "w", encoding="utf-8") as f:
            f.write(texto_final)
            
        logger.info(f"Documento generado y guardado en: {args.output}")

    except Exception as e:
        logger.error(f"Se ha producido un error: {e}") # <--- Log de error profesional
        sys.exit(1)

if __name__ == "__main__":
    main()