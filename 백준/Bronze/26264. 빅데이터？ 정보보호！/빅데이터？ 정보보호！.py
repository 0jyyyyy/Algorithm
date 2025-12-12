import re
n = int(input())
a= input()

pattern_big = r'bigdata'
pattern_sec = r'security'   
result_big = re.findall(pattern_big,a)  
result_sec = re.findall(pattern_sec,a)

if len(result_big) > len(result_sec):
  print('bigdata?')
elif len(result_big) < len(result_sec):
  print('security!')
else:
  print('bigdata? security!')