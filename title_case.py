def convert_to_title_case(sentence):
    words_to_be_small = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "nor", "of", "on", "or", "so", "the", "to", "up", "yet", "with", "from", "over", "into", "onto", "upon", "than", "via", "per", "about", "after", "before", "around", "like", "near", "is", "are", "was", "were"
    }
    
    words = sentence.split()
    
    tile_cased_sentence = []
    
    for i, word in enumerate(words):
        if i == 0 or i == len(sentence) -1 or word.lower() not in words_to_be_small:
            tile_cased_sentence.append(word.capitalize())
        else:
            tile_cased_sentence.append(word.lower())
            
    return " ".join(tile_cased_sentence)


print(convert_to_title_case("the name of our beautiful country is bangladesh"))