from bot.models import BotState
from bot.states.start_state import StartState


class StateStorage:
    context_default = {}

    def __init__(self, user_tg_id):
        self.user_tg_id = user_tg_id

    def get_bot_state(self):
        state, _ = BotState.objects.get_or_create(
            user_tg_id=self.user_tg_id,
            defaults={'state_name': StartState.__name__}
        )

        print('state_name', state)

        return state.state_name, state.context

    def set_bot_state(self, state_name):
        BotState.objects.filter(user_tg_id=self.user_tg_id).update(state_name=state_name)

    def set_bot_context(self, context=None):
        if context is None:
            context = self.context_default

        BotState.objects.filter(user_tg_id=self.user_tg_id).update(context=context)