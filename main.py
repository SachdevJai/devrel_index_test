from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os
app = FastAPI
        
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
