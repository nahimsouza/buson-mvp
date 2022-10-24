import json
import requests
import pycep_correios
import time

# key from graphhopper
key = "9c82d051-6ef6-4b98-b53b-29aa4466ac64"

# cep_sorocaba = [
#     # 18055091,
#     # 18071305,
#     # 18072856,
#     # 18080130,
#     # 18095340,
#     18081090,
#     18015140,
#     18015195,
#     18045520,
#     18044160,
# ]

# 18035380, 18035370, 18035060, 18035520, 18087561, 
# cep_sorocaba = [ 18085855, 18055010, 18055001, 18087039, 18087010, 18073703]

init_points = {
    'point': [
        {'lat': -23.494716, 'lng': -47.464843235154966}, 
        {'lat': -23.4993616, 'lng': -47.4737205}, 
        {'lat': -23.5063036, 'lng': -47.4592302}, 
        {'lat': -23.4770451, 'lng': -47.43509}, 
        {'lat': -23.4995769, 'lng': -47.5079568}, 
        {'lat': -23.4996704, 'lng': -47.511613}, 
        {'lat': -23.4419185, 'lng': -47.4556756}, 
        {'lat': -23.4465519, 'lng': -47.4599515}, 
        {'lat': -23.4914162, 'lng': -47.5080073}, 
        {"lat":-23.5014919, "lng":-47.372856}, 
        {'lat': -23.4460623, 'lng': -47.498025}, 
        {'lat': -23.4864668, 'lng': -47.4574782}, 
        {"lat":-23.4915767, "lng":-47.4491002}, 
        {'lat': -23.4783353, 'lng': -47.450232}, 
        {'lat': -23.5032815, 'lng': -47.4338944}, 
        {'lat': -23.4989181, 'lng': -47.4326235}, 
        {'lat': -23.520004550000003, 'lng': -47.48403724666956}, 
        {'lat': -23.5091208, 'lng': -47.4756003}
    ]
}


input_graph = {
    "vehicles" : [

    ],
    "vehicle_types": [

    ],
    "services": [

    ],
    "objectives": [
    ]
}

vehicle_types = {
    "type_id": "bus-transport",
    "profile": "truck",
    "capacity": [ 5 ]
}

objectives = [
    {
    "type": "min-max",
    "value": "completion_time"
    },
    {
    "type": "min-max",
    "value": "activities"
    }
]

id_vehicles = 0
id_services = 0

def new_vehicles():

    vehicles_template = {
        "vehicle_id": "bus",
        "type_id": "bus-transport",
        "end_address": {
            "location_id": "flextronics",
            "lon": -47.3678,
            "lat": -23.428313
        },
    }

    vehicles_aux = vehicles_template.copy()

    global id_vehicles 
    id_vehicles += 1

    vehicles_aux['vehicle_id'] = vehicles_aux['vehicle_id'] + " " + str(id_vehicles)
    return vehicles_aux

def new_services(latitude, longitude):

    services_template = {
        "id": "service",
        "name": "point",
        "address": {
        "location_id": "location",
        "lon": 0,
        "lat": 0
        }
    }

    service_aux = dict(services_template)

    global id_services

    id_services += 1

    service_aux['name'] = service_aux['name'] + " " + str(id_services)
    service_aux['id'] = service_aux['id'] + " " + str(id_services)
    (service_aux['address'])['location_id'] = (service_aux['address'])['location_id'] + " " + str(id_services)

    (service_aux['address'])['lon'] = longitude
    (service_aux['address'])['lat'] = latitude

    return service_aux

def set_new_service():
    cep = input('Digite seu CEP: ').replace(' ', '+')
    address = pycep_correios.get_address_from_cep(cep)
    aux_address = address['logradouro'].split(" ")
    del(aux_address[0])
    separator = ' '
    address_name = separator.join(aux_address)
    address_graph =  address_name+ ', ' + address['cidade'] + ', Brazil' 
    url = f'https://graphhopper.com/api/1/geocode?q={address_graph}&key={key}&debug=true'
    r = requests.get(url)
    # print(r.text)
    r_dictionary= r.json()

    loc = (r_dictionary['hits'])[0]

    for hit in r_dictionary['hits']:
        if hit['city'] == address['cidade']:
            loc = hit
            break

    loc_point = loc['point']

    global input_graph

    input_graph['services'].append(new_services(loc_point['lat'], loc_point['lng']))

set_new_service()

input_graph['vehicle_types'].append(vehicle_types)

input_graph['objectives'] = objectives

input_graph['vehicles'].append(new_vehicles())
input_graph['vehicles'].append(new_vehicles())
input_graph['vehicles'].append(new_vehicles())

input_graph['services'].append(new_services(-23.534395, -47.462948))

points_cep = {
    "point": [

    ]
}

def get_lat_lon_cep(cep):
    address = pycep_correios.get_address_from_cep(cep)
    aux_address = address['logradouro'].split(" ")
    del(aux_address[0])
    separator = ' '
    address_name = separator.join(aux_address)

    # print(f'endereco: {address_name}')

    address_graph =  address_name+ ', ' + address['cidade'] + ', Brazil' 
    url = f'https://graphhopper.com/api/1/geocode?q={address_graph}&key={key}&debug=true'
    r = requests.get(url)
    
    print(r.text)
    
    r_dictionary= r.json()

    loc = (r_dictionary['hits'])[0]

    for hit in r_dictionary['hits']:
        if hit['city'] == address['cidade']:
            loc = hit
            break

    loc_point = loc['point']

    global points_cep

    points_cep["point"].append(loc_point)


# pprint.pprint(input_graph)

# for cep_info in cep_sorocaba:
#     print(cep_info)
#     try:
#         get_lat_lon_cep(str(cep_info))
#     except Exception as e:
#         pass
        # print(points_cep)

for point in init_points["point"]:
    input_graph['services'].append(new_services(point["lat"], point["lng"]))

# print(points_cep)

json_object = json.dumps(input_graph, indent = 4) 
print(json_object)

with open("sample.json", "w") as outfile:
    json.dump(input_graph, outfile)




