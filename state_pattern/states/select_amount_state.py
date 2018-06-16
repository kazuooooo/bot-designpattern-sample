from .state_base import StateBase
class SelectAmountState(StateBase):
    def handle_message(self, amount_message):
        self.session.amount = amount_message
        self.finish()
        self.session.reset_session()