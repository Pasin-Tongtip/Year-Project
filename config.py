class Config:
    __ALL_CONFIGS = {
        'WIDTH': 800,
        'HEIGHT': 600,
        'WHITE': (255, 255, 255),
        'BLACK': (0, 0, 0),
        'RED': (255, 0, 0),
        'GREEN': (0, 255, 0),
        'BLUE': (50, 153, 213),
        'BLOCK_SIZE': 20,
        'SPEED': 10,
        'NUM_FOOD': 5,
    }

    @classmethod
    def get(cls, key):
        return cls.__ALL_CONFIGS[key]
