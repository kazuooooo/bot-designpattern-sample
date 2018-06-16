from .state_base import StateBase
class SelectPlaceState(StateBase):
    def handle_message(self, message):
        self.session.place = message
        self.change_state(self.STATUSES.STATUS_SELECT_DATE)
        self.session.messenger.say('日程はいつにしますか？')