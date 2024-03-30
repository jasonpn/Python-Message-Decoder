message_file = 'coding_qual_input.txt'

def decode(message_file):
    words_dict = dict()

    with open(message_file, 'r') as f:
        for line in f.readlines():
            number,word = line.split()
            words_dict[int(number)] = word

        sorted_words_dict = dict(sorted(words_dict.items()))

        pyramid = []
        
        for i in range(1, len(sorted_words_dict)):
            if sorted_words_dict.get(i*(i+1)/2) == None:
                break
            pyramid.append(sorted_words_dict.get(i*(i+1)/2))

        decode_message = " ".join(pyramid)
        return decode_message
