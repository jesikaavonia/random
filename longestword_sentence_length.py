# Longest word in sentence

# Reading sentence from user

def longestword_sentence_length(text):
    list = []
    text2=text.split(".")
    
    for i in text2:
        list.append(len(i))
        
    longest = max(list)
    
    return ("Longest word is: ", longest)
    return ("And its length is: ", len(longest))
    

print(longestword_sentence_length("HELLO WORLD. MY NAME IS SHOOKIJAN."))
