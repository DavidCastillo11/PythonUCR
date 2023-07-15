import time
from api import getOneUser
from ids import ids

start_time = int(time.time())

for id in ids:
    user = getOneUser(id)
    print(user['name'])

end_time = int(time.time())
duration = int(end_time - start_time)
print("Duración total:", duration, "segundos")