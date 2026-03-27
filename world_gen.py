import random

def generate_factions(world):
    factions = []
    minor_faction_templates = [
        {"name": "Bloody Fingers", "composition": ["Angel","MerFolk"], "territory": {"pois":[{"name":"Campo Bloody","coordinates":(-20,-20)}]}, "legendary_objects":[], "culture_bonus":{"Quality":5,"Entertainment":3}},
        {"name": "Crimson Talons", "composition": ["Dryad","Imp"], "territory": {"pois":[{"name":"Foresta Oscura","coordinates":(15,10)}]}, "legendary_objects":[], "culture_bonus":{"Quality":0,"Entertainment":2}}
    ]
    for temp in minor_faction_templates:
        temp["internal_behavior"] = "peaceful"  # verrà aggiornato in process
        temp["members"] = []
        factions.append(temp)
    return factions

def generate_world():
    world = {
        "wgs": [],
        "objects": [],
        "factions": generate_factions(None)
    }
    return world