from aiogram.fsm.state import State, StatesGroup

class QuizStates(StatesGroup):
    Question = State()  # question to the user
    Result = State()    # result
