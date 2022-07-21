from telebot import TeleBot

from .start_state import StartState


STATES = {
    StartState.__name__: StartState,
}


def make_state(state, context, storage, user_tg_id, tb: TeleBot):
    state_class = STATES[state]
    state = state_class(user_tg_id, context, storage, tb)
    return state