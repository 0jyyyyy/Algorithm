klp_ls = ["k","l","p"]
for _ in range(3):
  s = input()
  if s[0] in klp_ls:
    klp_ls.remove(s[0])

if len(klp_ls) == 0:
  print("GLOBAL")
else:
  print("PONIX")