import states.statuses
class StateBase:
    STATUSES = states.statuses
    def __init__(self, session):
        self.session = session

    def handle_message(self, message):
        return None

    def change_state(self, to_state):
        print("change state to {0}".format(to_state))
        self.session.state = to_state

    def finish(self):
        print('{0}への旅行を{1}の期間で{2}人で予約しました！'.format(
            self.session.place, self.session.date, self.session.amount
        ))
