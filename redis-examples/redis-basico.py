from datetime import datetime
import json

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0, charset='utf-8')

"""
Commandos de Redis para listas
https://redis.io/commands#list
El tipo de clave valor se define automáticamente al hacer primer insert
"""

""" Añade en una lista al final de la cola """
demo_row = {
    'msg': 'Insert por abajo',
    'type': 'log',
    'date': datetime.now().isoformat()
}
r.lpush('demo:lista', json.dumps(demo_row))
demo_row = {
    'msg': 'Segundo insert al final de la lista',
    'type': 'info',
    'date': datetime.now().isoformat()
}
r.lpush('demo:lista', json.dumps(demo_row))
""" r.rpush() hace lo mismo pero insertando al principio """

""" Se trae el primer elemento de la lista y lo borra """
demo_get = r.lpop('demo:lista')
print(demo_get.decode('utf-8'))
""" r.rpop el útimo elemento de la lista y lo borra """

""" Para hacer un get de un rango """
index_inicio = 0
index_fin = 1
# Trae los dos primeros elementos en este caso
r.lrange('demo:lista', index_inicio, index_fin)

""" Para borrar varios elementos """
index_inicio = 0
index_fin = -1
r.ltrim('demo:lista', index_inicio, index_fin)

"""
Commandos de Redis para hash
https://redis.io/commands#hash
"""
