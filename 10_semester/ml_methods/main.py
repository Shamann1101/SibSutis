import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler as ss
from sklearn.tree import DecisionTreeClassifier
from tabulate import tabulate


def prepare_data(filename='data.csv'):
    df = pd.read_csv(filename, header=None)

    df.columns = ['age', 'sex', 'cp', 'trestbps', 'chol',
                  'fbs', 'restecg', 'thalach', 'exang',
                  'oldpeak', 'slope', 'ca', 'thal', 'goal']

    df.isnull().sum()

    df['goal'] = df.goal.map({0: 0, 1: 1, 2: 1, 3: 1, 4: 1})
    df['thal'] = df.thal.fillna(df.thal.mean())
    df['ca'] = df.ca.fillna(df.ca.mean())

    data_x = df.iloc[:, :-1].values
    data_y = df.iloc[:, -1].values

    return data_x, data_y


def get_accuracy(data_x, data_y, max_depth=4, test_size=0.3):
    x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=test_size)

    sc = ss()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    classifier = DecisionTreeClassifier(max_depth=max_depth)
    classifier.fit(x_train, y_train)

    y_pred = classifier.predict(x_test)
    cm_test = confusion_matrix(y_pred, y_test)

    y_pred_train = classifier.predict(x_train)
    cm_train = confusion_matrix(y_pred_train, y_train)

    return [
        (cm_train[0][0] + cm_train[1][1]) / len(y_train),
        (cm_test[0][0] + cm_test[1][1]) / len(y_test)
    ]


def main():
    accuracy = []
    sum_learn = 0
    sum_test = 0
    data_x, data_y = prepare_data()
    for i in range(10):
        accuracy.append(get_accuracy(data_x, data_y))
        sum_learn = sum_learn + accuracy[i][0]
        sum_test = sum_test + accuracy[i][1]

    print(tabulate(accuracy, headers=['Learn', 'Test']))
    print('Learn Avg: ' + str(sum_learn / len(accuracy)))
    print('Test Avg: ' + str(sum_test / len(accuracy)))


if __name__ == '__main__':
    main()
