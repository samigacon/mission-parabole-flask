# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

import partie1 

def main():
    partie1.init_simulation()
    partie1.run_simulation()

if __name__ == "__main__":
    main()
