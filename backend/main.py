from fastapi import FastAPI, File, UploadFile, Form
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from fastapi.middleware.cors import CORSMiddleware

# Load Model & Tokenizer
MODEL_PATH = "./fine_tune_liar_model"

try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

LABELS = {
    0: "False",
    1: "Barely True",
    2: "Half True",
    3: "True",
    4: "True",
    5: "Pants on Fire",
}

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust if needed
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

async def get_text_from_file(file: UploadFile) -> str:
    """ Reads the content of a .txt file and extracts text. """
    if file.filename.endswith(".txt"):
        return (await file.read()).decode("utf-8").strip()
    return None  # Unsupported format

@app.post("/predict")
async def predict_news(
    statement: str = Form(None), 
    file: UploadFile = File(None)
):
    # Check if statement or file is provided
    if not statement and not file:
        return {"error": "Either text input or a .txt file must be provided"}

    # If file is provided, extract text
    if file:
        statement = await get_text_from_file(file)
        if not statement:
            return {"error": "Unsupported file format. Only .txt files are allowed."}

    # Tokenize and predict
    inputs = tokenizer(statement, return_tensors="pt", truncation=True, padding=True)
    
    with torch.no_grad():
        outputs = model(**inputs)

    predicted_label = torch.argmax(outputs.logits, dim=1).item()
    
    return {
        "statement": statement,
        "prediction": LABELS.get(predicted_label, "Unknown")
    }
