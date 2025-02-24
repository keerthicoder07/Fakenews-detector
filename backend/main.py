import os
import requests
from fastapi import FastAPI, HTTPException, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
load_dotenv()
app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hugging Face API Setup
API_KEY = os.getenv("HF_API_KEY")
if not API_KEY:
    raise RuntimeError("Hugging Face API key is missing. Set HF_API_KEY as an environment variable.")

MODEL_ID = "Keerthi0207/Fakenewsdetector"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Label Mapping
LABELS = {
    0: "False",
    1: "Barely True",
    2: "Half True",
    3: "Mostly True",
    4: "True",
    5: "Pants on Fire",
}

@app.post("/api/predict")
async def predict_news(
    text: str = Form(None), 
    file: UploadFile = File(None)
):
    try:
        if not text and not file:
            raise HTTPException(status_code=400, detail="Provide either text or a file.")

        if file:
            contents = await file.read()
            text = contents.decode("utf-8").strip()

        if not text:
            raise HTTPException(status_code=400, detail="Text is empty after processing.")

        payload = {"inputs": text}
        response = requests.post(API_URL, json=payload, headers=HEADERS)

        if response.status_code == 503:
            raise HTTPException(status_code=503, detail="Model is loading, try again later.")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())

        result = response.json()

        # ✅ Extract first item if response is nested
        if isinstance(result, list) and isinstance(result[0], list):
            result = result[0]  # Unwrap the nested list

        if not isinstance(result, list) or len(result) == 0:
            raise HTTPException(status_code=500, detail=f"Unexpected model response format: {result}")

        if not isinstance(result[0], dict) or "label" not in result[0] or "score" not in result[0]:
            raise HTTPException(status_code=500, detail=f"Unexpected model response format: {result}")

        best_prediction = max(result, key=lambda x: x["score"])  # Take the highest score
        label_index = int(best_prediction["label"].split("_")[-1])
        label = LABELS.get(label_index, "Unknown")

        return {"label": label, "score": best_prediction["score"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
app.mount("/", StaticFiles(directory="build", html=True), name="static")