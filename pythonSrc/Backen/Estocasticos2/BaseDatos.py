import random
class BaseDatos:
    def __init__(self):
        self.data = {}
        self.json=None


    def genera_base_data(self) -> dict:
        for i in range(1, 6):
            zapato = f'zapato{i}'
            enlaces = random.sample(range(1, 6), 5)  # Generar 3 enlaces aleatorios para cada artículo
            enlaces = [f'zapato{j}' for j in enlaces]
            metadata = {
                'id': i,
                'imagen': f'zapato{i}.jpeg',
                'nombre': f'zapato{i}',
                'rankin': None
            }
            self.data[zapato] = {'enlaces': enlaces, 'metadata': metadata}


    def __str__(self) -> str:
        for zapato, info in self.data.items():
            print(f'{zapato}: {info}')

            

if __name__ == '__main__':
    data1=BaseDatos()
    data1.genera_base_data()
    print(data1.data)