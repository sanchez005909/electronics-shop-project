import pathlib
from pathlib import Path

# Получаем строку, содержащую путь к рабочей директории:
dir_path = pathlib.Path.cwd()
# Объединяем полученную строку с недостающими частями пути
path = Path(dir_path, 'src', 'items.csv')
