#!/usr/bin/env python3
"""
Stats de Nginx en MongoDB
"""

from pymongo import MongoClient


def main():
    """Imprime las stats con el formato exacto"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    col = client.logs.nginx  # DB: logs, Collection: nginx

    # total de logs
    total = col.count_documents({})
    print(f"{total} logs")

    # métodos en orden exacto
    print("Methods:")
    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        cnt = col.count_documents({"method": m})
        print(f"\tmethod {m}: {cnt}")  # OJO: \t es tabulación

    # GET /status
    status_cnt = col.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_cnt} status check")


if __name__ == "__main__":
    main()
