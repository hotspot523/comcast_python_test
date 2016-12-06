import json, sys

file = 'coordinates.json'

with open(file) as json_data:
    data = json.load(json_data)
    json_data.close()

    print("enter the origin coordinate... x")
    x = int(sys.stdin.readline().strip())
    print("enter the origin coordinate... y")
    y = int(sys.stdin.readline().strip())

    myTuple = tuple([int(x), int(y)])
    l = []
    for d in data:
        l.append(tuple(map(int, (d['value']).split(','))))

    resC= []
    coordinate=(x,y)

    for n in range(0, len(l),1):

        resC.append(min(l, key=lambda c: (c[0]- coordinate[0])**2 + (c[1]-coordinate[1])**2))
        l.remove(min(l, key=lambda c: (c[0]- coordinate[0])**2 + (c[1]-coordinate[1])**2))

    print ("coordinates closest-to-farthest:")
    print (resC)
