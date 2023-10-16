class HashMap:
  def __init__(self, pow=8, loadfactor=.5):
    
    self.len = 0
    self.maxSize = 2**pow - 1
    self.loadfactor = loadfactor
    self.pow = 8
    
    self.keys = self.maxSize * [None]
    self.vals = self.maxSize * [None]

  def put(self, key, value):
    """ Determine the position of the key and value by hashing the key. """
    i = hash(key) % self.maxSize

    """ Attempt to place the element in the hash map. Apply Linear Probing if the initial location is full. """
    probing = True
    while probing:
      if self.keys[i] == None:
        self.keys[i] = key
        self.vals[i] = value
        probing = False
        """ Increase the current size of the hash map. """
        self.len += 1
      elif self.keys[i] == key:
        self.keys[i] = key
        self.vals[i] = value
        probing = False
      else:
        i += 1
        i %= self.maxSize


    """ Check that we haven't exceeded the max loadfactor. """
    """ If we have, rehash into larger arrays. """
    if self.len / self.maxSize >= self.loadfactor:
      self.rehash()

  def get(self, key):
    """ Determine the position of the key and value by hashing the key. """
    i = hash(key) % self.maxSize
    
    """ Attempt to locate the element in the hashmap. Apply Linear Probing if collision detected. """
    probing = True
    while probing:
      """ Found element. """
      if self.keys[i] == key:
        return self.vals[i]
      #""" Collision. """
      elif not self.keys[i] == None:
        i += 1
        i %= self.maxSize
      #""" Element is not in array. """
      else:
        return None


  def contains(self, key):
    """ Determine the position of the key and value by hashing the key. """
    i = hash(key) % self.maxSize
    
    """ Attempt to locate the element in the hashmap. Apply Linear Probing if collision detected. """
    probing = True
    while probing:
      """ Found element. """
      if self.keys[i] == key:
        return True
      #""" Collision. """
      elif not self.keys[i] == None:
        i += 1
        i %= self.maxSize
      #""" Element is not in array. """
      else:
        return False

  def rehash(self):
    
    """ The new array size is the next power of two - 1. """
    self.pow += 1
    newSize = 2 ** self.pow - 1

    """ Create the new arrays. """
    newKeys = newSize * [None]
    newVals = newSize * [None]

    """ For every element in the current hash table, hash it into the new table. """
    for i in range(self.maxSize):
      key = self.keys[i]
      val = self.vals[i]

      """ Only attempt to place the element if it is not None"""
      if not key == None:
        i = hash(key) % newSize
  
        """ Apply Linear Probing as before. """
        probing = True
        while probing:
          if newKeys[i] == None:
            newKeys[i] = key
            newVals[i] = val
            probing = False
          else:
            i += 1
            i %= newSize

    self.keys = newKeys
    self.vals = newVals
    self.maxSize = newSize

  def __len__(self):
    return self.len

def main():
  map = HashMap()
  
  """ Basic tests. """
  assert(len(map) == 0)
  map.put("Matt", 4000)
  assert(len(map) == 1)
  map.put("Gabe", 4250)
  assert(len(map) == 2)
  map.put("Ben", 4500)
  assert(len(map) == 3)
  map.put("Bobby", 4750)
  assert(len(map) == 4)

  assert(map.contains("Matt") == True)
  assert(map.contains("Gabe") == True)
  assert(map.contains("Ben") == True)
  assert(map.contains("Bobby") == True)

  assert(map.get("Matt") == 4000)
  assert(map.get("Gabe") == 4250)
  assert(map.get("Ben") == 4500)
  assert(map.get("Bobby") == 4750)
  
  map.put("Matt", 3750)
  assert(map.contains("Matt") == True)
  assert(len(map) == 4)
  assert(map.get("Matt") == 3750)
  
  """ Rehash tests. """
  map2 = HashMap()
  
  for i in range(200):
    map2.put(i, True)
  
  assert(len(map2) == 200)
  assert(map2.maxSize == 511)

  for i in range(200):
    assert(map2.contains(i) == True)
    assert(map2.get(i) == True)

  print(map2.keys[195:205])
  
  print("All tests passed.")

if __name__ == "__main__":
  main()