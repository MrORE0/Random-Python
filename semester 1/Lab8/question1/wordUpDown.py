def buildWordUpandDown (word):
      for char in range(len(word) + 1):
        print(word[:char])
      for char in range(len(word) -1, 0, -1):
        print(word[:char])

buildWordUpandDown('hello')