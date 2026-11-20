"""
ЗОНА ОТВЕТСТВЕННОСТИ: Backend Lead.
Задача: создать приложение FastAPI, описать входную схему Pydantic, связать функции из
database.py и ml_service.py в API-эндпоинты и настроить раздачу папки frontend/.
"""

# TODO: Импортировать FastAPI, StaticFiles, FileResponse, BaseModel, Field
# TODO: Импортировать функции из backend.database и backend.ml_service
# TODO: Создать объект app = FastAPI(...)
# TODO: Настроить вызов init_db() при старте приложения (событие startup или lifespan)


class OilInput:
    """
    Pydantic-схема (наследовать от BaseModel) для валидации данных, приходящих с фронтенда.
    Поля:
    - density: float (ограничить разумными рамками, например от 700 до 1050)
    - viscosity: float (от 0.5 до 500)
    - sulfur: float (от 0.0 до 10.0)
    """
    pass


# Маршрут: POST /api/predict
def api_predict(data: OilInput) -> dict:
    """
    Главный эндпоинт расчета.
    Вход: JSON с полями density, viscosity, sulfur (валидируется через OilInput).

    Что нужно сделать внутри:
        1. Вызвать predict_fractions(...) из ml_service.py.
        2. Вызвать generate_plot_base64(...) для полученной кривой.
        3. Вызвать save_calculation(...) из database.py и получить id записи.
        4. Собрать и вернуть итоговый словарь.

    Выход (JSON):
        {
            "id": 1,
            "curve": {"100°C": ..., "180°C": ..., "240°C": ..., "350°C": ...},
            "fractions": {"Бензиновая...": ..., ...},
            "recommendation": "...",
            "plot_image": "<строка base64>"
        }
    """
    pass


# Маршрут: GET /api/history
def api_history() -> list[dict]:
    """
    Вход: ничего.
    Выход: результат работы функции get_history(limit=10) из database.py.
    """
    pass


# Маршрут: GET /api/references
def api_references() -> list[dict]:
    """
    Вход: ничего.
    Выход: результат работы функции get_reference_oils() из database.py.
    """
    pass


# TODO: Подключить раздачу статических файлов (CSS, JS, картинки) из папки "frontend" по пути "/static"
# TODO: Создать маршрут GET "/", который отдает файл "frontend/index.html" через FileResponse