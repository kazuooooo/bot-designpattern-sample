#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pickle
import states.statuses
class Session:
    PICKLE_FILE = 'session.pickle'
    def __init__(self):
        self.place  = None
        self.date   = None
        self.amount = None
        self.state  = states.statuses.STATUS_INITIAL

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