from .strings import to_upper

# Теперь можно делать: from utils import to_upper
# вместо: from utils.strings import to_upper
__all__ = ['to_upper'] # Явно указываем, что доступно при import *