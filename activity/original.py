def uncommon_from_sentences(s1, s2):
    words = s1 + " " + s2 
    words_list = words.split()
    word_freq = {}

    for word in words_list: 
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

    unique_words = []

    for word in word_freq:
        if word_freq[word] == 1:
            unique_words.append(word)
    
    return unique_words

    word_freq = {}
    string = "this is a cat"
    for i in range(len(string)):
        start 
        end 
        if string[i] == " ":
            word_freq[string[start:end]] = 1

