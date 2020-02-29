import DataParser as dp
from sklearn.preprocessing import LabelEncoder

#path to data
path = "D:\My_Data\GithubRepos\Tutorials\PythonDataSci\melb_data.csv"

#prepare data
data = dp.GetData(path)

#print(data)

#print(data.columns)

#set what i want to predict
target = data.Price

#set my predictors
data['Suburb_enc'] = LabelEncoder().fit_transform(data['Suburb'])
#data['SellerG_enc'] = LabelEncoder().fit_transform(data['SellerG'])
predictors = ['Car', 'Rooms', 'Bathroom', 'Landsize', 'Suburb_enc']

bigSteps = dp.LogStepList(10)

aggdResults = []
for leafStep in bigSteps:
    #select and use a data model
    results = dp.GetPredictions(data, target, predictors, leafStep, "Forest")
    
    aggdResults.append([leafStep, results["ValidationMEA"]])
    
    #print results
    dp.PrintResults(results)


#fineRange = dp.GetFineSearchRange(aggdResults)
#fineList = dp.FineStepList(fineRange)
#aggdResults = []
#for fineStep in fineList:
    #select and use a data model
#    results = dp.GetPredictions(data, target, predictors, fineStep, "Forest")
#    aggdResults.append([fineStep, results["ValidationMEA"], results])

#results = dp.GetMinErrPrediction(aggdResults)
#print("Fine Search Results: \n")
#dp.PrintResults(results[2])
