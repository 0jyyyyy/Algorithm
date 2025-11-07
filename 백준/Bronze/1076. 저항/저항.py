color = {
    "black" : ['0',''],
    "brown" : ['1', '0'],
    "red" : ['2', '00'],
    "orange" : ['3', '000'],
    "yellow" : ['4', '0000'],
    "green" : ['5', '00000'],
    "blue" : ['6', '000000'],
    "violet" : ['7', '0000000'],
    "grey" : ['8', '00000000'],
    "white" : ['9', '000000000'],
}



first = input()
second = input()
third = input()
result = ""

result = color[f"{first}"][0]
result += color[f"{second}"][0]
result += color[f"{third}"][1]

print(int(result))
