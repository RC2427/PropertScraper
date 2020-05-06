# start_url = ['https://www.propertywala.com/properties/type-residential_apartment_flat/for-rent/location-pune_maharashtra/bedrooms-4/price-6/postedby-owner']
#
#
import scrape.FileRead as file


def walaurlgen():
    # eraser = open('url.txt', 'r+')
    # eraser.truncate()
    # eraser.close()

    input_list = file.form_reader()
    print(input_list)
    temp_city = input_list[0]
    city = file.find_city(temp_city)
    bhk = input_list[1]
    min = input_list[2]
    type1 = input_list[4]
    type_of_sale = input_list[5]
    url = ''
    if type_of_sale == 'rent':
        tem_max = input_list[3]
        max = file.find_price(tem_max)
        url = "https://www.propertywala.com/properties/type-residential_apartment_flat/for-rent/location-" + city + "/bedrooms-" + bhk + "/price-" + max
    if type_of_sale == 'sale':
        tem_max = input_list[3]
        max = file.find_price_Buy(tem_max)
        url = "https://www.propertywala.com/properties/type-residential_apartment_flat/for-sale/location-" + city + "/bedrooms-" + bhk + "/price-" + max
    writer = open('/home/rc/Documents/scrapetest2/scrape/url.txt', 'r+')
    writer.writelines(url)
    writer.close()


def magicurlgen():
    input_list = file.form1_reader()
    print(input_list)
    city = input_list[0]
    bhk = input_list[1]
    type1 = input_list[4]
    type_of_sale = input_list[5]
    print(type_of_sale)
    url = ''
    if type_of_sale == 'rent':
        min = input_list[2]
        max = input_list[3]
        print(max)
        url = "https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=" + bhk +"&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa&cityName="+city+"&BudgetMin="+min+"&BudgetMax="+max
    if type_of_sale == 'sale':
        min = input_list[2]
        max = input_list[3]
        url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=" + bhk + "&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa&cityName=" + city + "&BudgetMin=" + min + "&BudgetMax=" + max


    writer = open('/home/rc/Documents/scrapetest2/scrape/url1.txt', 'r+')
    writer.writelines(url)
    writer.close()


walaurlgen()