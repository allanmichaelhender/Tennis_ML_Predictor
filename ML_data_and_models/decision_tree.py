import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import os
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
# from . import settings


# dataframe_path = os.path.join(settings.BASE_DIR, 'mysite', 'ML_ready_data.csv')


# dataframe = pd.read_csv(dataframe_path, index_col=0)
dataframe = pd.read_csv('ML_ready_data.csv', index_col=0)
                        
X = dataframe.drop(columns=["player1_win"])
y = dataframe['player1_win']
x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.2)

pipeline = Pipeline([("imputer",SimpleImputer(strategy='mean')), ('decision_tree', DecisionTreeClassifier(random_state=0))])

pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_test)

pipeline_score = pipeline.score(x_test, y_test)
decision_tree_model = pipeline.named_steps['decision_tree']

joblib.dump(pipeline, 'decision_tree_pipeline.joblib')

print(pipeline_score)
