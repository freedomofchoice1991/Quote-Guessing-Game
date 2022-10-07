def displayRandomQuote():
    from random import randint
    from csv import reader

    def randQ():
        id = randint(1,97)
        return id

    with open("quotes.csv") as file:
        csv_reader = reader(file)
        randomQuote = list(csv_reader)[randQ()]

    return (randomQuote[1], randomQuote[2], randomQuote[4], randomQuote[5], randomQuote[3])    
    

# print(displayRandomQuote())

