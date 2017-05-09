from sand.stype import sandbit, stone, water
from sand.stype import fire, wood, null

GAMECONFIG = {
    'bounds': False,
    'initial_pen': 3,
    'starting_element': 'sand',
    'sources_enabled': True,
}

GAMECONFIG['elements'] = {
    'sand'  : sandbit.Sand(),
    'stone' : stone.Stone(),
    'water' : water.Water(),
    'fire'  : fire.Fire(),
    'wood'  : wood.Wood(),
    'null'  : null.Null(),
}

GAMECONFIG['element_sources'] = {
    (50, 0)  : "sand",
    (200, 0) : "water"
}
