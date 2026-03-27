from world_gen import generate_world
from systems.life_system import process_life
from systems.quest_system import process_quests
from systems.faction_system import process_factions

# Generazione mondo
world = generate_world()

# Ciclo simulazione semplice
for year in range(1,6):
    print(f"\n--- ANNO {year} ---")
    process_life(world)
    process_factions(world)   # Nuovo: gestione adesioni fazioni
    process_quests(world)