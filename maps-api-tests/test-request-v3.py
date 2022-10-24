import requests
import json 

key = "40ca48a2-d89c-4762-8860-9161190af2f0"


print ("\nTEST GET ====> ")

ploads = {'things':2,'total':25}
r = requests.get('https://httpbin.org/get',params=ploads)
print(r.text)
print(r.url)

print ("\nTEST POST ====> ")


pload = {'username':'Olivia','password':'123'}
r = requests.post('https://httpbin.org/post',data = pload)
print(r.text)

print ("\nTEST POST 2 ====> ")

pload = {'username':'olivia','password':'123'}
r = requests.post('https://httpbin.org/post',data = pload)
r_dictionary= r.json()
print(r_dictionary['form'])


print ("\nTEST GRAPHHOPPER GET ====> ")
r = requests.get('https://graphhopper.com/api/1/route?point=49.932707,11.588051&point=50.3404,11.64705&vehicle=car&debug=true&key=40ca48a2-d89c-4762-8860-9161190af2f0&optimize=true')
print(r.text)


print ("\nTEST GRAPHHOPPER POST ====> ")

post_data = {
  "vehicles": [
    {
      "vehicle_id": "vehicle-1",
      "type_id": "cargo-bike",
      "start_address": {
        "location_id": "berlin",
        "lon": 13.406,
        "lat": 52.537
      },
      "earliest_start": 1554804329,
      "latest_end": 1554808329,
      "max_jobs": 3
    },
    {
      "vehicle_id": "vehicle-2",
      "type_id": "cargo-bike",
      "start_address": {
        "location_id": "berlin",
        "lon": 13.406,
        "lat": 52.537
      },
      "earliest_start": 1554804329,
      "latest_end": 1554808329,
      "max_jobs": 3,
      "skills": [
        "physical strength"
      ]
    }
  ],
  "vehicle_types": [
    {
      "type_id": "cargo-bike",
      "capacity": [
        10
      ],
      "profile": "bike"
    }
  ],
  "services": [
    {
      "id": "s-1",
      "name": "visit-Joe",
      "address": {
        "location_id": "13.375854_52.537338",
        "lon": 13.375854,
        "lat": 52.537338
      },
      "size": [
        1
      ],
      "time_windows": [
        {
          "earliest": 1554805329,
          "latest": 1554806329
        }
      ]
    },
    {
      "id": "s-2",
      "name": "serve-Peter",
      "address": {
        "location_id": "13.393364_52.525851",
        "lon": 13.393364,
        "lat": 52.525851
      },
      "size": [
        1
      ]
    },
    {
      "id": "s-3",
      "name": "visit-Michael",
      "address": {
        "location_id": "13.416882_52.523543",
        "lon": 13.416882,
        "lat": 52.523543
      },
      "size": [
        1
      ]
    },
    {
      "id": "s-4",
      "name": "do nothing",
      "address": {
        "location_id": "13.395767_52.514038",
        "lon": 13.395767,
        "lat": 52.514038
      },
      "size": [
        1
      ]
    }
  ],
  "shipments": [
    {
      "id": "7fe77504-7df8-4497-843c-02d70b6490ce",
      "name": "pickup and deliver pizza to Peter",
      "priority": 1,
      "pickup": {
        "address": {
          "location_id": "13.387613_52.529961",
          "lon": 13.387613,
          "lat": 52.529961
        }
      },
      "delivery": {
        "address": {
          "location_id": "13.380575_52.513614",
          "lon": 13.380575,
          "lat": 52.513614
        }
      },
      "size": [
        1
      ],
      "required_skills": [
        "physical strength"
      ]
    }
  ],
  "objectives": [
    {
      "type": "min",
      "value": "vehicles"
    },
    {
      "type": "min",
      "value": "completion_time"
    }
  ],
  "configuration": {
    "routing": {
      "calc_points": True,
      "snap_preventions": [
        "motorway",
        "trunk",
        "tunnel",
        "bridge",
        "ferry"
      ]
    }
  }
}


r = requests.post(f'https://graphhopper.com/api/1/vrp/optimize?key={key}', json=post_data)
print(r.json)
print(r.text)

job_id = json.loads(r.text)["job_id"]

url = f'https://graphhopper.com/api/1/vrp/solution/{job_id}?key={key}'
r = requests.get(url)
print(r.text)


print("TEST GEOCODE =====>")

url = f'https://graphhopper.com/api/1/vrp/solution/{job_id}?key={key}'
r = requests.get(url)
print(r.text)

import pycep_correios
address = pycep_correios.get_address_from_cep('18085850')
aux_address = address['logradouro'].split(" ")
del(aux_address[0])
separator = ' '
address_name = separator.join(aux_address)

address_graph =  address_name+ ', ' + address['cidade'] + ', Brazil' 
# address = 'Darci Carvalho Daffernner, 18087-125 Sorocaba, Brazil'
# address_bruno = 'Waldomiro Fonda street, number 128, district Jardim Santa Lucia, 18078692, City Sorocaba, State Sao Paulo, Brazil'
url = f'https://graphhopper.com/api/1/geocode?q={address_graph}&key={key}&debug=true'
r = requests.get(url)
print(r.text)

rev = '-23.4754292,-47.4285757'
url = f'https://graphhopper.com/api/1/geocode?point={rev}&key={key}&debug=true&reverse=true'
r = requests.get(url)
print(r.text)
