
from Customer_churn.entity.config_entity import ModelPredictionConfig
import sys
import pandas as pd
from Customer_churn.exception import CustomException
from Customer_churn.utils.common import load_object

class ModelPrediction:
    def __init__(self, model_prediction_config: ModelPredictionConfig):
        self.config = model_prediction_config
    
    def predict(self,features):
        try:
            model_path = self.config.model_path
            preprocessor_path = self.config.preprocessor_obj_file_path
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(self,
        CreditScore: str,
        Gender: str,
        Age,
        Tenure: str,
        Balance: str,
        NumOfProducts: int,
        HasCrCard: int,
        IsActiveMember: int,
        EstimatedSalary: str,
        SatisfactionScore: str,
        CardType: str,
        PointEarned: str):

        self.CreditScore = CreditScore
        self.Gender = Gender
        self.Age = Age
        self.Tenure = Tenure
        self.Balance = Balance
        self.NumOfProducts = NumOfProducts
        self.HasCrCard = HasCrCard
        self.IsActiveMember = IsActiveMember,
        self.EstimatedSalary = EstimatedSalary
        self.SatisfactionScore = SatisfactionScore
        self.CardType = CardType
        self.PointEarned = PointEarned

    def get_data_as_dataframe(self):

        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
