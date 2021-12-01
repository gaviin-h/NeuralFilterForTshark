## load data set
def load_set():
    from Tshark import Tshark
    p=Tshark()
    f=open('sample.txt', 'a')
    proc=p.start('en0')
    for line in proc.stdout:
        f.write(str(line)+'\n')
    f.close()

# format data 
import numpy as np
from tokenizer import tokenize
norm_data=open('../sample.txt', 'r')
X=np.array
Y=np.array

for line in norm_data:
    X.append(tokenize(line))
    Y.append(0)

## load net and current settings
from sklearn import tree
desc_tree=tree.DecisionTreeClassifier()
desc_tree.fit(X,Y)

# run model

# save results 