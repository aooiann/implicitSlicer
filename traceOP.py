
def traceMain(branchList,indexList):
    tracepnt=[]
    tracepnt.append(branchList[0][0])
    tracepnt.append(branchList[0][1])
    num=len(branchList)
    k=0
   
    while k<num:
        sig=k
        for i in range(1,len(branchList)):
            strPnt=tracepnt[0]
            endPnt=tracepnt[len(tracepnt)-1]
            
            if branchList[i][0]==endPnt and i not in indexList :
                indexList.append(i) 
                k+=1
                tracepnt.append(branchList[i][1])
            
            if branchList[i][1]==endPnt and i not in indexList :
                indexList.append(i) 
                k+=1
                tracepnt.append(branchList[i][0])
                
            if branchList[i][0]==strPnt and i not in indexList :
                indexList.append(i) 
                k+=1
                tracepnt.insert(0,branchList[i][1])
            
            if branchList[i][1]==strPnt and i not in indexList :
                indexList.append(i) 
                k+=1
                tracepnt.insert(0,branchList[i][0])
                   
        if k==sig:
            return tracepnt   

    return tracepnt 

def createBranch(listLine,idList):
    newListLine=[]
    for i in range(len(listLine)):
        if i not in idList:
            newListLine.append(listLine[i])
    return newListLine

def decideEnd(idList,listLine):
    num=0
    tarNum=len(listLine)

    for list in idList:
            num=num+len(list)
    return num<tarNum
         
def trace(listLine):
    pntPath=[]
    idList=[]
    branches=listLine

    while decideEnd(idList,listLine):
        ids=[]
        ids.append(0)
        pntPath.append(traceMain(branches,ids))
        idList.append(ids)
        branches=createBranch(branches,ids)
    
    return pntPath