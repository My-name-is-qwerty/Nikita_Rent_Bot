from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_start_builder1: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
button1: KeyboardButton = KeyboardButton(text="Пост с 1 фото")
button2: KeyboardButton = KeyboardButton(text="Пост с большим количество фото")
kb_start_builder1.row(button1).row(button2)
kb_start: ReplyKeyboardMarkup = kb_start_builder1.as_markup(resize_keyboard=True, input_field_placeholder="Выберите кнопку")
