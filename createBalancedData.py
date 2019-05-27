import pandas as pd
import praw
import csv
import time
import random


def createBalancedData():
    everything = db
    alldata = db[['id', 'num_comments', 'locked']]
    dbL = pd.DataFrame(columns=['id', 'num_comments', 'locked'])
    dbnL = pd.DataFrame(columns=['id', 'num_comments', 'locked'])
    q=0
    v=0
    comLockedCount = 0
    comNotLockedCount = 0
    for index, row in alldata.iterrows():
        if row[2]:
            dbL.loc[q] = row
            q+=1
            comLockedCount += row[1]
        elif row[2] == False:
            dbnL.loc[v] = row
            comNotLockedCount += row[1]
            v+=1

    sortedListLocked = dbL.sort_values(by='num_comments', ascending=False)
    sortedListNotLocked = dbnL.sort_values(by='num_comments', ascending=False)
    count_rowL = sortedListLocked.shape[0]
    count_rownL = sortedListNotLocked.shape[0]

    distributeL = round(comLockedCount/10)
    distributenL = round(comNotLockedCount/10)

    part1 = distributeL
    partnL = distributenL
    print(comLockedCount)
    print(comNotLockedCount)
    idnumbers1 = []
    idnumbers2 = []
    idnumbers3 = []
    idnumbers4 = []
    idnumbers5 = []
    idnumbers6 = []
    idnumbers7 = []
    idnumbers8 = []
    idnumbers9 = []
    idnumbers10 = []


    i=0
    x=1
    for index, row in sortedListLocked.iterrows():
        i += row[1]

        if (i<part1 and x==1):
            idnumbers1.append(row[0])
            i += row[1]
        elif (x == 1):
            x += 1
            i = 0

        if (i < part1 and x == 2):
            i += row[1]
            idnumbers2.append(row[0])
        elif (x == 2):
            x += 1
            i = 0

        if (i < part1 and x == 3):
            i += row[1]
            idnumbers3.append(row[0])

        elif (x == 3):
            x += 1
            i = 0

        if (i < part1 and x ==4):
            i += row[1]
            idnumbers4.append(row[0])
        elif (x == 4):
            x += 1
            i = 0

        if (i < part1 and x ==5):
            i += row[1]
            idnumbers5.append(row[0])
        elif (x == 5):
            x += 1
            i = 0

        if (i < part1 and x ==6):
            i += row[1]
            idnumbers6.append(row[0])
        elif (x == 6):
            x += 1
            i = 0

        if (i < part1 and x ==7):
            i += row[1]
            idnumbers7.append(row[0])
        elif (x == 7):
            x += 1
            i = 0

        if (i < part1 and x ==8):
            i += row[1]
            idnumbers8.append(row[0])
        elif (x == 8):
            x += 1
            i = 0

        if (i < part1 and x ==9):
            i += row[1]
            idnumbers9.append(row[0])
        elif (x == 9):
            x += 1
            i = 0

        if (x ==10):
            i += row[1]
            idnumbers10.append(row[0])
    i = 0
    x = 1
    idnumbers1NL = []
    idnumbers2NL = []
    idnumbers3NL = []
    idnumbers4NL = []
    idnumbers5NL = []
    idnumbers6NL = []
    idnumbers7NL = []
    idnumbers8NL = []
    idnumbers9NL = []
    idnumbers10NL = []
    for index, row in sortedListNotLocked.iterrows():
        i += row[1]

        if (i<partnL and x==1):
            idnumbers1NL.append(row[0])
            i += row[1]
        elif (x == 1):
            x += 1
            i = 0

        if (i < partnL and x == 2):
            i += row[1]
            idnumbers2NL.append(row[0])
        elif (x == 2):
            x += 1
            i = 0

        if (i < partnL and x == 3):
            i += row[1]
            idnumbers3NL.append(row[0])

        elif (x == 3):
            x += 1
            i = 0

        if (i < partnL and x ==4):
            i += row[1]
            idnumbers4NL.append(row[0])
        elif (x == 4):
            x += 1
            i = 0

        if (i < partnL and x == 5):
            i += row[1]
            idnumbers5NL.append(row[0])
        elif (x == 5):
            x += 1
            i = 0

        if (i < partnL and x == 6):
            i += row[1]
            idnumbers6NL.append(row[0])
        elif (x == 6):
            x += 1
            i = 0

        if (i < partnL and x == 7):
            i += row[1]
            idnumbers7NL.append(row[0])
        elif (x == 7):
            x += 1
            i = 0

        if (i < partnL and x == 8):
            i += row[1]
            idnumbers8NL.append(row[0])
        elif (x == 8):
            x += 1
            i = 0

        if (i < partnL and x == 9):
            i += row[1]
            idnumbers9NL.append(row[0])
        elif (x == 9):
            x += 1
            i = 0

        if (x ==10):
            i += row[1]
            idnumbers10NL.append(row[0])

    # print(idnumbers2)
    # print(idnumbers1)
    # print(idnumbers3)
    # print(idnumbers4)
    # print(idnumbers5)
    scaling = 0.87
    ratio1 = (len(idnumbers1NL) / len(idnumbers1))*scaling
    ratio2 = (len(idnumbers2NL) / len(idnumbers2))*scaling
    ratio3 = (len(idnumbers3NL) / len(idnumbers3))*scaling
    ratio4 = (len(idnumbers4NL) / len(idnumbers4))*scaling
    ratio5 = (len(idnumbers5NL) / len(idnumbers5))*scaling
    ratio6 = (len(idnumbers6NL) / len(idnumbers6))*scaling
    ratio7 = (len(idnumbers7NL) / len(idnumbers7))*scaling
    ratio8 = (len(idnumbers8NL) / len(idnumbers8))*scaling
    ratio9 = (len(idnumbers9NL) / len(idnumbers9))*scaling
    ratio10 = (len(idnumbers10NL) / len(idnumbers10))*scaling

    print(ratio1, ratio2, ratio3, ratio4, ratio5, ratio6, ratio7, ratio8, ratio9, ratio10)
    tussendata = pd.DataFrame(columns=['id', 'locked', 'name', 'archived', 'created_utc', 'num_comments', 'score', 'upvote_ratio', 'comments_body'])
    print(everything.shape)
    w = 0

    for id in idnumbers1:

        amnt_dupl = round((random.uniform(0, 1) - 0.5) + ratio1)
        print(amnt_dupl)
        for index, row in everything.iterrows():
            if row[0] == id:
                for i in range(amnt_dupl):
                    tussendata=tussendata.append(row, ignore_index=True)
                    #tussendata = tussendata.append({'id': row[0], 'locked': row[1], 'name':row[2], 'archived':row[4], 'created_utc':row[5], 'num_comments':row[6], 'score':row[7], 'upvote_ratio':row[8], 'comments_body':row[9]}, ignore_index=True)
                    #everything.loc[everything.size + 1] = row

    #everything= everything.append(tussendata, ignore_index=True)
    # print(everything.shape, w)
    # print(tussendata.shape, w)
    #
    # print(tussendata)
    # everything = everything.append(tussendata, ignore_index=True)
    # print(everything.shape, w)

    for id in idnumbers2:
        amnt_dupl = round((random.uniform(0, 1) - 0.5) + ratio2)
        for index, row in everything.iterrows():
            if row[0] == id:
                for i in range(amnt_dupl):
                    tussendata=tussendata.append(row, ignore_index=True)

    print(everything.shape)

    for id in idnumbers3:
        amnt_dupl = round((random.uniform(0, 1) - 0.5) + ratio3)

        for index, row in everything.iterrows():
            if row[0] == id:
                for i in range(amnt_dupl):
                    tussendata=tussendata.append(row, ignore_index=True)

    print(everything.shape)

    for id in idnumbers4:
        amnt_dupl = round((random.uniform(0, 1) - 0.5) + ratio4)

        for index, row in everything.iterrows():
            if row[0] == id:
                for i in range(amnt_dupl):
                    tussendata=tussendata.append(row, ignore_index=True)
    print(everything.shape)

    for id in idnumbers5:
        amnt_dupl = round((random.uniform(0, 1) - 0.5) + ratio5)

        for index, row in everything.iterrows():
            if row[0] == id:
                for i in range(amnt_dupl):
                    tussendata=tussendata.append(row, ignore_index=True)

    print(everything.shape)

    for id in idnumbers6:
        amnt_dupl = round((random.uniform(0, 1) - 0.5) + ratio6)

        for index, row in everything.iterrows():
            if row[0] == id:
                for i in range(amnt_dupl):
                    tussendata=tussendata.append(row, ignore_index=True)

    print(everything.shape)

    for id in idnumbers7:
        amnt_dupl = round((random.uniform(0, 1) - 0.5) + ratio7)

        for index, row in everything.iterrows():
            if row[0] == id:
                for i in range(amnt_dupl):
                    tussendata=tussendata.append(row, ignore_index=True)

    print(everything.shape)

    for id in idnumbers8:
        amnt_dupl = round((random.uniform(0, 1) - 0.5) + ratio8)

        for index, row in everything.iterrows():
            if row[0] == id:
                for i in range(amnt_dupl):
                    tussendata=tussendata.append(row, ignore_index=True)

    print(everything.shape)

    for id in idnumbers9:
        amnt_dupl = round((random.uniform(0, 1) - 0.5) + ratio9)

        for index, row in everything.iterrows():
            if row[0] == id:
                for i in range(amnt_dupl):
                    tussendata=tussendata.append(row, ignore_index=True)

    print(everything.shape)

    for id in idnumbers10:
        amnt_dupl = round((random.uniform(0, 1) - 0.5) + ratio10)
        for index, row in everything.iterrows():
            if row[0] == id:
                for i in range(amnt_dupl):
                    tussendata=tussendata.append(row, ignore_index=True)
    #'call database and 5x idnumbers1 verdubbelen, 3x idnumbers2 en 2x idnumbers3'
    everything = everything.append(tussendata, ignore_index=True)
    print(everything.shape)


    comLockedCount = 0
    comNotLockedCount = 0
    alldata = everything[['id', 'num_comments', 'locked']]

    for index, row in alldata.iterrows():
        if row[2]:
            comLockedCount += row[1]
        elif row[2] == False:
            comNotLockedCount += row[1]


    print(comLockedCount)
    print(comNotLockedCount)
    return(everything)

if __name__ == '__main__':
    db = pd.read_csv("submissiondatabase1558829476.6550424.csv")
    newbd = createBalancedData()
    newbd.to_csv('balanced_submissiondatabase1558829476.6550424.csv', sep='\t', encoding='utf-8')
    db = pd.read_csv("balanced_submissiondatabase1558829476.6550424.csv", error_bad_lines=False)


