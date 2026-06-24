from lightgbm import LGBMRegressor


class LightGBMTrainer:

    def __init__(self):

        self.model = LGBMRegressor(
            n_estimators=500,
            learning_rate=0.05,
            max_depth=8,
            random_state=42
        )

    def train(self,x_train,y_train):

        print("Training LightGBM...")
        self.model.fit(x_train,y_train)
        return self.model

    def predict(self,x_test):
        return self.model.predict(x_test)