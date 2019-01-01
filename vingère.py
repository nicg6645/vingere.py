def codeword(y,foo): #returns codeword y modulated to the length of the text
  z = len(y) 
  c = len(foo) 
  if c > len(y) * 2:
    return y + y[0:c-z] + y[0:(c-z)-len(y)]
  else:
    return y + y[0:c-z] #it cant print y longer than 5 characters
def numero(x): #0=a,1=b,etc.
  b = ord(x)
  return b - 97
def every_other(l): #returns a list with every odd value from the original list
    return l[::2] 
def tabula(): #returns properly indexed tabula recta
  lines = open('tabularecta.txt', 'r').readlines() #http://www.cppapers.com/tableau.pdf
  q = list(lines)
  emptylist = []
  i = 0
  shmeptylist = []
  for entry in q:
    emptylist.append(list(entry))
  for entry in emptylist:
    shmeptylist.append(every_other(entry))
  return shmeptylist
def encrypto(y,foo): #returns correct entry in tabula recta (l,f) for each char in string y is key and foo is plaintext
  k = tabula()
  a = codeword(y,foo)
  l = list(a)
  f = list(foo)
  emptylist = ''
  #print (list(zip(l,f))) (commented out - used to be for debugging)
  for entry in zip(l,f):
    #print (list(entry)) (commented out - used to be for debugging)
    a = k[numero(list(entry).pop(1))]
    emptylist = emptylist + a[numero(list(entry).pop(0))]
  return emptylist 
def decrypto(y,x): #y is key and x is ciphertext
  k = tabula() #opening tabula recta
  ylist = list(codeword(y,x)) #turning characters in key into list
  xlist = list(x) #turning characters in ciphertext int list
  emptystring = ''
  z = list(zip(ylist,xlist)) #zipping the two together
  i = -1
  for entry in z: #iterating thru the tuple (codeword,ciphertext) for each character of plaintext
    i = i + 1
    a = k[numero(list(entry).pop(0))] # assign a to the correct row in tabula recta 
    for entry in a: #iterate through this entry
      if numero(entry) == numero(list(z[i]).pop(1)): #if the letter is the same as for the entry...
        emptystring = emptystring + chr(a.index(entry)+97) #the correct character of plaintext is the chr of its place in tabula recta
  return emptystring

