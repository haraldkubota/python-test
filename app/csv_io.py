import pandas as pd
import pprint

def readCSV(filename: str):
    data = pd.read_csv(filename, delimiter=',')
    return data

if __name__ == "__main__":
    data = readCSV('~/t/test.csv')
    index = data.count().keys()
    print(type(index))
    print(index)
    # for x in data:
    #         print(f'[{x}]={data[x]}')

