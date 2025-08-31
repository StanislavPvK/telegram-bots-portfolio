from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from app.data.questions import QUESTIONS
from app.keyboards.inline import get_question_keyboard, repeat_inline_kb, ctg_inline_kb
from app.states.quiz_states import QuizStates


# Роутер для обработки логики викторины
quiz_router = Router()


# Обработка выбора категории
@quiz_router.callback_query(F.data.in_(["ctg_python", "ctg_history"]))
async def choose_category(callback: types.CallbackQuery, state: FSMContext):

    current_state = await state.get_state()

    # Проверяем, не находится ли пользователь уже в процессе викторины
    if current_state == QuizStates.Question:
        await callback.answer("Сначала завершите текущую викторину!", show_alert=True)
        return

    # Определяем категорию по callback_data
    if callback.data == "ctg_python":
        category = "Python"
    else:
        category = "History"

    # Сохраняем данные викторины в FSM
    await state.update_data(
        category=category,
        current_question=0,
        correct_answers=0
    )
    await state.set_state(QuizStates.Question)

    # Отправляем первый вопрос
    question_data = QUESTIONS[category][0]
    await callback.message.answer(
        text=question_data["question"],
        reply_markup=get_question_keyboard(question_data)
    )

    await callback.answer()


# Обработка ответа пользователя
@quiz_router.callback_query(F.data.in_(["0", "1", "2", "3"]))
async def process_answer(callback: types.CallbackQuery, state: FSMContext):

    data = await state.get_data()
    category = data["category"]
    current_question = data["current_question"]
    correct_answers = data["correct_answers"]

    questions = QUESTIONS[category]
    question_data = questions[current_question]

    selected_answer = int(callback.data)

    # Проверка правильности ответа
    if selected_answer == question_data["answer"]:
        correct_answers += 1

    current_question += 1

    # Убираем кнопки у предыдущего вопроса
    await callback.message.edit_reply_markup(reply_markup=None)

    if current_question < len(questions):

        # Переходим к следующему вопросу
        await state.update_data(current_question=current_question, correct_answers=correct_answers)
        next_question = questions[current_question]

        await callback.message.answer(
            text=next_question["question"],
            reply_markup=get_question_keyboard(next_question))
        
    else:

        # Если вопросов больше нет — показываем результат
        await state.update_data(correct_answers=correct_answers)

        await state.set_state(QuizStates.Result)

        await callback.message.answer(
            text=f"Викторина завершена!\nВы ответили правильно на {correct_answers} из {len(questions)} вопросов.",
            reply_markup=repeat_inline_kb
        )

    await callback.answer()


# Обработка повторного запуска викторины
@quiz_router.callback_query(F.data == "repeat_quiz")
async def repeat_quiz(callback: types.CallbackQuery, state: FSMContext):

    await state.clear()
    
    await callback.message.answer(
        text="Выберите категорию для новой викторины:",
        reply_markup=ctg_inline_kb
    )
    
    await callback.answer()