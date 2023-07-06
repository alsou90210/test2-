import requests 
from bs4 import BeautifulSoup 
# для защиты от бана 
headers = {
    'Accept':'*/*',
    'User-Agent': ''
}




url ='https://www.kivano.kg/mobilnye-telefony'
req = requests.get(url,headers=headers)

bs4 = BeautifulSoup(req.text,'html.parser')


items = bs4.findAll('div',class_ = 'item product_listbox oh')

print(items)

for item in items:
    # result = item.find('div',class_ = 'listbox_title oh').get_text(strip = True)
    # result_name = item.find('div',class_ = 'listbox_price text-center').get_text(strip = True)
    result_tar = item.find('div',class_= 'product_text pull-left').get_text(strip = True)
    # print(result_name)
#     # print(result)
    print(result_tar)




import requests 
from bs4 import BeautifulSoup 
# для защиты от бана 
headers = {
    'Accept':'*/*',
    'User-Agent': ''
}




url ='https://telefon.kg/smartphone'
req = requests.get(url,headers=headers)

bs4 = BeautifulSoup(req.text,'html.parser')


items = bs4.findAll('div',class_ = 'caption')

print(items)

for item in items:
#     result = item.find('p',class_ = 'description').get_text(strip = True)
#     result_price = item.find('p',class_ = 'price').get_text(strip = True)
#     result_tar = item.find('a').get('href')
    # print(result_price)
    # print(result)
    # print(result_tar)
    result = item.find('p',class_ = 'description').get_text(strip = True)
    with open('description.txt','a') as file_description:
        file_description.write(f'{result}\n')
      
    result_tar = item.find('a').get('href')
    with open('name.txt','a') as file_name:
        file_name.write(f'{result_tar}\n')
        
    result_price = item.find('p',class_ = 'price').get_text(strip = True)
    with open('price.txt','a') as file_price:
        file_price.write(f'{result_price}\n')
        




import requests 
from bs4 import BeautifulSoup 
import csv
headers = {
    'Accept':'*/*',
    'User-Agent': ''
}


url ='https://www.kivano.kg/mobilnye-telefony'
req = requests.get(url,headers=headers)

bs4 = BeautifulSoup(req.text,'html.parser')


items = bs4.findAll('div',class_ = 'item product_listbox oh')



with open('kivani.csv','w',newline='') as csv_file:
    writer = csv.writer(csv_file)


    writer.writerow(['Phone Name', 'Price', 'Description', 'Link'])

    for item in items:
        phone_name = item.find('div', class_ = "listbox_title oh").get_text(strip = True)
        price = item.find('div', class_ = "listbox_price text-center").get_text(strip = True)
        description = item.find('div', class_ = "product_text pull-left").get_text(strip = True)
        link = item.find('a').get('href')
        # print(f"{phone_name} - {price} - {description} - {link}")


        writer.writerow([phone_name,price,description,link])


with open('phones.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    
    writer.writerow(['Phone Name', 'Price', 'Description', 'Link'])

    
    for item in items:
        phone_name = item.find('div', class_="listbox_title oh").get_text(strip=True)
        price = item.find('div', class_="listbox_price text-center").get_text(strip=True)
        description = item.find('div', class_="product_text pull-left").get_text(strip=True)
        link = item.find('a').get('href')

        
        writer.writerow([phone_name, price, description, link])










import requests 
from bs4 import BeautifulSoup 
import csv
headers = {
    'Accept':'*/*',
    'User-Agent': ''
}


url ='https://www.mashina.kg/new/search'
req = requests.get(url,headers=headers)

bs4 = BeautifulSoup(req.text,'html.parser')


items = bs4.findAll('div',class_ = 'listing-item main')



with open('car.csv','w',newline='') as csv_file:
    writer = csv.writer(csv_file)


    writer.writerow(['Cars', 'Price'])

    for item in items:
        cars = item.find('span', class_ = "white font-big").get_text(strip=True)
        price = item.find('span', class_ = "white custom-margins font-small")

        if price is None:
            continue
        else:
            price = price.text
        print(price,cars)    


        writer.writerow([cars, price])  

