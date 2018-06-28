import json

def convert (feed):
    f = open(feed + '.json', 'r')
    jf = json.load(f)
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type" : 
                "Feature",
                "geometry" : {
                    
                    "type": "Point",
                    "coordinates": item['coordinates']['coordinates'],
                    },
                "properties" : item,
            } for item in jf
        ]
    }
    f.close()
    f = open(feed + '.geojson', 'w')
    json.dump(geojson, f)
    f.close()

if __name__ == "__main__":
    convert('data_loc_en')
