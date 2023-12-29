MODELPATH = 'data/model.txt'


def train(value):
    with open(MODELPATH, 'w') as file:
        file.write(value)

