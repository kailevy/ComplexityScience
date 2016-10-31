import random

class WeightedFlip():
  """This will do a flip with probability of the opponent's previous moves"""
  def step(self, history, round):
      if round == 0:
          action = 1
      else:
          action = int(flip(sum(history[self.order^1])/len(history[self.order^1])))
      return action

def flip(p):
   return random.random() < p
