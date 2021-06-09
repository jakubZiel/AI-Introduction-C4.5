import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

dataset = pd.read_csv("data/divorce2.csv")

X = dataset.drop('Class', axis=1)
Y = dataset['Class']

for i in range(5):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    print(confusion_matrix(y_test, y_pred))

    print(classification_report(y_test, y_pred))
