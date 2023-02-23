''' A python program to build a system that will tell you what to watch next based on the word
    vector similarity of the description of movies.  The function to return which movies a user would watch
    next if they have watched Planet Hulk with the description as given.
    The list of moveis to watch next is given in movies.txt'''

import spacy
nlp = spacy.load('en_core_web_lg')

sentence_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, " \
                      "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the " \
                      "Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold " \
                      "into slavery and trained as a gladiator."

# read from movies.txt file and store each line as a list in sentences list
with open("movies.txt", "r" , encoding="utf-8") as file:
    sentences = file.read().split('\n')

model_sentence = nlp(sentence_to_compare)

# the 2D array next_movie_list will contain movie name similarity
next_movie_list = []

# iterating over the sentences list and comparing with model_sentence to determine similarity value
for sentence in sentences:
  similarity = nlp(sentence).similarity(model_sentence)
  # print(sentence[:8] + " - ", similarity)
  temp = [sentence[:8] , similarity]
  next_movie_list.append(temp)

# print(next_movie_list)

max_similarity_value = 0
# finding the index of movie which has the highest similarity value
for i in range(0,len(next_movie_list)):
  if next_movie_list[i][1] > max_similarity_value :
    max_similarity_value = next_movie_list[i][1]
    max_similarity_index = i

# print(next_movie_list[max_similarity_index])

# printing the next-to-watch recommendation
print(f"\nWith the highest similarity index of {next_movie_list[max_similarity_index][1]} , "
      f"the most recommended movie to watch next is \" {next_movie_list[max_similarity_index][0]}\" ")

