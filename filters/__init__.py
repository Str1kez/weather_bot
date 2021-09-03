from loader import dp
from .is_group import IsGroup
from .is_admin import IsAdmin


if __name__ == "filters":
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsAdmin)
