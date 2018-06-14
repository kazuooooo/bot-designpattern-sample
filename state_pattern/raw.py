import pickle
import pdb
import os
import sys

STATUS_INITIAL       = 'INITIAL'
STATUS_SELECT_PLACE  = 'SELECT_PLACE'
STATUS_SELECT_DATE   = 'SELECT_DATE'
STATUS_SELECT_AMOUNT = 'SELECT_AMOUNT'

class Sesssion:
    PICKLE_FILE = 'session.pickle'
    def __init__(self):
        self.place  = None
        self.date   = None
        self.amount = None
        self.state  = STATUS_INITIAL

    @classmethod
    def read_session(cls):
        try:
            with open(cls.PICKLE_FILE, mode='rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return cls()

    def save_session(self):
        with open(self.PICKLE_FILE, mode='wb') as f:
            pickle.dump(self, f)

    def reset_session(self):
        os.remove(self.PICKLE_FILE)

if __name__ == '__main__':
    session = Sesssion.read_session()
    state = session.state
    if state == STATUS_INITIAL:
        session.state = STATUS_SELECT_PLACE
        session.save_session()
        print('旅行botです!どこに行きたいですか？:')
    elif state == STATUS_SELECT_PLACE:
        session.place = sys.argv[1]
        session.state = STATUS_SELECT_DATE
        session.save_session()
        print('日程はいつにしますか？')
    elif state == STATUS_SELECT_DATE:
        session.date  = sys.argv[1]
        session.state = STATUS_SELECT_AMOUNT
        session.save_session()
        print('何人でいきますか？')
    elif state == STATUS_SELECT_AMOUNT:
        session.amount = sys.argv[1]
        print('{0}への旅行を{1}の期間で{2}人で予約しました！'.format(session.place, session.date, session.amount))
        session.reset_session()