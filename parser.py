import os
import time
spisok = []
for adress, dirs, files in os.walk('E:\\!SOFT\Plug-ins'):
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 888886400:
            spisok.append(full)
file = open('parser.txt', 'w')
file.write(str(spisok))
file.close()