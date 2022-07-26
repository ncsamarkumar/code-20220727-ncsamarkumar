"""
All helper functions
"""

from collections.abc import Iterable
import csv
from decimal import Decimal


def flatten(lis):
    """
    This function make multiple lists to single list and then yeilds it
    i.e [a,[b,c,[d,e]]] -> [a,b,c,d,e]
    :param lis: a list object

    """
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for _ in flatten(item):
                yield _
        else:
            yield item


def to_csv(data, file_name, header="", mode='w'):
    """
    To export data to csv
    :param data: list of lits which contains data
    :param file_name: file_name to save the file
    :param header: Column headers for csv
    :param mode: To specify the mode we need to read
                i.e w - to write, a- to append etc
    """

    with open(file_name + '.csv', mode, encoding='UTF8', newline='') as f_obj:
        writer = csv.writer(f_obj)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)


def count_elements(lista):
    """
    This function with count number of occurances of Bmi Category
    :param lista: List of list of data
    :return:
    """
    weight_criteria = [str(item[4]) for item in lista]

    output = {}

    for item in set(weight_criteria):
        output[item] = weight_criteria.count(item)

    return output


def remove_exponent(dec_no):
    """
    This function will remove trailing zeros from decimal
    i.e 25.0 to 25
    :param dec_no : a number.
    """

    return dec_no.quantize(Decimal(1)) if dec_no == dec_no.to_integral() else dec_no.normalize()
