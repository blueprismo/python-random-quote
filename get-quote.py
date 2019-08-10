import random
def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) -1
  rnd = random.randint(0,last)
  rnd1 = random.randint(0,last)
  print (quotes[rnd],quotes[rnd1])

if __name__== "__main__":
  primary()
