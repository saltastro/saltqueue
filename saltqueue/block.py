# Licensed under a 3-clause BSD style license - see LICENSE.rst
#This module implements the base NDData class.

__all__ = ['Block']

class Block(object):
   """Block describes an observing Block as defined for SALT.  
  
      Parameters
      -----------
      blockid: int
         Integer value for block ID in the database

      Raises
      ------
      TypeError
        If the blockid is not an integer
   """

   def __init__(self, blockid):
      self.blockid=blockid    
   
   @property
   def blockid(self):
       return self._blockid

   @blockid.setter
   def blockid(self, value):
      if isinstance(value, int):
           self._blockid = value
      else:
           raise TypeError('Blockid must be a integer')

