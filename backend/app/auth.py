from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from config import API_KEY

# Define the API key header
api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=True)

# Function to check API key validity
def validate_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key
