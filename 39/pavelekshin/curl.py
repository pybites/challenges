import os

tests = """
# get items
curl -i http://127.0.0.1:5000/api/v1.0/items
# item 1
curl -i http://127.0.0.1:5000/api/v1.0/items/1
# item2
curl -i http://127.0.0.1:5000/api/v1.0/items/2
# err: non-existing item
curl -i http://127.0.0.1:5000/api/v1.0/items/4
# err: add item already in items
curl -i -H "Content-Type: application/json" -X POST -d  '{"name":"book", "value": 20}' http://127.0.0.1:5000/api/v1.0/items
# err: add item with value not int 
curl -i -H "Content-Type: application/json" -X POST -d  '{"name":"monitor", "value": "200"}' http://127.0.0.1:5000/api/v1.0/items
# add item with proper values
curl -i -H "Content-Type: application/json" -X POST -d  '{"name":"monitor", "value": 200}' http://127.0.0.1:5000/api/v1.0/items
# show items
curl -i http://127.0.0.1:5000/api/v1.0/items
# err: edit non-existing item
curl -i -H "Content-Type: application/json" -X PUT -d '{"value": 30}' http://127.0.0.1:5000/api/v1.0/items/5
# OK: edit existing item
curl -i -H "Content-Type: application/json" -X PUT -d '{"value": 30}' http://127.0.0.1:5000/api/v1.0/items/3
# show items
curl -i http://127.0.0.1:5000/api/v1.0/items
# err: delete non-existing item
curl -i -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/api/v1.0/items/5
# OK: delete existing item
curl -i -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/api/v1.0/items/3
# show items
curl -i http://127.0.0.1:5000/api/v1.0/items
"""

for line in tests.strip().split("\n"):
    print("\n{}".format(line))
    if not line.startswith("#"):
        cmd = line.strip()
        os.system(cmd)
