#Cette première partie j'ai utilisé une approche plus compliqué car je ne voyais pas d'autres options pour le faire,
# après quelques recherche et en m'inspirant des projets des autres j'ai trouvé une solution bien plus simple et efficace

# def my_long_word(chiffre, phrase):
#     length_phrase = get_length(phrase)
#     i=0
#     parsed_phrase = []
#     index_breakpoint = 0
#     while i < length_phrase:
#         if phrase[i] == ' ' or phrase[i] == ',':
            
#             # print(phrase[:i])
#             substring = phrase[index_breakpoint + 1:i]
#             if substring != '':
#                 parsed_phrase += [substring]
#                 index_breakpoint = i
#         i += 1
#     if index_breakpoint != length_phrase -1:
#         parsed_phrase += [phrase[index_breakpoint + 1:]]
#     length_parsed_phrase = get_length(parsed_phrase)
#     return_phrase = ''
#     i = 0
#     while i < length_parsed_phrase:
#         if get_length(parsed_phrase[i]) >= chiffre:
#             return_phrase += parsed_phrase[i]
#         i += 1
#     print(parsed_phrase)
    
# test = " a cest cool la vie, je suis la bete"
# my_long_word(3, test)

# Voici la méthode qui marche même si il y a des espaces en trop
def get_length(chaine):
    length = 0

    while True:
        try:
            element = chaine[length]
            length += 1
        except IndexError:
            break

    return length
def my_long_word(chiffre, phrase):
    length = get_length(phrase)
    word = ''
    word_list = []
    i=0
    while i < length:
        if phrase[i] != ' ' and phrase[i] != ',':
            word += phrase[i]
        else:
            if word != '':
                word_list += [word]
                word = ''
        i += 1
    if word != 0:
        word_list += [word]
        word = ''
    i = 0
    length = get_length(word_list)
    phrase_return = ""
    while i < length:
        if get_length(word_list[i]) >= chiffre:
            phrase_return += word_list[i] + ' '   
        i += 1
    return phrase_return
        
            
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

print(my_long_word(3, phrase))