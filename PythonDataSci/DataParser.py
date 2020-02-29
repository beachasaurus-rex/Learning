from DataModels import Forest
import pandas as pd
from statistics import mean

def GetData(filePath):
    data = pd.read_csv(filePath)
    #just drop missing values.
    #deal with missing values in more effective ways later. just learning for now.
    data.dropna(axis=0)
    return data

def PreprocessCategories(data, dfs):
    if dfs != None:
        for df in dfs:
            df = pd.get_dummies(df[1])
            data.update(df)
    return data
        
def LogStepList(baseNum):
    logList = []
    for i in range(1, 5):
        logList.append(baseNum ** i)
    return logList

def FineStepList(rangeList):
    fineList = []
    step = rangeList[1] // rangeList[0]
    for i in range(rangeList[0], rangeList[1], step):
        fineList.append(i)
    return fineList

def GetFineSearchRange(aggdList):
    meaList = []
    for subList in aggdList:
        meaList.append(subList[1])

    i = 1
    minVal = min(meaList)
    for subList in aggdList:
        if subList[1] == minVal:
            if i == 1:
                x = aggdList[i+1]
                stop = x[0]
                start = subList[0] * 10 ** -1
            elif i == (len(aggdList) - 1):
                x = aggdList[i-1]
                start = x[0]
                stop = subList[0] * 10 ** 1
            else:
                x = aggdList[i-1]
                start = x[0]
                x = aggdList[i+1]
                stop = x[0]
            rangeList = [start, stop]
            return rangeList
        i = i + 1

def GetMinErrPrediction(fineAggdList):
    meaList = []
    for subList in fineAggdList:
        meaList.append(subList[1])

    minVal = min(meaList)
    for subList in fineAggdList:
        if subList[1] == minVal:
            return subList

def GetPredictions(data, target, predictors, maxLeafs, dataModel):
    results = {}
    if dataModel == "Forest":
        model = Forest(data, target, predictors, maxLeafs)
        model.MakePredictions()

    
    trainingMean = model.TrainingPredictions.mean()
    results["MaxLeafs"] = model.MaxLeafs
    
    results["TrainingMean"] = trainingMean
    results["TrainingPredictions"] = model.TrainingPredictions
    results["TrainingMEA"] = model.TrainingMEA
    results["TrainingR2"] = model.TrainingR2
    
    validationMean = model.ValidationPredictions.mean()
    results["ValidationMean"] = validationMean
    results["ValidationPredictions"] = model.ValidationPredictions
    results["ValidationMEA"] = model.ValidationMEA
    results["ValidationR2"] = model.ValidationR2

    return results
    
def PrintResults(results):
    #trRelAcc = 1 - (abs(results["TrainingMean"] - results["TrainingMEA"]) / results["TrainingMean"])
    #valRelAcc = 1 - (abs(results["ValidationMean"] - results["ValidationMEA"]) / results["ValidationMean"])

    print("Max Leafs - %d" %results["MaxLeafs"])
    print("\nTraining Results:")
    #print(results["TrainingPredictions"])
    print("MEA: {0}".format(results["TrainingMEA"]))
    print("R2: {0}".format(results["TrainingR2"]))
    #print("Mean % Accuracy: {0}".format(trRelAcc))
    print("\nValidation Results:")
    #print(results["ValidationPredictions"])
    print("MEA: {0}".format(results["ValidationMEA"]))
    print("R2: {0}".format(results["ValidationR2"]))
    #print("Mean % Accuracy: {0}".format(valRelAcc))
    print("\n\n\n")
