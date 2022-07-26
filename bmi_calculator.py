"""
To read data and calculate BMI and its status
"""

import json

import bmi_main
import utils
from constants import HEADER,GENDER,RESULT,HEIGHTCM,WEIGHTKG

if __name__ == "__main__":

    FILE_PATH = 'bmi' #Declare file Path

    with open('data.json', 'r', encoding='utf-8') as data_obj:
        data = data_obj.read()
        data = json.loads(data)

        data_to_csv = []
        for arr in data:

            bmi_obj = bmi_main.BMI(arr.get(HEIGHTCM), arr.get(WEIGHTKG))
            bmi_value = bmi_obj.to_calculate_bmi() #Calulating BMI

            if isinstance(bmi_value, float):

                # Geting Healthrisk and category
                bmi_status = bmi_obj.compare_bmi()
            else:
                bmi_status = []

            bmi_cate = [
                        arr.get(GENDER),str(arr.get(HEIGHTCM)),
                        str(arr.get(WEIGHTKG)),str(bmi_value),
                        bmi_status
                        ]

            data_to_csv.append(list(utils.flatten(bmi_cate)))

    if data_to_csv:
        utils.to_csv(data_to_csv, FILE_PATH, HEADER, 'w')

    #Finding Observations
    stats = utils.count_elements(data_to_csv)
    for key, val in stats.items():
        RESULT.append([key] + [str(val)])
    utils.to_csv(RESULT, FILE_PATH, '', 'a')

    # To only get the bmi status if required
    # bmi_obj = bmi_main.BMI(bmi_value='26.05')
    # bmi_status = bmi_obj.compare_bmi()
    # print(bmi_status)
