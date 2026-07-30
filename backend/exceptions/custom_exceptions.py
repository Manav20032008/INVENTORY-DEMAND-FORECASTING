class model_not_found_execption(Exception):

    def __init__(self,message="Model file not found."):
        self.message = message
        super().__init__(self.message)

class predictiob_execption(Exception):

    def __init__(self,message="Prediction failed."):
        self.message = message
        super().__init__(self.message)

        