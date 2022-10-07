#!/usr/bin/env python3
# Copyright @reza.karami.arbeiten@gmail.com
#=========================================================================
#Quote Guessing Game
###scrape website " http://quotes.toscrape.com "
#When run, your program will scrape a website for a collection of quotes. 
#Pick one at random and display it.
#The player will have 4 chances to guess who said the quote.
#After every wrong guess they'll get a hint about the author's identity.
#=========================================================================
from scrape import scrap
from startGame import start_game

scrap()         ##We don't need to scrap the website every time / it slows down the program

def main():
    start_game()
    
if __name__ == '__main__': main()    

######End