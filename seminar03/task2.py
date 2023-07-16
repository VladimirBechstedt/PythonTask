'''
    В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
    Не учитывать знаки препинания и регистр символов.
    За основу возьмите любую статью из википедии или из документации к языку.
'''

staty = {}
sign = ['.', ',', '(', ')']
text = 'In all cases, if the optional parts are omitted, ' \
       'the code is executed in the current scope. ' \
       'If only globals is provided, it must be a dictionary ' \
       '(and not a subclass of dictionary), which will be used for both ' \
       'the global and the local variables. If globals and locals are given, ' \
       'they are used for the global and local variables, respectively. ' \
       'If provided, locals can be any mapping object. ' \
       'Remember that at the module level, globals and locals are the same dictionary. ' \
       'If exec gets two separate objects as globals and locals, ' \
       'the code will be executed as if it were embedded in a class definition.'

for i in sign:
    text = text.replace(i, '')

text = text.lower()
text_arr = text.split(' ')

for i in text_arr:
    staty[i] = text_arr.count(i)

staty_dict_sort = dict(sorted(staty.items(), key=lambda item: item[1], reverse=True))

a = 0
for key, values in staty_dict_sort.items():
    print(f'Слово {key} встречается {values} раз')
    a += 1
    if a == 10:
        break