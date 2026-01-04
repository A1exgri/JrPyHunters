from aiogram.fsm.state import StatesGroup, State


class GPTRequest(StatesGroup):
    wait_for_request = State()


class CelebrityTalk(StatesGroup):
    dialog = State()


class Quiz(StatesGroup):
    game = State()


class Translater(StatesGroup):
    language = State()


class Recommendations(StatesGroup):
    recommendation = State()
