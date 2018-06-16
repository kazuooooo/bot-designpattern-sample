from .state_base import StateBase
class InitialState(StateBase):
    def handle_message(self, message):
        self.change_state(self.STATUSES.STATUS_SELECT_PLACE)
        self.session.messenger.say('旅行botです!どこに行きたいですか？:')