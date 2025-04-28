def uncommon_from_sentences(sentences):
    word_freq = {}
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1

    unique_words = []

    for word in word_freq:
        if word_freq[word] == 1:
            unique_words.append(word)
    
    return unique_words
