# Абсолютный импорт (рекомендуется)
#from utils.strings import to_upper
from utils import to_upper
from utils.strings import to_lower
from db.connector import connect

# Относительный импорт (используется внутри пакетов)
# from .strings import to_upper (работает только внутри пакета)

print(to_upper("aaa"))
print(to_lower("AAA"))
connect()

print(dir())