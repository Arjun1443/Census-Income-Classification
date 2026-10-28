# Census Income Classification

## Interactive Streamlit app

A companion application is available in [streamlit_app/app.py](streamlit_app/app.py).

```bash
python -m pip install -r streamlit_app/requirements.txt
python -m streamlit run streamlit_app/app.py
```

This app fits a fresh random-forest baseline from the included dataset. Its evaluation is separate from prior notebook runs.

See [DEPLOYMENT.md](DEPLOYMENT.md) for Community Cloud setup, validation coverage, and runtime requirements. A live deployment is not yet confirmed.


A tabular machine-learning project exploring income-category classification from demographic and employment attributes.

## Why this project matters

The project provides a setting for practicing preprocessing, exploratory analysis, classifier comparison, and evaluation on structured data.

## Repository contents

- [Census income.ipynb](<Census income.ipynb>): analysis and modeling notebook
- [census-income_.csv](census-income_.csv): included dataset

## Technical focus

Python · pandas · NumPy · scikit-learn · Matplotlib · Seaborn

The existing project documentation describes logistic regression, decision tree, and random forest experiments. Inspect the notebook and rerun its cells before relying on model comparisons.

## Explore locally

```bash
git clone https://github.com/Arjun1443/Census-Income-Classification.git
cd Census-Income-Classification
python -m pip install numpy pandas scikit-learn matplotlib seaborn jupyter
python -m jupyter notebook
```

Open the notebook, point its data-loading cell to `census-income_.csv`, and review the split and preprocessing order before training.

## Evaluation considerations

Report precision, recall, F1, class balance, and the evaluation split alongside accuracy. Demographic data can encode historical disparities; this educational model should not be treated as a validated tool for decisions about individuals. No independently reproduced performance claim is made here.
