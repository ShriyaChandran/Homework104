import csv
from collections import Counter
with open('SOCR-HeightWeight.csv', newline="") as f:
    reader=csv.reader(f)
    fileData=list(reader) 

fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    num=fileData[i][1]
    newData.append(float(num))

n=len(newData)
data= Counter(newData)
modeDataForRange= {
    "75-95": 0,
    "95-115": 0,
    "115-135": 0,
    "135-155":0,
    "155-175":0
}
for height, occurence in data.items():
    if(75<float(height)<95):
        modeDataForRange["75-95"]+=occurence
    elif(95<float(height)<115):
        modeDataForRange["115-135"]+=occurence
    elif(135<float(height)<155):
        modeDataForRange["135-155"]+=occurence
    elif(155<float(height)<175):
        modeDataForRange["155-175"]+=occurence

mode_range, mode_occurence=0,0
for range, occurence in modeDataForRange.items():
    if(occurence>mode_occurence):
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode = float((mode_range[0]+mode_range[1])/2)
print(f"mode is: {mode: 2f}")