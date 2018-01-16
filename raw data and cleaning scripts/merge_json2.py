import json
from operator import itemgetter
from itertools import groupby

def mergeJson():
    jsonFile1 = open("data_foreigner_clean.json", "r")
    data1 = json.load(jsonFile1)
    jsonFile1.close()
    jsonFile2 = open("data_births_clean.json", "r")
    data2 = json.load(jsonFile2)
    jsonFile2.close()
    jsonFile3 = open("data_algii_clean.json", "r")
    data3 = json.load(jsonFile3)
    jsonFile3.close()
  

    sort1 = open("data_foreigner_match.json", "w")
    sort2 = open("data_births_match.json", "w")
    sort3 = open("data_algii_match.json","w")
    array1 = []
    array2 = []
    array3 = []

    for index1, val1 in enumerate(data1):
        for index2, val2 in enumerate(data2):
            for index3, val3 in enumerate(data3):
                if val1["districtNumber"] == val2["districtNumber"] == val3["districtNumber"] and val1["year"] == val2["year"] == val3["year"] and val1["shape"] == val2["shape"] == val3["shape"]:
                    array1.append(val1)
                    array2.append(val2)
                    array3.append(val3)
              
    sort1.write(json.dumps(array1))
    sort2.write(json.dumps(array2))
    sort3.write(json.dumps(array3))
                    

    sort1.close()
    sort2.close()
    sort3.close()

              


    


mergeJson()
                
