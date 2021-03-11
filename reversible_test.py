#!/usr/bin/env python3
""" Tests for reversible.py """

import os
from subprocess import getstatusoutput, getoutput

prg = './reversible.py'


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_file():
    """ Works with input """

    file = './test.txt'
    assert os.path.isfile(file)
    rv, out = getstatusoutput(f'{prg} -f {file}')
    assert rv == 0
    lines = out.splitlines()
    assert len(lines) == 3
    assert lines == ['banana', 'dresser', 'grammar']
