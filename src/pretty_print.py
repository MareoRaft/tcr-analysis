import pprint

PP = pprint.PrettyPrinter(indent=4)

def print(*args):
  PP.pprint(*args)
