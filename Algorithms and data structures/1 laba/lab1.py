import numpy as np
import pandas as pd
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
df_checks = pd.DataFrame({"Products":[],"Sum":[]})
types, products = pd.read_csv('1 laba\\types.txt'), pd.read_csv('1 laba\\products.txt')
with open("1 laba\\combinations.txt", 'r', encoding="utf-8") as fr:
    combs = [l.strip('\n\r') for l in fr]
    combs_formated = []
    for i in combs:
        combs_formated.append(i.split(','))

    for steps in range(0, 200):
        random_expert = np.random.choice(combs_formated) 
        check = pd.DataFrame({'Product_Name': [], 'Product_Value': []})
        for tovar_type in random_expert:
            if tovar_type == '~':
                tovar_type = np.random.choice(list(types.columns))
            tovars = []
            tovars_probabilities = []
            tovars = list(types[tovar_type].dropna())
            for i in tovars:
                tovars_probabilities.append(float(products.query('product == @i').probability))
            tovar = np.random.choice(tovars, p=tovars_probabilities)
            check.loc[len(check.index)] = [tovar, float(products.query('product == @tovar').value)]
        df_checks.loc[len(df_checks.index)] = set(check.Product_Name),check.Product_Value.sum()

    df_checks.to_csv("result.csv", index=False)