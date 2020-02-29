from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

class Forest:
    
    def __init__(self, data, target, predictors, maxLeafs):
        self.Data = data
        self.Target = target
        self.Predictors = predictors
        self.MaxLeafs = maxLeafs
        self.Algorithm = DecisionTreeRegressor(random_state=1, max_leaf_nodes=maxLeafs)

    def MakePredictions(self):
        x = self.Data[self.Predictors]
        y = self.Target

        #split data for verification and training
        x_train, x_val, y_train, y_val = train_test_split(x, y, random_state = 1)
        
        self.Algorithm.fit(x_train,y_train)

        self.TrainingPredictions = self.Algorithm.predict(x_train)
        self.TrainingMEA = mean_absolute_error(y_train, self.TrainingPredictions)
        self.TrainingR2 = r2_score(y_train, self.TrainingPredictions)
        
        self.ValidationPredictions = self.Algorithm.predict(x_val)
        self.ValidationMEA = mean_absolute_error(y_val, self.ValidationPredictions)
        self.ValidationR2 = r2_score(y_val, self.ValidationPredictions)
        
    



