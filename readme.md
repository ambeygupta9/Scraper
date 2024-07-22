Run the following commands to set and start the server

1. Create venv for this python project

```python3 -m venv .venv```

```source .venv/bin/activate```

2. Install python packages

```pip install -r requirements.txt```

3. Start server

```uvicorn main:app --reload```

Navigate to

```http://127.0.0.1:8000/docs#```