from aiogram.fsm.state import State, StatesGroup

class QuizStates(StatesGroup):
    Question = State()  # вопрос пользователю
    Result = State()    # результат