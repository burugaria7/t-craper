import os

for i in range(1049):
    os.rename('img/deru1000/' + str(i) + '.png', 'img/deru1000/deru1000_' + str(i) + '.png')
