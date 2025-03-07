import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


prostate_cancer = pd.read_csv("Prostate_Cancer.csv")
print(prostate_cancer.shape)


prostate_cancer = prostate_cancer[['radius', 'texture', 'perimeter', 'diagnosis_result']]


Y = prostate_cancer[['diagnosis_result']].values.ravel()
X = prostate_cancer.drop('diagnosis_result', axis=1)


modele = KNeighborsClassifier()
modele.fit(X, Y)

def Consultation_prostate_cancer(radius, texture, perimeter, modele):
    
    Xn = pd.DataFrame([[radius, texture, perimeter]], columns=['radius', 'texture', 'perimeter'])
   
    prediction = modele.predict(Xn)
    proba = modele.predict_proba(Xn)[0]

    print("Prédiction:", prediction)
    print("Probabilité:", proba)

    
    labels = ['Bénin (B)', 'Malin (M)']
    colors = ['green', 'red']

    
    plt.pie(proba, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title(f"Probabilité de diagnostic pour les features suivants : Radius={radius}, Texture={texture}, Perimeter={perimeter}")
    plt.show()


Consultation_prostate_cancer(8, 41, 67, modele)