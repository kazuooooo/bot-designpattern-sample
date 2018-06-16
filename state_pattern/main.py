#!/usr/bin/env python
# -*- coding: utf-8 -*-
from session import Session
from states.initial_state import InitialState
from states.select_place_state import SelectPlaceState
from states.select_date_state import SelectDateState
from states.select_amount_state import SelectAmountState
import sys

if __name__ == '__main__':
    # sessionを読み込み
    session = Session.read_session()
    message = sys.argv[1]
    # stateを取得
    state_class = eval(session.state)
    state = state_class(session)
    state.handle_message(message)

    session.save_session()