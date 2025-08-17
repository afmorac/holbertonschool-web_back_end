#!/usr/bin/env python3
"""
Función para listar todos los documentos de una colección
"""

def list_all(mongo_collection):
    """
    Devuelve todos los documentos de la colección
    Si no hay, devuelve lista vacía
    """
    # find() trae todos los docs → lo convertimos a lista
    return list(mongo_collection.find())
