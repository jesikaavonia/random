def longest_sentence_length(text):
    x=text.split(".")
    length = [len(i) for i in x]
    y=(x[length.index(max(length))])
    return len(y.split())
