from flask import Flask, jsonify

app = Flask(__name__)

trip_rainfall=[
    {"station":"USC00516128", "name":"MANOA LYON ARBO 785.2, HI US", "total_precip":"1068.0899999999997", "station_lat":"21.3331","station_lng":" -157.8025","station_elevation":"152.4"}, 
    {"station":"USC00519281", "name":"WAIHEE 837.5, HI US", "total_precip":"588.6400000000001", "station_lat":"21.45167","station_lng":"-157.84888999999998","station_elevation":"32.9"},
    {"station":"USC00513117", "name":"KANEOHE 838.1, HI US", "total_precip":"382.6199999999998", "station_lat":"21.4234","station_lng":"-157.8015","station_elevation":"14.6"},
    {"station":"USC00519523", "name":"WAIMANALO EXPERIMENTAL FARM, HI US", "total_precip":"295.6800000000001", "station_lat":"21.33556","station_lng":"-157.71139","station_elevation":"19.5"}
    "station":"USC00514830", "name":"KUALOA RANCH HEADQUARTERS 886.9, HI US", "total_precip":"234.49000000000007", "station_lat":"21.5213", "station_lng": "-157.8374", "station_elevation": "7.0"},
    {"station":"USC00519397", "name":"WAIKIKI 717.2, HI US","total_precip": "131.61999999999992","station_lat": "21.2716", "station_lng":"-157.8168", "station_elevation": "3.0"},
    {"station":"USC00511918", "name":"HONOLULU OBSERVATORY 702.2, HI US", "total_precip": "92.67999999999995","station_lat": "21.3152","station_lng": "-157.9992","station_elevation": "0.9"},
    {"station":"USC00518838", "name":"UPPER WAHIAWA 874.3, HI US", "total_precip":"170.86999999999999","station_lat":"21.4992", "station_lng":"-158.0111","station_elevation": "306.6"},
    {"station":"USC00517948","name": "PEARL CITY, HI US","total_precip":"43.43999999999998","station_lat": "21.3934","station_lng": "-157.9751","station_elevation": "11.9"}
]

@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

@app.route('/api/v1.0/precipitation')
def 