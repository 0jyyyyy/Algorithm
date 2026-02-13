while True:
  try:
    n = input()
    m = str.maketrans({'i':'e','e':'i','I':'E','E':'I'})

    result = n.translate(m)
    print(result)
  except EOFError:
    break