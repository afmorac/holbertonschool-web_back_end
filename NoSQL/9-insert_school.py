#!/usr/bin/env python3
"""
Insertar un documento en la colección
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserta un doc usando kwargs
    Devuelve el _id nuevo
    """
    # insert_one crea el doc con los campos dados
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
