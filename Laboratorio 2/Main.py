import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from api import getOneUser
from ids import ids

starttime = int(time.time())

with ThreadPoolExecutor() as executors: 
    user_name = []
    for id in ids: 
        user_name.append(executors.submit(getOneUser, id))
    
    for resultados in as_completed(user_name):
        new_data = resultados.result()
        print(new_data['name'])

enttime = int(time.time())
finishtime = int(enttime - starttime)
print("Tiempo Final:",finishtime, "segundos.")
