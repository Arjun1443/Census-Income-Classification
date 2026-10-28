# Run and deploy the Streamlit companion

## Entry point

Repository: `Arjun1443/Census-Income-Classification`  
Branch: `main`  
Main file: `streamlit_app/app.py`  
Python: **3.11**

## Local setup

```bash
git clone https://github.com/Arjun1443/Census-Income-Classification.git
cd Census-Income-Classification
python -m venv .venv
# Activate the virtual environment before continuing.
python -m pip install -r streamlit_app/requirements.txt
python -m streamlit run streamlit_app/app.py
```

Dependencies are scoped to the app directory. Existing notebooks and their dependencies are preserved.

## Community Cloud

1. Sign in to https://share.streamlit.io/ with an account authorized for this GitHub repository.
2. Select **Create app**, then deploy from the repository above.
3. Use branch `main` and main file `streamlit_app/app.py`.
4. In Advanced settings, select Python 3.11 and configure secrets only where needed.
5. Deploy and wait for a successful build. Test the main interaction on the live app before adding its URL as a portfolio demo.

No live deployment URL is claimed in this document. Official deployment guidance: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Runtime configuration

No secrets are required for this app.

## Implementation scope

This app fits a fresh random-forest baseline from the included dataset. Its evaluation is separate from prior notebook runs.

## Validation

The app was checked locally with Streamlit AppTest for initial rendering. The tabular apps were also exercised through training and scenario prediction. Digit predictions, catalog similarity, currency calculation, and GRPO reward edge cases were checked locally. Credential-dependent and heavyweight model flows are identified above and are not covered by a successful initial-render test.

Dependency ranges are not a complete lockfile. Validate the hosted environment and resource use after deployment. Do not put keys in repository files.
