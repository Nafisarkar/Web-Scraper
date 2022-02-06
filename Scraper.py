#read data from html
import requests
import io
from Discord_connect import *
from bs4 import BeautifulSoup

#take string as a input and return the last character
def last_char(string):
    return int(string[-1])



def rest_printer(x,url):
    for i in range(x):
            if i>1:
                print("\n\n\n")
                url2 = url + "?page="+str(i);
                print (url2)
                result_alpha = requests.get(url2)
                print("requesting url:",url2)
                soup = BeautifulSoup(result_alpha.text, "html.parser")
                mysoup = soup.find_all('td',{'class':'wide'})
                for a in mysoup:
                    href1 = a.find('a',href=True)
                    print(href1.text)
                    store_input(href1.text)
                #call_dis(href1.text)
        
#store all the input to a text file
def store_input(input_string):
    f.write(input_string+"\n")


                
    

url = input("Enter the url:")
filename = input("Enter the filename:")
f = open(filename+".txt","a")


result = requests.get(url)
html = BeautifulSoup(result.content, "html.parser")
mydivs = html.find_all('td',{'class':'wide'})

for a in mydivs:
    href = a.find('a',href=True)
    print(href.text)
    store_input(href.text)
    #call_dis(href.text)


print("\n\n\n")
#this findes out how many pages we have to scrape
page = html.find('div',{'id':'table-info'})
#print(last_char(page.text))
page_number = int(str(page).split('of')[-1].split('<')[-2].replace(" ",""))
print(page_number)


#this calls the rest_printer function which prints the rest of the pages after the home page
rest_printer(page_number+1,url)

f.close()







