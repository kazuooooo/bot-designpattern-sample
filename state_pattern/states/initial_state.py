from .state_base import StateBase
class InitialState(StateBase):
    def handle_message(self, message):
        self.change_state(self.STATUSES.STATUS_SELECT_PLACE)
        print('旅行botです!どこに行きたいですか？:')