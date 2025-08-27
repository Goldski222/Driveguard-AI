from fastapi import APIRouter

router = APIRouter()

DETECTORS = {
    "Room 1": [{"label":"NH₃","x":35,"y":35,"units":"ppm"}],
    "Room 2": [{"label":"CO","x":85,"y":62,"units":"ppm"}],
    "Room 3": [{"label":"O₂","x":5,"y":44,"units":"%"}],
    "Room 12 17": [{"label":"Ethanol","x":63,"y":15,"units":"ppm"}],
    "Room Production": [
        {"label":"NH₃","x":20,"y":28,"units":"ppm"},
        {"label":"O₂","x":88,"y":40,"units":"%"}
    ],
    "Room Production 2": [
        {"label":"O₂","x":83,"y":45,"units":"%"},
        {"label":"H₂S","x":15,"y":29,"units":"ppm"}
    ]
}

THRESHOLDS = {
    "O₂": {"mode":"low","warn":19.5,"alarm":18.0,"units":"%"},
    "CO": {"mode":"high","warn":35.0,"alarm":50.0,"units":"ppm"},
    "H₂S":{"mode":"high","warn":10.0,"alarm":15.0,"units":"ppm"},
    "NH₃":{"mode":"high","warn":25.0,"alarm":35.0,"units":"ppm"},
    "Ethanol":{"mode":"high","warn":300.0,"alarm":500.0,"units":"ppm"},
}

HOTSPOTS = {
    "Room 1": {"left":63,"top":2,"width":14,"height":16},
    "Room 2": {"left":67,"top":43,"width":14,"height":16},
    "Room 3": {"left":60,"top":19,"width":14,"height":16},
    "Room 12 17": {"left":38,"top":-13,"width":13,"height":15},
    "Room Production": {"left":24,"top":28,"width":23,"height":21},
    "Room Production 2":{"left":23,"top":3,"width":23,"height":21}
}

@router.get("")
def get_config():
    return {"detectors": DETECTORS, "thresholds": THRESHOLDS, "hotspots": HOTSPOTS}
