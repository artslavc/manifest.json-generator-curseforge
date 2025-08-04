import json

# Читаем ID модов из файла
with open("mods.txt", "r", encoding="utf-8") as f:
    mod_ids = [line.strip() for line in f if line.strip().isdigit()]

# Загружаем шаблон manifest.temple
with open("manifest-template.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

# Формируем список файлов для manifest.json
files = [{"projectID": int(mod_id), "fileID": 0} for mod_id in mod_ids]

# Вставляем в manifest
manifest["files"] = files

# Записываем итоговый manifest.json
with open("manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=4)

print("manifest.json успешно создан!")