import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix


def commercial():
    dataset = pd.read_csv("data/divorce2.csv")

    X = dataset.drop('Class', axis=1)
    Y = dataset['Class']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    return cm

def avg_commercial_error(testNumber: int):

    avgError = 0.0

    for i in range (testNumber):
        conf_matrix = commercial()
        successNumber = conf_matrix[0][0] + conf_matrix[1][1]
        tryNumber = successNumber + conf_matrix[0][1] + conf_matrix[1][0]

        avgError = avgError + (1-successNumber/tryNumber)

    avgError = avgError/testNumber
    avgError = float("{:.3f}".format(avgError))
    print("avg error : " + str(avgError))

