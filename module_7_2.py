def custom_write(file_name, strings: list):
  file = open(f'{file_name}', 'w')
  string = int()
  crs = int()
  keylist = []
  valuelist = []
  for i in strings:
    string = 1 + strings.index(i)
    crs = file.tell()
    file.write(f'{i} \n')
    file.close
    keylist.append((string, crs))
    valuelist.append(i)
  strings_positions = dict(zip(keylist, valuelist))
  return strings_positions


info = [
  'Text for tell.',
  'Используйте кодировку utf-8.',
  'Because there are 2 languages!',
  'Спасибо!'
  ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
  