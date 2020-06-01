''' In given lyrics find out the occurrence of each word
and then min/max frequencies of the words using dictionaries '''


# creating a dictionary
def lyrics_to_frequencies(lyrics):
    my_dict = {}
    for word in lyrics:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict


she_loves_you = ["she", "loves", "you", "yeah", "yeah", "yeah", "oh",
                 "oh", "oh", "she", "loves", "you", "yeah", "yeah"]
print(lyrics_to_frequencies(she_loves_you))


# using the dictionary
def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


print(most_common_words(lyrics_to_frequencies(she_loves_you)))


# leveraging dictionary properties of mutation
def words_often(freqs, min_times):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= min_times:
            # print(temp[1])
            result.append(temp)
            for w in temp[0]:
                # print(temp[0])
                del(freqs[w])
        else:
            done = True
    return result


print(words_often(lyrics_to_frequencies(she_loves_you), 3))
