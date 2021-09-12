import pandas as pd

def search(list, platform):
    for i in range(len(list)):
        if list[i].replace(" ","") == platform.replace(" ",""):
            return True
    return False

first_excel=pd.read_excel('studentrole.xlsx')
second_excel=pd.read_excel('justpubliccourse.xlsx')


firstList = first_excel['name'].tolist()
secondList = second_excel['name'].tolist()

resultUserFoundList=[]
resultUserNotFoundList=[]
for i in secondList:
    if search(firstList, i):
        resultUserFoundList.append(i)
    else:
        resultUserNotFoundList.append(i)

with open("userFindMode7.txt", "w",encoding="utf-8") as output:
    for item in resultUserFoundList:
        output.write("%s\n" % item)
with open("userNotFindMode7.txt", "w",encoding="utf-8") as output:
    for item in resultUserNotFoundList:
        output.write("%s\n" % item)
