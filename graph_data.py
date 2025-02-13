from user_mapping import user_data
import pandas as pd
from matplotlib import pyplot as plt

from pprint import pprint

pprint(user_data.head())


def userUniqueItem(columnName):
    uniqueItems = []

    for i in range(0,len(user_data)):
        if user_data[columnName][i] not in uniqueItems:
            uniqueItems.append(user_data[columnName][i])
    print(uniqueItems)

def userItems(columnName):
    items = []
    for i in range(0,len(user_data)):
        items.append(user_data[columnName][i])
    print(items)


userUniqueItem('city')
#userItems('region')