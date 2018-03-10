"""RATP_Watch.py: Gets schedule info for transports in Paris. Modify the requested URLs to make it your own.
If you run it it will print the info, once. For constant update and UI, use RATP-interfaceV2.py"""

__author__      = "Adrien Le Falher"

import requests




def parse_results(results):
    if 'DEVIATION' not in str(results):
        next_bus = results['result']['schedules'][0]['message'] + ' - DESTINATION ' + str(results['result']['schedules'][0]['destination'])
        last_bus = results['result']['schedules'][1]['message'] + ' - DESTINATION ' + str(results['result']['schedules'][0]['destination'])
        updated = results['_metadata']['date']
    else :
        next_bus = results['result']['schedules'][0]['message']
        last_bus = results['result']['schedules'][1]['message']
        updated = results['_metadata']['date']

    print(next_bus)
    print(last_bus)
    print(updated)
    print('\n')

    return next_bus, last_bus, updated



def get_95_morillons():
    print('LIGNE 95 - MORILLONS')
    m = requests.get('https://api-ratp.pierre-grimaud.fr/v3/schedules/bus/95/morillons/R')
    results = m.json()

    next_bus, last_bus, updated = parse_results(results)
    return next_bus, last_bus, updated




def get_89_brancion_vouille():
    print('LIGNE 89 - BRANCION VOUILLE')
    m = requests.get('https://api-ratp.pierre-grimaud.fr/v3/schedules/bus/89/brancion+vouille/A')

    results = m.json()
    # print(results)

    next_bus, last_bus, updated = parse_results(results)
    return next_bus, last_bus, updated


def get_62_brancion_vouille():
    print('LIGNE 62 - BRANCION VOUILLE')
    m = requests.get('https://api-ratp.pierre-grimaud.fr/v3/schedules/bus/62/brancion+vouille/R')

    results = m.json()

    next_bus, last_bus, updated = parse_results(results)
    return next_bus, last_bus, updated



def get_12_convention():
    error = False
    line = 'LIGNE M12 - CONVENTION'
    print(line)
    try:
        m = requests.get('https://api-ratp.pierre-grimaud.fr/v3/schedules/metros/12/convention/A')

        if '400' in str(m):
            error = True
            print(line + " Error")
            print(m.json())
    except Exception as e:
        print(e)
        print(line + " Error")
        error = True
        pass

    if not error:
        results = m.json()
        next_bus, last_bus, updated = parse_results(results)
        return next_bus, last_bus, updated


def get_velib():
    print("VELIB FRANQUET LABROUSTE - EN ATTENDANT MIEUX")
    m = requests.get("https://www.velib-metropole.fr/webapi/map/details?gpsTopLatitude=49&gpsTopLongitude=2.85&gpsBotLatitude=48.7&gpsBotLongitude=2&zoomLevel=19")

    for item in m.json():
        if "Franquet - Labrouste" in str(item):
            # print(item)
            bike = item['nbBike']
            ebike = item["nbEbike"]
            station = item["station"]['name']
            print(station)
            print("Vélo dispo : " + str(bike))
            print("Ebike dispo : " + str(ebike))
    print('\n')

    return bike, ebike

if __name__ == '__main__':
    get_velib()
    get_95_morillons()
    get_89_brancion_vouille()
    get_62_brancion_vouille()
    get_12_convention()