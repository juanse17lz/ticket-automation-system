def validar_no_vacio(valor: str, nombre_campo: str = "Campo") -> bool:
    """
    Valida que un valor no sea un campo vacío.
    
    Args:
        valor: El string a validar.
        nombre_campo: Nombre descriptivo del campo (para el mensaje de error).
    
    Returns:
        True si el campo es válido, False si está vacío.
    """
    if not valor or not valor.strip():
        print(f"Error: {nombre_campo} no puede estar vacío.")
        return False
    return True