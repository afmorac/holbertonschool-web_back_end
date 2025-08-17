#!/usr/bin/env python3
"""
Stats de Nginx en MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    # Conexión local por default
    client = MongoClient()
    col = client.logs.nginx  # DB: logs, Collection: nginx

    # 1) total
    total = col.count_documents({})
    print("{} logs".format(total))

    # 2) métodos (orden exacto) — OJO: TAB real antes de 'method'
    print("Methods:")
    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        cnt = col.count_documents({"method": m})
        print("\tmethod {}: {}".format(m, cnt))

    # 3) GET /status
    status_cnt = col.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_cnt))
