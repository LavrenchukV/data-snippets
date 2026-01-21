"""
ML project template notes.

Contains:
- project folder structure (bash)
- requirements template
- venv setup commands

"""

# === Project structure (bash command)===
"""
mkdir -p \
  data/raw data/processed data/external \
  notebooks \
  src/{data,features,models,utils} \
  app \
  configs \
  scripts \
  tests \
  .github/workflows \
  docker \
  great_expectations \
  mlruns \
  artifacts
"""

# === requirements (libraries in Linux command)

"""
cat > requirements.txt << 'EOF'
pandas
numpy
scikit-learn
mlflow
fastapi
uvicorn
pydantic
python-dotenv
joblib
great-expectations
pytest
EOF
"""

# === venv + install requirements (Linux command)

"""
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
uv pip install -r requirements.txt
"""