import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv('blkjckhands.csv', header=[0])


new = df.filter(['card1','card2','card3', 'dealcard1', 'winloss'], axis=1)

new = new[new.winloss != "Loss"]
new = new[new.winloss != "Push"]
del new["winloss"]
print(len(new))

new_hit = new[new.card3 != 0]
new_stand = new[new.card3 == 0]
new_hit["hit_stand"] = "hit"
del new_hit["card3"]
new_stand["hit_stand"] = "stand"
del new_stand["card3"]

df = pd.concat([new_hit, new_stand], axis=0)
df = shuffle(df)
print(df)
features = df[['card1', 'card2', 'dealcard1']]
target = df['hit_stand']
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=1)
#model = LogisticRegressionCV(cv=10,random_state=0)
#model.fit(X_train,y_train)

filename = 'finalized_model.sav'
# load the model from disk
model = pickle.load(open(filename, 'rb'))

y_pred = model.predict(X_test)
print("#########################################################")
print("Training score: "+"{:.2f}".format(model.score(X_train, y_train)))
print("Testing score: "+"{:.2f}".format(model.score(X_test, y_test)))
print("Confusion Matrix: \n", confusion_matrix(y_pred, y_test))
print()
print("Classification Report:\n", classification_report(y_pred, y_test))
print()

# save the model to disk
#filename = 'finalized_model.sav'
#pickle.dump(model, open(filename, 'wb'))
