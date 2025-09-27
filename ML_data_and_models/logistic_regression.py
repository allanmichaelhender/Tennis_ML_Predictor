from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV


dataframe = pd.read_csv('ML_ready_data.csv', index_col=0)
                        
X = dataframe.drop(columns=["player1_win"])
y = dataframe['player1_win']
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

#rank_points = Pipeline([("imputer",SimpleImputer(strategy='mean'))])
non_rank_points = Pipeline([("imputer",SimpleImputer(strategy='mean')), ("scale",StandardScaler())])

#rank_points_col = ["ranking_diff"]
non_rank_cols = X.columns#.drop(columns=["ranking_diff"]).columns

preprocess = ColumnTransformer(
    transformers=[
        #("rank_points_process", rank_points, rank_points_col),
        ("non_rank_process", non_rank_points, non_rank_cols)
    ]
)

lr = LogisticRegression(solver='liblinear', max_iter=1000)
parameters = {'penalty': ['l1', 'l2'], 'C': [1, 10, 100, 1000]}
clf = GridSearchCV(lr, parameters)
scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
clf.fit(x_train_scaled,y_train)
best_model=clf.best_estimator_
print(best_model)

logistic_regr_pipeline = Pipeline([("preprocess", preprocess), ("regr", best_model)])

logistic_regr_pipeline.fit(x_train, y_train)
y_pred = logistic_regr_pipeline.predict(x_test)

logistic_regr_pipeline_score = logistic_regr_pipeline.score(x_test, y_test)
print(logistic_regr_pipeline_score)

joblib.dump(logistic_regr_pipeline, 'logistic_regr_pipeline.joblib')