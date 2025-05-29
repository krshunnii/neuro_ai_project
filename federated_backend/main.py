from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import shutil
import os
from model_loader import predict_stroke

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        temp_file_path = f"temp_images/{file.filename}"
        os.makedirs("temp_images", exist_ok=True)
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Run prediction
        prediction = predict_stroke(temp_file_path)

        # Optionally delete the temp file
        os.remove(temp_file_path)

        return {"result": prediction}
    except Exception as e:
        return {"result": f"Prediction failed: {str(e)}"}

# ✅ Run
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
