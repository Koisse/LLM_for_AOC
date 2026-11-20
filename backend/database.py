"""
ЗОНА ОТВЕТСТВЕННОСТИ: Backend DB.
Задача: подключиться к PostgreSQL через SQLAlchemy, описать 2 таблицы и написать 4 функции.
"""

# TODO: Импортировать os, datetime и нужные модули из sqlalchemy (create_engine, Column, Integer, Float, String, DateTime, JSON, declarative_base, sessionmaker)

# TODO: Прочитать строку подключения из переменной окружения DATABASE_URL
# Создать engine, SessionLocal и базовый класс Base


class ReferenceOil:
    """
    Таблица в БД: reference_oils (Эталонные марки нефти: Urals, Brent и др.)
    Нужно унаследовать от Base и описать колонки:
    - id: Integer, primary_key
    - name: String, уникальное, не пустое (название марки)
    - density: Float (плотность, кг/м3)
    - viscosity: Float (вязкость, сСт)
    - sulfur: Float (содержание серы, %)
    """
    pass


class CalculationHistory:
    """
    Таблица в БД: calculation_history (История расчетов пользователей)
    Нужно унаследовать от Base и описать колонки:
    - id: Integer, primary_key
    - created_at: DateTime (дата создания, по умолчанию текущее время)
    - density: Float
    - viscosity: Float
    - sulfur: Float
    - result_curve: JSON (словарь с результатами прогноза кривой разгонки)
    """
    pass


def init_db() -> None:
    """
    Создает все описанные таблицы в БД (если их еще нет) и заполняет таблицу ReferenceOil
    3-5 базовыми марками нефти, если таблица пустая.

    Вход: ничего.
    Выход: None.
    """
    pass


def save_calculation(density: float, viscosity: float, sulfur: float, result_curve: dict) -> int:
    """
    Сохраняет один выполненный расчет в таблицу calculation_history.

    Вход:
        density (float): Плотность нефти, например 870.0
        viscosity (float): Вязкость, например 15.2
        sulfur (float): Содержание серы в %, например 1.35
        result_curve (dict): Словарь с кривой, например {"100°C": 12.5, "180°C": 28.0, "240°C": 42.0, "350°C": 65.0}

    Выход:
        int: ID (число) только что созданной записи в базе данных.
    """
    pass


def get_history(limit: int = 10) -> list[dict]:
    """
    Достает из БД последние N расчетов (отсортированных от новых к старым).

    Вход:
        limit (int): Сколько последних записей вернуть (по умолчанию 10).

    Выход:
        list[dict]: Список словарей строго в таком формате:
        [
            {
                "id": 1,
                "created_at": "2026-11-20 14:30",  # строка с датой
                "density": 870.0,
                "viscosity": 15.2,
                "sulfur": 1.35,
                "result_curve": {"100°C": 12.5, "180°C": 28.0, "240°C": 42.0, "350°C": 65.0}
            },
            ...
        ]
    """
    pass


def get_reference_oils() -> list[dict]:
    """
    Возвращает список всех эталонных нефтей из таблицы reference_oils.

    Вход: ничего.

    Выход:
        list[dict]: Список словарей строго в таком формате:
        [
            {"id": 1, "name": "Urals", "density": 870.0, "viscosity": 15.2, "sulfur": 1.35},
            ...
        ]
    """
    pass