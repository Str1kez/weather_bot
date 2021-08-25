from loader import dp
from .throttling import ThrottlingMiddleware


if __name__ == "middlewares":
    # установка миддлварей, которые импортируются в app.py -> инициализируют этот инит
    dp.middleware.setup(ThrottlingMiddleware())
