#read data from html
import requests
from bs4 import BeautifulSoup



def page_(url3):
    url3 = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
    result_alpha = requests.get(url3)
    soup = BeautifulSoup(result_alpha.text, "html.parser")
    mysoup = soup.find_all('td',{'class':'wide'})
    for a in mysoup:
        href = a.find('a',href=True)
        print(href.text)

#take string as a input and return the last character
def last_char(string):
    return int(string[-1])



def rest_printer(x,url):
    for i in range(x):
            print("\n\n\n")
            url2 = url + "?page="+str(i);
            print (url2)
            
            result_alpha = requests.get(url2)
            print("requesting url:",url2)
            soup = BeautifulSoup(result_alpha.text, "html.parser")
            mysoup = soup.find_all('td',{'class':'wide'})
            for a in mysoup:
                href = a.find('a',href=True)
                print(href.text)
        
        
                
    

url = input("Enter the url:")

result = requests.get(url)
html = BeautifulSoup(result.content, "html.parser")
mydivs = html.find_all('td',{'class':'wide'})

for a in mydivs:
    href = a.find('a',href=True)
    print(href.text)


print("\n\n\n")
#this findes out how many pages we have to scrape
page = html.find('div',{'id':'table-info'})
#print(last_char(page.text))

#this converts the string to an integer
page_number = last_char(page.text)

#this calls the rest_printer function which prints the rest of the pages after the home page
rest_printer(page_number+1,url)







