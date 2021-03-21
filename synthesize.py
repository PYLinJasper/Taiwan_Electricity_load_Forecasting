import argparse
import pandas as pd
import numpy as np
import sklearn
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # training data import
    parser.add_argument('--path', default='台北天氣',
    help='input path name')

    args = parser.parse_args()

    nowPath = os.getcwd()
    # print(nowPath)
    newPath = nowPath + '/' + args.path + '/'
    os.chdir(newPath)
    # print(os.getcwd())
    
    # allFile = os.listdir()
    # # print(allFile)
    # newAllFile = []
    # for fileName in allFile:
    #     if fileName[len(fileName)-4:] == '.csv':
    #         newAllFile.append(fileName)
    # # print(newAllFile)

    allDoc = pd.read_csv('1.csv')
    allDoc = allDoc.drop(index = [0])
    for index in range(2,28):
        # print(index)
        temp = pd.read_csv('%d.csv'%index)
        temp = temp.drop(index = [0])
        allDoc = pd.concat([allDoc, temp], ignore_index=True)

    os.chdir(newPath + 'allTemp')
    allDoc.to_csv(args.path + '.csv', index=0)