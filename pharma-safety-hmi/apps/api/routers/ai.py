from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
import os

router = APIRouter()

class SummRequest(BaseModel):
    room: str; gas: str; latest: float|None; units: str; recent: list[tuple[str,float]]

@router.post("/summarize")
def summarize(body: SummRequest):
    key=os.getenv("OPENAI_API_KEY")
    if not key:
        return {"text":f"{body.room} {body.gas}: {body.latest}{body.units} (no API key)."} 
    client=OpenAI(api_key=key)
    user=f"Room:{body.room}\nGas:{body.gas}\nLatest:{body.latest}{body.units}"
    resp=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":"Industrial gas safety assistant."},
                  {"role":"user","content":user}],
        max_tokens=100
    )
    return {"text":resp.choices[0].message.content.strip()}
