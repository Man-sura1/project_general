from collections import OrderedDict
regionName,mag,region_Name=[],[],[]
def sortFile():
    with open(r"earthquakes.txt",'r') as file:
        for line in file:
            line=line.split()
            regionName.append(line[7:])
            mag.append(line[1])
    mag.pop(0)
    regionName.pop(0)
    newMag=[float(i) for i in mag]
    for i in regionName:
        string=' '.join(f for f in i)
        region_Name.append(string)
    global earthDict
    earthDict={}
    for i in region_Name:
        if i not in earthDict:
            earthDict[i]=[0]*6
    for i,j in zip(region_Name,newMag):
        if 5<=j<=5.9:
            earthDict[i][1]+=1
            earthDict[i][5]+=1
        elif 6<=j<=6.9:
            earthDict[i][2]+=1
            earthDict[i][5]+=1
        elif 7<=j<=7.9:
            earthDict[i][3]+=1
            earthDict[i][5]+=1
        elif 8<=j:
            earthDict[i][4]+=1
            earthDict[i][5]+=1
        else:
            earthDict[i][0]+=1
    earthDict=OrderedDict(sorted(earthDict.items()))
    return earthDict



def classifyFile():
    global overall
    global names
    global sumN
    global MaxName
    global earthDict
    sumN=0          
    names,inconsequential,moderate,strong,major,great,overall=[],[],[],[],[],[],[]
    for i,j in earthDict.items():
        names.append(i)
        inconsequential.append(j[0])
        moderate.append(j[1])
        strong.append(j[2])
        major.append(j[3])
        great.append(j[4])
        overall.append(j[5])
    for i in overall:
        sumN+=float(i)
    
    MaxName=names[overall.index(max(overall))]
        
def generateReport():
    earthDict=sortFile()
    classifyFile()
    reportName=input("Enter destination file name: ")
    with open(reportName,'a') as file:
        file.write(f"{'Region':<60} {'Incons.':<10} {'Moderate':<10} {'Strong':<10} {'Great':<10} {'Major':<10} {'Overall':<10}\n")
        for o,n in earthDict.items():
            file.write(f'{o:<60} {n[0]:<10} {n[1]:<10} {n[2]:<10} {n[3]:<10} {n[4]:<10} {n[5]:<10}\n')
    line1=f'TOTAL NUMBER OF EARTHQUAKES OF MAGNITUDE>=5.0 DURING THE PERIOD 2011/03/06-2021/03/12: {sumN}'
    line2=f'REGIONS WITH THE HIGHEST NUMBER OF EARTHQUAKES: {MaxName} {max(overall)}'
    with open('summary.txt','w') as file:
        file.write(f'{line1}\n{line2}\n')
    print('Processing Complete')
generateReport()
    
