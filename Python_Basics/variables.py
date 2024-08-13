#variables are boxes "containers" which contain our data

# Creating first string variable
name = 'Malgus'
profession = 'Sith Lord'

# Create variable containing 'integer'
books_written = 6

# concatenate and print out variables
output = name + ' is a ' + profession + ' and he has written ' + str(books_written) + ' books. '
print(output)

# simpler way to concatenate
output_2 = f"{name} is a {profession} and he has written {books_written} books."
print(output_2)



#Define three new variables with specific names and values:
name = 'Mike'
#genre: assigned the value 'fiction'.
genre = 'fiction'
#first_book: assigned the value "Moon of Solace".
first_book = 'Moon of Solace'
#award: assigned the value "Best Fiction Writer 2023".
award ='Best Fiction Writer 2023'
#Concatenate these new variables to form a new variable:
author_bio = f"{name}, a {genre} writer, is best known for his first book {first_book} and was awarded the {award}."
#author_bio:  "Mike, a fiction writer, is best known for his first book Moon of Solace and was awarded the Best Fiction Writer 2023."
print(author_bio)


