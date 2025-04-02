import requests

def geocode_address(address):
    """Convert address to latitude/longitude using OpenStreetMap Nominatim API"""
    url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json&limit=1"
    headers = {"User-Agent": "HydrogenStorageVisualizer/1.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return float(data['lat']), float(data['lon'])
    return None, None