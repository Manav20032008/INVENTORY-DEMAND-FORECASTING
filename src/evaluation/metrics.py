import numpy as np
from sklearn.metrics import (mean_absolute_error,
                             mean_squared_error,
                             r2_score)

class RegressionMetrics :

    @staticmethod
    def mae(y_true, y_pred):
        return mean_absolute_error(y_true,y_pred)
    
    @staticmethod
    def rmse(y_true, y_pred):
        return np.sqrt(mean_squared_error(y_true,y_pred))
    
    @staticmethod
    def r2(y_true,y_pred):
        return r2_score(y_true,y_pred)
    
    @staticmethod
    def mape(y_true,y_pred):
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)
        mask = y_true != 0

        return (np.mean(
            np.abs((y_true[mask]-y_pred[mask])/y_true[mask])
            )*100)

    @staticmethod
    def evaluate(y_true,y_pred):

        results = {
            "MAE":RegressionMetrics.mae(y_true,y_pred),
            "RMSE":RegressionMetrics.rmse(y_true,y_pred),
            "R2":RegressionMetrics.r2(y_true,y_pred),
            "MAPE":RegressionMetrics.mape(y_true,y_pred)
        }

        return results