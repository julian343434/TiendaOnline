import random
class BaseDatos:
    def __init__(self):
        self.data = {}
        self.json=None

    def genera_base_data(self) -> dict:
        for i in range(1, ):
            zapato = f'zapato{i}'
            enlaces = random.sample(range(1, 6), 3)  # Generar 3 enlaces aleatorios para cada artículo
            enlaces = [f'zapato{j}' for j in enlaces]
            self.data[zapato] = {'enlaces': enlaces}

    def __str__(self) -> str:
        for zapato, info in self.data.items():
            print(f'{zapato}: {info}')