from typing import List, Dict
from pathlib import Path

def get_cats_info(path: str) -> List[Dict[str, str]]:
    """
    Read a text file with cat info and return a list of dicts:
    [{'id': str, 'name': str, 'age': str}, ...]

    Args:
        path (str): Path to the text file.

    Returns:
        List[Dict[str, str]]: List of cat information dictionaries.
                              Returns an empty list if file is missing or invalid.
    """
    cats = []

    file_path = Path(path)
    if not file_path.is_absolute():
        # шукаємо відносно поточного файлу (де task1.py)
        file_path = Path(__file__).parent / file_path
    try:
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) != 3:
                    # skip malformed line
                    continue

                cat_id, name, age = parts
                cats.append({
                    "id": cat_id.strip(),
                    "name": name.strip(),
                    "age": age.strip(),
                })

    except FileNotFoundError:
        return []

    return cats

if __name__ == "__main__":
    cats = get_cats_info("./kats_info_ID.txt")
    print(cats)
