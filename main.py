import pandas as pd

familyTree = {
    'Kids': ["Dad","Mom","Chisom","Amarachi","Ebuka","Tochukwu","Ikechukwu"],
    'Position': [1,2,3,4,5,6,7],
    'Gender': ["Male","Female","Female","Female","Male","Male","Male"],
    'Age': [42,37,17,9,7,6,1]
}
family = pd.DataFrame(familyTree)
print(family)
