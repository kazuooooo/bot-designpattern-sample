#!/usr/bin/env python
# -*- coding: utf-8 -*-
from session import Session
from states.initial_state import InitialState
from states.select_place_state import SelectPlaceState
from states.select_date_state import SelectDateState
from states.select_amount_state import SelectAmountState
from messengers.plain_messenger import PlainMessenger
from messengers.line_messenger import LineMessenger

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--message')
parser.add_argument('--messenger')

def buildMessenger():
    if(parser.parse_args().messenger == 'line'):
        return LineMessenger()
    else:
        return PlainMessenger()

if __name__ == '__main__':
    # messengerを作成
    messenger = buildMessenger()
    # messengerをSessionにセット
    session = Session.read_session(messenger)
    message = parser.parse_args().message

    # stateを取得
    state_class = eval(session.state)
    state = state_class(session)

    state.handle_message(message)

    session.save_session()


