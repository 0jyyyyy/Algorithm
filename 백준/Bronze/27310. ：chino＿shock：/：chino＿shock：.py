imo = input()
imo_len = len(imo)
col_count = imo.count(':')
under_count = imo.count('_')*5

result = imo_len + col_count + under_count
print(result)