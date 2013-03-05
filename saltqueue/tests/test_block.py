# Licensed under a 3-clause BSD style license - see LICENSE.rst

from ..block import Block

__all__=['test_block']

def test_block():
    testblock=Block(5)
    assert testblock.blockid==5
    try:
        testblock=Block(5.5)
    except TypeError, e:
        pass

if __name__=='__main__':
   test_block()

