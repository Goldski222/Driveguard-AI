from fastapi import APIRouter, Query
import numpy as np, pandas as pd, math

router = APIRouter()

DEFAULT_BASE = {"NH₃":20.0,"CO":12.0,"O₂":20.8,"H₂S":1.5,"Ethanol":260.0}

def build_series(days=60, step_minutes=15, spikes_per_week=1, label="CO"):
    now = pd.Timestamp.utcnow().floor("min")
    start = now - pd.Timedelta(days=days)
    idx = pd.date_range(start, now, freq=f"{step_minutes}min")
    n = len(idx)
    weeks = max(1, days//7)
    spike_count = max(1, weeks*spikes_per_week)
    base = DEFAULT_BASE.get(label, 10.0)
    wave = 0.5*np.sin(np.linspace(0,12*np.pi,n))
    noise = np.random.normal(0,0.2,n)
    s = base + wave + noise
    centers = np.random.choice(np.arange(48, n-48), size=spike_count, replace=False)
    for c in centers:
        width = int(60/step_minutes)
        height = {"NH₃":15,"CO":25,"O₂":-3,"H₂S":8,"Ethanol":180}.get(label, 10)
        for k in range(-width,width+1):
            idxk=c+k
            if 0<=idxk<n: s[idxk]+=height*math.exp(-(k*k)/(2*(width/2.2)**2))
    return pd.DataFrame({"t": idx, "value": s})

@router.get("")
def get_history(room:str, det:str, from_:int|None=Query(None,alias="from"), to:int|None=Query(None,alias="to")):
    df=build_series(label=det)
    if from_ and to:
        s=pd.to_datetime(from_,unit="ms",utc=True); e=pd.to_datetime(to,unit="ms",utc=True)
        df=df[(df["t"]>=s)&(df["t"]<=e)]
    return [{"t":str(t),"value":float(v)} for t,v in zip(df["t"],df["value"])]
