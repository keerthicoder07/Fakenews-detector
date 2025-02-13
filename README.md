# Fake News Detection API

## Overview
This project is a Fake News Detection API built with **FastAPI** and a fine-tuned **DeBERTa model**. It predicts the truthfulness of a given statement using natural language processing techniques.

## Features
- Accepts text input for fake news classification
- Uses a **fine-tuned `sileod/deberta-v3-base-tasksource-nli` model**
- Returns predictions as one of six categories: `False`, `Barely True`, `Half True`, `True`, `Mostly True`, `Pants on Fire`

- React frontend for user interaction

---

## Tech Stack
- **Backend**: FastAPI, Transformers (Hugging Face), PyTorch, MongoDB
- **Frontend**: React.js, Axios
- **Database**: MongoDB

---

## Setup Instructions

### Backend Setup (FastAPI)

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/fake-news-detection.git
   cd fake-news-detection/backend
   ```

2. **Create a virtual environment & activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB (if required)**
   Ensure MongoDB is running locally or provide a connection string to **MongoDB Atlas** in `.env`.

5. **Run the FastAPI server**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Frontend Setup (React)

1. **Navigate to the frontend folder**
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```

---

## API Endpoints

### 1. Predict Fake News
- **URL:** `POST /predict`
- **Description:** Accepts a text statement and returns a classification result.
- **Request Body (Form-Data):**
  ```json
  {
    "statement": "NASA is planning to launch a space hotel by 2030."
  }
  ```
- **Response:**
  ```json
  {
    "statement": "NASA is planning to launch a space hotel by 2030.",
    "prediction": "False"
  }
  ```

---

## Required Dependencies

### Backend (Python)
Install these using:
```bash
pip install -r requirements.txt
```

```text
fastapi
pydantic
transformers
torch
uvicorn


### Frontend (React)
Install these using:
```bash
npm install
```

```text
react
axios
```

---

## Contribution
Feel free to contribute by submitting **pull requests** or reporting issues!

---

## License
This project is **MIT Licensed**. See `LICENSE` for details.

