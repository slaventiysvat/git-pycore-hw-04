from typing import Tuple
from pathlib import Path


def total_salary(path: str) -> tuple[int, float]:
    file_path = Path(path)
    if not file_path.is_absolute():
        # шукаємо відносно поточного файлу (де task1.py)
        file_path = Path(__file__).parent / file_path

    if not file_path.exists():
        return (0, 0.0)

    total = 0
    count = 0

    with file_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                _, salary_str = line.split(",", 1)
                total += float(salary_str)
                count += 1
            except ValueError:
                continue

    return (int(total), round(total / count, 2)) if count else (0, 0.0)

if __name__ == "__main__":
    print(total_salary("./salaries.txt"))
