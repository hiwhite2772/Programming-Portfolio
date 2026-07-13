from sklearn.naive_bayes import MultinomialNB
import numpy as np
e1 = [2,1,2,2,2,2]
e2 = [2,2,2,1,2,2]
e3 = [1,0,2,1,2,0]
e4 = [2,0,1,1,2,1]

train_data = np.array([e1,e2,e3,e4])
ket_qua = np.array(['yes','yes','no','no'])
e6 = np.array([[2,1,2,1,2,0]])
ml = MultinomialNB(alpha=1)
ml.fit(train_data, ket_qua)
print("Probability of e6:", ml.predict_proba(e6))
print(f"Predicting class of e6: {str(ml.predict(e6))}")