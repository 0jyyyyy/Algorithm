result = 0
while True:
  try:
    n = input()
    if n == "gum gum for jay jay":
      result +=1
  except EOFError:
    print(result)
    break