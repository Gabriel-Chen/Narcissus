import json

f = open('datosRETC.json', 'r')
jf = json.load(f)
f.close()
after = [ ]
for item in jf:
    try:
        location = item['location']
        lat = float(location[0])
        lng = float(location[1])
        if lat < 33 and lat > 14 and lng < 119 and lng > 86:
            after.append(item)
    except:
        pass
f = open('datosRETCafter.json', 'w')
json.dump(after, f)
f.close()
