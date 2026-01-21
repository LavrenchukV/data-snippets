# ML Project Template Notes

Contains:
- project folder structure (bash)
- requirements template
- venv setup commands

---

## 📁 Project structure (bash)

```bash
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
```
---

## 📦 Requirements (Linux)

```bash
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
```


## 🐍 Virtual environment setup (Linux / Ubuntu)

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
uv pip install -r requirements.txt
