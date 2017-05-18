#!usr/bin/env python
# -*- coding: utf-8 -*-
import pickle

def save_dict(name, dict):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(dict, f, pickle.HIGHEST_PROTOCOL)

def load_dict(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)