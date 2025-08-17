#!/usr/bin/env python3
"""
Buscar escuelas por topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Devuelve todas las escuelas que tengan ese topic
    - topic: string (ej. "Python")
    """
    # find con condición en el array topics
    return list(mongo_collection.find({ "topics": topic }))
