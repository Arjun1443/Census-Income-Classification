from pathlib import Path
import pandas as pd
import streamlit as st
from ui import page, data_path
from engine import clean, fit

page('Income Pattern Explorer', 'Inspect census data and evaluate an income-classification baseline with a transparent held-out split.', "TABULAR ML")
TARGET='income'
TASK='classification'
@st.cache_data
def load():
    return clean(pd.read_csv(data_path('census-income_.csv')))
@st.cache_resource
def train():
    return fit(load(),TARGET,TASK)
df=load()
c1,c2,c3=st.columns(3)
c1.metric("Dataset rows",f"{len(df):,}")
c2.metric("Input features",len(df.drop(columns=[TARGET,'customerID'],errors='ignore').columns))
c3.metric("Evaluation split","80 / 20")
explore,predict,method=st.tabs(["Explore the data","Model studio","Methodology"])
with explore:
    st.subheader("Understand the dataset")
    numeric=list(df.select_dtypes(include='number').columns)
    col=st.selectbox("Inspect a numeric feature",numeric)
    st.bar_chart(pd.cut(df[col],bins=15).value_counts(sort=False).rename_axis(col).reset_index(name='Rows').assign(**{col:lambda d:d[col].astype(str)}).set_index(col))
    st.dataframe(df.head(100),use_container_width=True,hide_index=True)
with predict:
    st.subheader("Train once. Inspect every result.")
    st.caption("This app trains a fresh random-forest baseline from the repository dataset; it does not load a notebook checkpoint.")
    if st.button("Build the baseline",type="primary"):
        with st.spinner("Training on the training partition only…"):
            train()
        st.session_state.ready=True
    if st.session_state.get('ready'):
        model,metrics,result,X=train()
        cols=st.columns(2)
        for container,(key,value) in zip(cols,metrics.items()): container.metric(key,f"{value:.3f}")
        st.caption("Held-out test results · fixed seed 42 · preprocessing fitted on training rows only")
        if TASK=='regression': st.scatter_chart(result,x='Observed',y='Predicted')
        else:
            st.caption("Confusion matrix: actual classes are rows; predicted classes are columns.")
            st.dataframe(result,use_container_width=True)
        st.subheader("Try a scenario")
        values={}
        with st.form('scenario'):
            columns=st.columns(3)
            for i,col in enumerate(X.columns):
                with columns[i%3]:
                    if pd.api.types.is_numeric_dtype(X[col]):
                        values[col]=st.number_input(col,value=float(X[col].median()))
                    else:
                        choices=sorted(X[col].dropna().unique().tolist())
                        values[col]=st.selectbox(col,choices)
            submit=st.form_submit_button('Run prediction',type='primary')
        if submit:
            sample=pd.DataFrame([values],columns=X.columns)
            outcome=model.predict(sample)[0]
            st.success(f"Estimated charges: {outcome:,.2f} dataset currency units" if TASK=='regression' else f"Predicted class: {outcome}")
            if TASK=='classification':
                st.bar_chart(pd.DataFrame({'Class':model.classes_,'Model probability':model.predict_proba(sample)[0]}).set_index('Class'))
                st.caption("Model probabilities are not calibrated guarantees.")
        st.download_button('Download evaluation',result.to_csv(index=True),'evaluation.csv','text/csv')
with method:
    st.markdown("""### A reproducible baseline
1. Clean column names and missing-value markers.
2. Hold out 20% of rows before fitting preprocessing.
3. Impute missing values, encode categories, and fit a random forest.
4. Evaluate on the held-out partition.

The dataset is a historical learning dataset. Scores describe this split, not real-world performance. This demo is intended for model inspection, not consequential decisions about individuals. The original notebook remains available in the repository.
""")
