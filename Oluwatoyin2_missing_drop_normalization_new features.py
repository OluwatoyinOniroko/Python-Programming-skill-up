import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import preprocessing

#Question 1
# Read a dataset with missing values
Analytic_data = pd.read_csv("C:/Users/HP/OneDrive/Desktop/Ty  - Fall 2023/Programming/Py file/Wk 3/Datasets/2017CHR_CSV_Analytic_Data-new.csv")

# Select the rows that have at least one missing value
Analytic_top = Analytic_data[Analytic_data.isnull().any(axis=1)].head()
print(Analytic_top)

#check the missing value in each of the column
column_missing_value = Analytic_data.isnull().sum()
print(column_missing_value)

#check if there are any columns with missing values
if column_missing_value.empty:
    print("column missing value")
    print(column_missing_value)

#Impute missing values (for example, fill with the mean)
    Analytic_data.fillna(Analytic_data.mean(), inplace=True)

#Question 2
#Drop(remove) the identifier column
dropped_columns = ["5-Digit FIPS Code", "statecode", "countycode", "county"]
Analytic_data.drop(columns=dropped_columns, inplace=True)
print(Analytic_data)

#Question 3
#Use Z-score to normalize columns
Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']] = Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']].fillna(Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']].mean())
print(Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']])

#Applying Z-score normalization
scaler = preprocessing.StandardScaler()
Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']] = scaler.fit_transform(Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']])
print(Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']])

#Question 4
#Create a new column “Diabetes-level” by coding the “Diabetes Value” into four groups
bins = [0, 25, 50, 75, 100]
labels = ['low', 'median low', 'median high', 'high']
Analytic_data['Diabetes-level'] = pd.cut(Analytic_data['Diabetes Value'], bins=bins, labels=labels)
print(Analytic_data['Diabetes-level'])

""""
# Alternative Solution to Question 3
#Use Z-score to normalize columns
scaler = preprocessing.StandardScaler()
normalized_column = Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']]
mean_std = Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']].mean(), Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']].std()
Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']] = (Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']] - mean_std[0]) / mean_std[1]
print(Analytic_data[['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value']])


#Bonus trial optional
#Apply feature selection to find the top five features relevant to "Diabetes-level
y = Analytic_data["Diabetes-level"]
X = Analytic_data.drop(['Diabetes Value', 'Diabetes Value'], axis=1)

selector = Select.(score_func=mutual_info_classif, k=5)
X_new = selector.fit_transform(X, y)
selected_feature_indices = selector.get_support(indices=True)
elected_features = X.columns[selected_feature_indices]
print("Top 5 selected features:")
print(selected_features)
"""













