#-*- coding: iso-8859-15 -*-
import json
from operator import itemgetter
from itertools import groupby



def formatForeigner():
    jsonFile = open("foreigner_quote.json", "r")  # Open the JSON file for reading
    data = json.load(jsonFile)  # Read the JSON into the buffer
    jsonFile.close()  # Close the JSON file

    for idx, val in enumerate(data):

        # delete expendable entries
        del val['INDIKATOR_GRUPPE']
        del val['INDIKATOR_BEZEICHNUNG']
        del val['NAME_BASISWERT1']
        del val['NAME_BASISWERT2']
        del val['NAME_BASISWERT3']
        del val['NAME_BASISWERT4']
        del val['NAME_BASISWERT5']
        del val['BASISWERT_3']
        del val['BASISWERT_4']
        del val['BASISWERT_5']
        del val['GLIEDERUNG']
        del val['NUMMER']
        
        # normalize comma to dot notation
        # val['BASISWERT_1'] = val['BASISWERT_1'].replace(",", ".")
        # val['BASISWERT_2'] = val['BASISWERT_2'].replace(",", ".")
        val['INDIKATOR_WERT'] = str(val['INDIKATOR_WERT']).replace(",", ".")
        # rename keys
        val['foreignerPercent'] = val.pop('INDIKATOR_WERT')
        val['foreignerPercent'] = val['foreignerPercent'].replace(",", ".")
        val['population'] = val.pop('BASISWERT_2')
        val['foreigners'] = val.pop('BASISWERT_1')
        val['shape'] = val.pop('INDIKATOR_AUSPRAEGUNG')
        val['year'] = val.pop('JAHR')
        val['district'] = val.pop('NAME')
        # extract district number to separate entry
        val['districtNumber'] = val['district'][:2].strip('0')
        val['district'] = val['district'][3:]

    data = [i for i in data if i['shape'] !=
            ' ' and i['district'] != 'dt M\u00c3\u00bcnchen']

    # Save changes to JSON file
    jsonFile = open("data_foreigner_clean.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()


formatForeigner()
