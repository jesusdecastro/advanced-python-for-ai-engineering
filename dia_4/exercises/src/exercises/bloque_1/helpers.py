"""
Funciones helper para procesamiento de configuraciones.

YA ESTÁN IMPLEMENTADAS — no las modifiques, solo úsalas desde tus clases.
"""


def normalize_job_name(name: str) -> str:
    """
    Normalize job name to snake_case.

    :param name: Raw job name
    :type name: str
    :return: Normalized name
    :rtype: str
    """
    return name.strip().lower().replace(" ", "_")
