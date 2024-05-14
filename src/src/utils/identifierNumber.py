def identifier_number(value):

    number_before_point = ''
    index_point = None
    point = False

    for i, caracter in enumerate(value):

        if caracter == '.':
            index_point = i
            point = True

            break

        number_before_point = '{}{}'.format(number_before_point, caracter)

    if index_point > 3:

        for i, caracter in enumerate(number_before_point): 

            print(i, caracter)

    if not point:

        value_formated = 'R${},00'.format(value)

        return value_formated




teste = identifier_number('1045.2')

print(teste)
# verification_point = 0
#     index = -1
#     value_formated = value

#     for i, caracter in enumerate(value):

#         if caracter == '.':

#             verification_point = 1
#             index = i       
        
#     if verification_point != 0:

#         number_after_point = index + 3

#         if number_after_point != len(value):

#             value_formated = '{}{}'.format(value, '0')
        
#         return 'R${}'.format(value_formated)

#     else:

#         return 'R${},00'.format(value)   

