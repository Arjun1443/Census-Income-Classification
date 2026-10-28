import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score, f1_score, confusion_matrix

def clean(frame):
    df = frame.copy()
    df.columns = df.columns.str.strip()
    for col in df.select_dtypes(include=['object', 'string']):
        df[col] = df[col].str.strip().replace({'?':np.nan, '':np.nan})
    if 'TotalCharges' in df:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    return df

def fit(frame, target, task):
    df = clean(frame).dropna(subset=[target])
    X = df.drop(columns=[target, 'customerID'], errors='ignore')
    y = df[target]
    numeric = list(X.select_dtypes(include='number').columns)
    categorical = [c for c in X if c not in numeric]
    prep = ColumnTransformer([
        ('numeric', Pipeline([('impute',SimpleImputer(strategy='median')),('scale',StandardScaler())]), numeric),
        ('category', Pipeline([('impute',SimpleImputer(strategy='most_frequent')),('encode',OneHotEncoder(handle_unknown='ignore'))]), categorical)
    ])
    estimator = (RandomForestRegressor(n_estimators=80,max_depth=12,random_state=42,n_jobs=1)
                 if task == 'regression' else RandomForestClassifier(n_estimators=80,max_depth=12,random_state=42,n_jobs=1,class_weight='balanced'))
    Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=.2,random_state=42,stratify=y if task=='classification' else None)
    model = Pipeline([('preprocess',prep),('model',estimator)]).fit(Xtr,ytr)
    pred = model.predict(Xte)
    if task == 'regression':
        metrics = {'MAE':float(mean_absolute_error(yte,pred)), 'R²':float(r2_score(yte,pred))}
        result = pd.DataFrame({'Observed':np.asarray(yte),'Predicted':pred})
    else:
        metrics = {'Accuracy':float(accuracy_score(yte,pred)), 'Macro F1':float(f1_score(yte,pred,average='macro'))}
        result = pd.DataFrame(confusion_matrix(yte,pred,labels=model.classes_),index=model.classes_,columns=model.classes_)
    return model,metrics,result,X
