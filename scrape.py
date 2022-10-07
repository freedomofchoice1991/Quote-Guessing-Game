def scrap():
    import requests
    from bs4 import BeautifulSoup
    from csv import writer
    from time import sleep           ## to delay between scraping request => for not being cut from website

    address = ["https://quotes.toscrape.com/"
    ,"https://quotes.toscrape.com/page/2/"
    ,"https://quotes.toscrape.com/page/3/"
    ,"https://quotes.toscrape.com/page/4/"
    ,"https://quotes.toscrape.com/page/5/"
    ,"https://quotes.toscrape.com/page/6/"
    ,"https://quotes.toscrape.com/page/7/"
    ,"https://quotes.toscrape.com/page/8/"
    ,"https://quotes.toscrape.com/page/9/"
    ,"https://quotes.toscrape.com/page/10/"]




    with open("quotes.csv", "w") as file:
            csv_writer = writer(file)
            csv_writer.writerow(["id","quote", "author", "quote type", "date of Birth", "location of Birth"])
    id = 1
    for a in address:
        response = requests.get(a)
        print(f"Now scraping 👉🏻 {a} ...")
        soup = BeautifulSoup(response.text, "html.parser")
        texts = soup.find_all(class_="quote")

        with open("quotes.csv", "a") as file:
            csv_writer = writer(file)
        
            for t in texts:
                quote = t.find("span").get_text()
                author = t.find("small").get_text()
                q_type = t.find("meta")["content"]
                a_detail = t.find("a")["href"]
                base_url = "http://quotes.toscrape.com"
                a_result = base_url + a_detail
                author_response = requests.get(a_result)
                author_soup = BeautifulSoup(author_response.text, "html.parser")
                a_info = author_soup.find_all("span")
                

                if len(quote) > 320:
                    continue
                csv_writer.writerow([id,quote,author,q_type, a_info[0].get_text(),a_info[1].get_text()]) 
                

                id += 1
        sleep(5)      ## to delay between scraping request => for not being cut from website      

    
if __name__ == '__scrap__': scrap() 





###############################################
####  Reading the csv file as a dict or list ##
###############################################
# from csv import DictReader
# def read_quotes(filename):
#     with open (filename, 'r') as file:
#         csv_reader = DictReader(file)
#         # for thing in csv_reader:
#         #     print(thing)
#         #     print("================================================================")
#         return list (csv_reader)    

# listOfQuotes = read_quotes("quotes.csv")     
# print(listOfQuotes[0])  
 
####################################
####################################
