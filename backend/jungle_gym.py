import numpy as np
from tokenizer import tokenize_f, tokenize_n

# format data 
def classify(norm_data, X, Y):
    odd=True
    i=0
    for line in norm_data:
        if(i<=19999):
            if odd:
                odd=False
                try:
                    token=tokenize_f(line)
                    for c,j in enumerate(token):
                        X[i, c]=j
                except(ValueError):
                    print(line)
                    import sys
                    sys.exit()
                if '(ping)' in line.split() or ('192.168.1.167' in line.split() and '192.168.1.176' in line.split()):
                    Y[i]=1
                i+=1
            else:
                odd=True
        else:
            try:
                token=tokenize_n(line)
                for c,j in enumerate(token):
                    X[i, c]=j
            except(ValueError):
                print(line)
                import sys
                sys.exit()
            if '(ping)' in line.split() or ('192.168.1.167' in line.split() and '192.168.1.176' in line.split()):
                Y[i]=1  
            i+=1         
    return X, Y

def normalize(norm_data, X):
    for line in norm_data:
        X=np.append(X,tokenize_f(line))

## load net and current settings
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

norm_data=open('backend/sample.txt', 'r')
X=np.zeros([220000, 6])
Y=np.zeros([220000, 1])
X, Y = classify(norm_data, X, Y)

# from pandas import value_counts
# print(value_counts(Y.flatten()))
# shuffle and format
shuffler=np.random.permutation(X.shape[0])
X=X[shuffler]
Y=Y[shuffler]
X_train, X_test, Y_train, Y_test = train_test_split(X,Y)

# # Model and test
desc_tree=IsolationForest(max_features=6, contamination=0.0288, n_estimators=108)
desc_tree.fit(X_train)
# from joblib import load
# desc_tree = load('backend/models/net_two.joblib')
Y_predict=desc_tree.predict(X_test)
Y_predict = np.where(Y_predict==1, 1, 0)

# Look at results 
from sklearn.metrics import accuracy_score
scores = desc_tree.decision_function(X_test)

for t in (-2, -.15, -.1, -.05, 0, .05):
    preds = np.where(scores < t, 0, 1)  # customize threshold
    print(t, accuracy_score(preds, Y_test))

# f=open('test.txt', 'w')
# for i in Y_predict:
#     f.write(str(i))
# f.close()

# save results 
from joblib import dump
dump(desc_tree, 'backend/models/net_three.joblib')
