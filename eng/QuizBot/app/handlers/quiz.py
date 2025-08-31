from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from app.data.questions import QUESTIONS
from app.keyboards.inline import get_question_keyboard, repeat_inline_kb, ctg_inline_kb
from app.states.quiz_states import QuizStates


# Router for handling quiz logic
quiz_router = Router()


# Handle category selection
@quiz_router.callback_query(F.data.in_(["ctg_python", "ctg_history"]))
async def choose_category(callback: types.CallbackQuery, state: FSMContext):

    current_state = await state.get_state()

    # Check if the user is already in a quiz
    if current_state == QuizStates.Question:
        await callback.answer("Please finish the current quiz first!", show_alert=True)
        return

    # Determine category from callback_data
    if callback.data == "ctg_python":
        category = "Python"
    else:
        category = "History"

    # Save quiz data in FSM
    await state.update_data(
        category=category,
        current_question=0,
        correct_answers=0
    )
    await state.set_state(QuizStates.Question)

    # Send the first question
    question_data = QUESTIONS[category][0]
    await callback.message.answer(
        text=question_data["question"],
        reply_markup=get_question_keyboard(question_data)
    )

    await callback.answer()


# Handle user answer
@quiz_router.callback_query(F.data.in_(["0", "1", "2", "3"]))
async def process_answer(callback: types.CallbackQuery, state: FSMContext):

    data = await state.get_data()
    category = data["category"]
    current_question = data["current_question"]
    correct_answers = data["correct_answers"]

    questions = QUESTIONS[category]
    question_data = questions[current_question]

    selected_answer = int(callback.data)

    # Check if the answer is correct
    if selected_answer == question_data["answer"]:
        correct_answers += 1

    current_question += 1

    # Remove buttons from the previous question
    await callback.message.edit_reply_markup(reply_markup=None)

    if current_question < len(questions):

        # Move to the next question
        await state.update_data(current_question=current_question, correct_answers=correct_answers)
        next_question = questions[current_question]

        await callback.message.answer(
            text=next_question["question"],
            reply_markup=get_question_keyboard(next_question))
        
    else:

        # If no more questions — show the result
        await state.update_data(correct_answers=correct_answers)

        await state.set_state(QuizStates.Result)

        await callback.message.answer(
            text=f"Quiz completed!\nYou answered {correct_answers} out of {len(questions)} questions correctly.",
            reply_markup=repeat_inline_kb
        )

    await callback.answer()


# Handle quiz restart
@quiz_router.callback_query(F.data == "repeat_quiz")
async def repeat_quiz(callback: types.CallbackQuery, state: FSMContext):

    await state.clear()
    
    await callback.message.answer(
        text="Choose a category for the new quiz:",
        reply_markup=ctg_inline_kb
    )
    
    await callback.answer()
