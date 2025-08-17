#!/usr/bin/env python3
"""
Actualizar los topics de una escuela por nombre
"""

def update_topics(mongo_collection, name, topics):
    """
    Cambia los topics de la escuela con ese nombre
    - name: string (nombre de la escuela)
    - topics: lista de strings
    """
    # update_one busca por nombre y reemplaza el campo topics
    mongo_collection.update_one(
        { "name": name },
        { "$set": { "topics": topics } }
    )
