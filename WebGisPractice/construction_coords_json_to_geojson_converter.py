import os
import json
import requests

SERVER_BASE_URL: str = "http://[2a01:4f8:c2c:97ba::1]:8000"


def fetch_construction_location_data_as_geo_json():
    response: requests.Response = requests.get(
        SERVER_BASE_URL + "/api/construction-location",
        headers={
            "Content-Type": "application/json"
        }
    )
    response_data = response.json()

    point_features = []
    for response_entry in response_data:
        current_feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [response_entry["longitude"], response_entry["latitude"]]
            },
            "properties": {
                "id": response_entry["id"],
                "marker-symbol": "building",
                "created_at": response_entry["created_at"]
            }
        }
        point_features.append(current_feature)

    return {
        "type": "FeatureCollection",
        "features": point_features
    }


geo_json = fetch_construction_location_data_as_geo_json()

OUTPUT_FILE_PATH: str = "./data/construction_site_points.geojson"
os.makedirs(os.path.dirname(OUTPUT_FILE_PATH), exist_ok=True)

with open(OUTPUT_FILE_PATH, "w") as file:
    file.write(json.dumps(geo_json, indent=2))

# Visualize in browser geojson: https://geojson.io/
