import pandas as pd
import numpy as np
dataset = pd.read_csv("diabetes.csv")
x = dataset.iloc[:, :8].values
y = dataset.iloc[:, 8:].values
y = np.ravel(y)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)
prd = classifier.predict(x_test)

from sklearn.metrics import classification_report, accuracy_score
print("Classification Report: \n", classification_report(y_test, prd))
print("Accuracy Rate: ", accuracy_score(y_test, prd))
