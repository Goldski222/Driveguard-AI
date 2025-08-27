# OBW Modbus HMI (PyQt6 + pymodbus)

This starter runs a **desktop HMI** (no Streamlit) with a 2.5D floorplan and live Modbus polling.

## Features
- Async Modbus polling via `pymodbus` (TCP)
- PyQt6 desktop UI with floorplan image and **clickable room buttons**
- Detector dialog with **real-time chart** (pyqtgraph), live, z-score, slope
- Built-in **Modbus simulator** (run separately) on `127.0.0.1:5020`
- Historical CSV loader in `app/data_manager.py` (batch pre-fill buffers)

## Quickstart
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Terminal A — simulator (optional)
python -m app.simulator

# Terminal B — HMI
python -m app.main
```

## Map to your devices
Edit `app/settings.py` and set:
- `host`, `port` (usually 502), `unit_id`
- `points`: a dict of `"<Room>: <Gas>" -> holding_register_address`

## Load historical CSV
Write a small script (or a button in UI) that calls:
```python
from app.data_manager import load_history_csv
load_history_csv("your_history.csv", key_map={"your_key":"Room 12: CO"}, time_col="timestamp", value_col="ppm", key_col="key")
```
