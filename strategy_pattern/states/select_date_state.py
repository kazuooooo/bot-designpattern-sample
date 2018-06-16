from .state_base import StateBase
class SelectDateState(StateBase):
    def handle_message(self, date_message):
        self.session.date = date_message
        self.change_state(self.STATUSES.STATUS_SELECT_AMOUNT)
        self.session.messenger.say('人数は何人ですか？')