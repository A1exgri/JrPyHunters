from aiogram.fsm.state import StatesGroup, State


class GPTRequest(StatesGroup):
    wait_for_request = State()
