from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# START KEYBOARD ReplyMarkup
buttons = [
    [KeyboardButton(text='START')],
    [KeyboardButton(text='HELP')],
    [KeyboardButton(text='SETTINGS')],
    [KeyboardButton(text='SETTINGS')],
    [KeyboardButton(text='SETTINGS')]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, is_persistent=True, one_time_keyboard=False, resize_keyboard=True, input_field_placeholder='Оберіть команду')


# START KEYBOARD Inline
buttons_inline = [
    [InlineKeyboardButton(text='Telegram', callback_data='Котик', url='https://core.telegram.org/bots/api#replykeyboardmarkup')],
    [InlineKeyboardButton(text='Собачка', callback_data='Собачка')],
    [InlineKeyboardButton(text='Єнот', callback_data='Єнот')]
]

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=buttons_inline)
