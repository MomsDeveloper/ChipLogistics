"""Articles menu texts."""

TITLE = 'Управление позициями'

OPEN_LIST_BTN = 'Список позиций'

CREATE_BTN = 'Добавить позицию'

LIST_TITLE = 'Созданные позиции'

ARTICLE_DESCRIPTION = """<b>{name}</b>

Таможенная пошлина: {duty_fee_ratio}
"""

DELETE_BTN = 'Удалить'

DELETED_MESSAGE = 'Позиция удалена'


BACK_TO_MENU = '🔙 Вернуться в меню'

BACK_TO_ARTICLES_MENU = '🔙 Вернуться в управление'

BACK_TO_LIST = '🔙 Вернуться к списку'


ASK_NAME = 'Укажите наименование позиции:'

ASK_DUTY_FEE_RATIO = 'Укажите пошлину на позицию (например, "9.5" для наценки в 9.5%):'  # noqa: E501

BAD_DUTY_FEE_RATIO = 'Неверный формат. Пошлина должна быть числом, например, например, "9.5" для наценки в 9.5%. Попробуйте снова'   # noqa: E501

CONFIRM_ARTICLE_CREATION = """Будет создана позиция:
<b>Наименование:</b> {name}
<b>Пошлина:</b> {duty_fee_ratio}
"""

CONFIRM_CREATION_BTN = 'Подтвердить'

DISMISS_CREATION_BTN = 'Отмена'

CREATED_ARTICLE = """Позиция успешно создана:
<b>Наименование:</b> {name}
<b>Пошлина:</b> {duty_fee_ratio}
"""
