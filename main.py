from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os
app = FastAPI()
STORAGE_DIR = "string_operations"
os.makedirs(STORAGE_DIR, exist_ok=True)
class StringRequest(BaseModel):
    text: str
    filename: str | None = None
class StringResponse(BaseModel):
    result: str
@app.post("/reverse-string/")
async def reverse_string(request: StringRequest):
    try:
        reversed_text = request.text[::-1]
        
        if not request.filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"reversed_string_{timestamp}.txt"
        else:
            filename = request.filename
            
        if not filename.endswith('.txt'):
            filename += '.txt'
            
        file_path = os.path.join(STORAGE_DIR, filename)
        
        with open(file_path, 'w') as f:
            f.write(reversed_text)
            
        return {
            "original_text": request.text,
            "reversed_text": reversed_text,
            "filename": filename,
            "file_path": file_path
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
@app.get("/concatenate/{text}")
async def concatenate_string(text: str):
    try:
        result = text + text
        
        return StringResponse(result=result)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
