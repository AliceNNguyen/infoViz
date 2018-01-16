import json
from operator import itemgetter
from itertools import groupby


def formatAlgii():
    jsonFile = open("data_algii.json", "r")  # Open the JSON file for reading
    data = json.load(jsonFile)  # Read the JSON into the buffer
    jsonFile.close()  # Close the JSON file

    for idx, val in enumerate(data):

        # delete expendable entries
        del val['INDIKATOR_GRUPPE']
        del val['INDIKATOR_BEZEICHNUNG']
        del val['NAME_BASISWERT1']
        del val['NAME_BASISWERT2']
        # normalize comma to dot notation
        val['BASISWERT_1'] = val['BASISWERT_1'].replace(",", ".")
        val['BASISWERT_2'] = val['BASISWERT_2'].replace(",", ".")
        val['INDIKATOR_WERT'] = val['INDIKATOR_WERT'].replace(",", ".")
        # rename keys
        val['unemployedPercent'] = val.pop('INDIKATOR_WERT')
        val['population'] = val.pop('BASISWERT_2')
        val['unemployed'] = val.pop('BASISWERT_1')
        val['shape'] = val.pop('INDIKATOR_AUSPRAEGUNG')
        val['year'] = val.pop('JAHR')
        val['district'] = val.pop('NAME')
        # extract district number to separate entry
        val['districtNumber'] = val['district'][:2].strip('0')
        val['district'] = val['district'][3:]

    data = [i for i in data if i['shape'] !=
            'gesamt' and i['district'] != 'dt Munchen']

    # Save changes to JSON file
    jsonFile = open("data_algii_clean.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()


formatAlgii()
