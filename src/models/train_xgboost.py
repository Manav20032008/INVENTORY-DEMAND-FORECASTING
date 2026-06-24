from xgboost import XGBRegressor

class XGBoostTainer :

    def __init__(self):
        
        self.model = XGBRegressor(
            n_estimators = 500 ,
            learning_rate = 0.05 ,
            max_depth = 8,
            subsample = 0.8,
            colsample_bytree = 0.8,
            random_state = 45 ,
            n_jobs = -1
        )

    def train(self,x_train,y_train):
        print("Training XGBoost ...")

        self.model.fit(
            x_train,y_train
        )
        return (self.model)
    
    def predict(self, x_test):

        return self.model.predict(x_test)