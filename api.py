from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from data_manager import insert_ip_data, get_all_ip_data


app = FastAPI(title="possiveis iPs para API")

class IPInput(BaseModel):
    ambiguous_ip: str

@app.post("/ips/", response_model=dict)
async def calculate_ips(data: IPInput):
    try:
        resultado = insert_ip_data(data.ambiguous_ip)
        return {"resultado": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar: {str(e)}")

@app.get("/ips/", response_model=list[dict])
async def list_ips():
    return get_all_ip_data()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)