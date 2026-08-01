class ModelNotFoundException(Exception):
    def __init__(self, message: str = "Model file not found."):
        self.message = message
        super().__init__(self.message)


class PredictionException(Exception):
    def __init__(self, message: str = "Prediction failed."):
        self.message = message
        super().__init__(self.message)


model_not_found_execption = ModelNotFoundException
predictiob_execption = PredictionException
