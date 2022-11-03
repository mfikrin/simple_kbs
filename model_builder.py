import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text;

# Import metrics untuk pengukuran performa model
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
data = pd.read_csv("MZVAV-1.csv")
# Splitting the Data

# Test size ratio
# 80% data training dan 20% data testing
TEST_SIZE_RATIO = 0.2

# Feature names
data_feature_names = data.columns[1:17]
data_feature_names

# Store the feature datas
data_x = data.iloc[:, 1:17]

# Store the target data
data_y = data.iloc[:, 17]

# Split the data using Scikit-Learn's train_test_split
data_x_train, data_x_test, data_y_train, data_y_test = train_test_split(data_x, data_y, test_size=TEST_SIZE_RATIO, random_state=12)

dtl_model = DecisionTreeClassifier()

dtl_model.fit(data_x_train, data_y_train)

# dtl_export = export_text(clf, feature_names=data_feature_names.tolist())

# Generating prediction models
dtl_y_test_prediction = dtl_model.predict(data_x_test)

dtl_test_accuracy = accuracy_score(data_y_test, dtl_y_test_prediction)
dtl_test_f1 = f1_score(data_y_test, dtl_y_test_prediction)

inputDataFrame = pd.DataFrame([[68,55.04,32,68,75.2,0,0,0,0,0,0,0,0,0.04,0,0]], columns=data_feature_names.tolist())
result = dtl_model.predict(inputDataFrame)
print(result)

joblib.dump(dtl_model, 'classifier.pkl')