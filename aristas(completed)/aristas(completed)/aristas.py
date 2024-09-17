import json,csv, requests
from bs4 import BeautifulSoup


product_list_header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "_gcl_au=1.1.1549122772.1716961563; _ga=GA1.1.1084908900.1716961566; __hstc=137092719.ae4b872b950bbfb17491266163c2c5de.1716961594074.1716961594074.1716961594074.1; hubspotutk=ae4b872b950bbfb17491266163c2c5de; messagesUtk=13d295cbff5146c9995e4b32fe6c0c1f; nitroCachedPage=1; _clck=1ox69cq%7C2%7Cfmm%7C0%7C1610; _ga_Q7SW174SG7=GS1.1.1718341951.3.1.1718341975.36.0.1163976861; _clsk=10zvog2%7C1718341975988%7C2%7C1%7Cd.clarity.ms%2Fcollect",
    "Priority": "u=0, i",
    "Referer": "https://aristas.co/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Service-Worker-Navigation-Preload": "true",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}


urls = [
    "https://aristas.co/categoria-producto/salas/sofas",
    "https://aristas.co/categoria-producto/salas/salas-en-l", 
    "https://aristas.co/categoria-producto/salas/sofa-camas",
    "https://aristas.co/categoria-producto/salas/reclinables",
    "https://aristas.co/categoria-producto/salas/sillones-y-poltronas",
    "https://aristas.co/categoria-producto/salas/puff",
    "https://aristas.co/categoria-producto/salas/mesas-de-centro",
    "https://aristas.co/categoria-producto/salas/mesas-auxiliares",
    "https://aristas.co/categoria-producto/salas/aparadores",
    "https://aristas.co/categoria-producto/salas/modulos-flotantes",
    "https://aristas.co/categoria-producto/comedores/juegos-de-comedor-8-puestos",
    "https://aristas.co/categoria-producto/comedores/juegos-de-comedor-6-puestos", 
    "https://aristas.co/categoria-producto/comedores/juegos-de-comedor-4-puestos",
    "https://aristas.co/categoria-producto/comedores/mesas-de-comedor-8-puestos",
    "https://aristas.co/categoria-producto/comedores/mesas-de-comedor-6-puestos",
    "https://aristas.co/categoria-producto/comedores/mesas-de-comedor-4-puestos",
    "https://aristas.co/categoria-producto/comedores/sillas-de-comedor",
    "https://aristas.co/categoria-producto/comedores/sillas-bar",
    "https://aristas.co/categoria-producto/comedores/bifes-y-aparadores",
    "https://aristas.co/categoria-producto/dormitorios/camas",
    "https://aristas.co/categoria-producto/dormitorios/cama-+-colchon",
    "https://aristas.co/categoria-producto/dormitorios/cabeceros",
    "https://aristas.co/categoria-producto/dormitorios/mesas-de-noche",
    "https://aristas.co/categoria-producto/dormitorios/colchones",
    "https://aristas.co/categoria-producto/dormitorios/comodas-y-aparadores",
    "https://aristas.co/categoria-producto/estudios/sofa-camas",
    "https://aristas.co/categoria-producto/estudios/reclinables", 
    "https://aristas.co/categoria-producto/estudios/escritorios",
    "https://aristas.co/categoria-producto/estudios/sillas-de-oficina",
    "https://aristas.co/categoria-producto/estudios/bibliotecas",
    "https://aristas.co/categoria-producto/accesorios/espejos",
    "https://aristas.co/categoria-producto/accesorios/esculturas"
    ]

result = []
for url in urls:
    if url == "https://aristas.co/categoria-producto/dormitorios/colchones":
        sub_urls = [
            "https://aristas.co/categoria-producto/dormitorios/colchones/king-2-00-metros/",
            "https://aristas.co/categoria-producto/dormitorios/colchones/queen-1-60-metros/",
            "https://aristas.co/categoria-producto/dormitorios/colchones/doble-1-40-metros/",
            "https://aristas.co/categoria-producto/dormitorios/colchones/semidoble-1-20-metros/",
            "https://aristas.co/categoria-producto/dormitorios/colchones/sencilla-1-00-metros/",
        ]
        for sub_url in sub_urls:
            response = requests.get(sub_url, headers=product_list_header)
            if response.status_code == 200:
                colchone_soup = BeautifulSoup(response.content, "html.parser")
                categories_txt = colchone_soup.find("nav").text
                print(categories_txt)
                # Categories
                categories = categories_txt.split("/ ")[1].split(" /")[0]
                linea = categories_txt.split(f'{categories}/ ')[1].split(" /")[0]
                sublinea = categories_txt.split(f'{linea} / ')[1]
                print(categories)
                print(linea)
                print(sublinea)
                # Get product URLs
                products = colchone_soup.find_all("div", {"class":"image-fade_in_back"})
                product_prices = str(colchone_soup).split("image-fade_in_back")[1:]

                products_price1 = []
                products_price2 = []
                for product_price in product_prices:
                    product_price_range = product_price.split('<div class="price-wrapper">')[1].split('</span> </div> </div> </div> <span')[0]
                    if "<ins>" in product_price:
                        product_price1 = product_price_range.split('<ins><span class="woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">$</span>')[1].split('</bdi>')[0].replace(",","")
                        product_price2 = ""
                        products_price1.append(product_price1)
                        products_price2.append(product_price2)
                    else:
                        product_price1 = product_price_range.split('<bdi><span class="woocommerce-Price-currencySymbol">$</span>')[1].split('</bdi></span>')[0].replace(",","")
                        # print(product_price1)
                        product_price2 = product_price_range.split('</span> – <span class="woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">$</span>')[1].split('</bdi></span>')[0].replace(",","")
                        # print(product_price1, product_price2)
                        products_price1.append(product_price1)
                        products_price2.append(product_price2)
                print(len(products_price1), len(products_price2))
                product_urls = []
                for product in products:
                    product_url = product.find("a")["href"]
                    product_urls.append(product_url)
                i = 0
                print(len(products))
                product_urls = []
                for product in products:
                    product_url = product.find("a")["href"]
                    product_urls.append(product_url)
                for product in product_urls:
                    print(product)
                    # Variables
                    product_name = ""
                    product_price1 = products_price1[i]
                    product_price2 = products_price2[i]
                    product_medidas = ""
                    product_structure = ""
                    product_form = ""
                    product_tela = ""
                    product_origin = ""
                    product_delivery_time = ""

                    product_paint = ""
                    product_certification = ""
                    product_materiales = ""
                    img_url = ""

                    # Get content
                    product_response = requests.get(product)
                    product_soup = BeautifulSoup(product_response.content, "html.parser")

                    # Get Product Detail Info
                    product_name = product_soup.find("h1", {"class":"product_title"}).get_text()

                    if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_estructura"}):
                        product_structure = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_estructura"}).find("td").find("p").text
                    if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_pa_tiempo-de-entrega"}):
                        product_structure = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_pa_tiempo-de-entrega"}).find("td").find("p").text
                    if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_tiempo-de-entrega"}):
                        product_delivery_time = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_tiempo-de-entrega"}).find("td").find("p").text
                    if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_espuma"}):
                        product_form = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_espuma"}).find("td").find("p").text
                    if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_tela"}):
                        product_tela = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_tela"}).find("td").find("p").text
                    if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_origen"}):
                        product_origin = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_origen"}).find("td").text
                    if product_soup.find("tr",{"class":"woocommerce-product-attributes-item--attribute_madera-y-pintura"}):
                        product_paint = product_soup.find("tr",{"class":"woocommerce-product-attributes-item--attribute_madera-y-pintura"}).find("td").text
                    if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_certificaciones"}):
                        product_certification = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_certificaciones"}).find("td").text
                    if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_materiales"}):
                        product_certification = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_materiales"}).find("td").text
                    if product_soup.find("div", {"class":"jet-woo-product-gallery__image-item"}):
                        img_url = product_soup.find("div", {"class":"jet-woo-product-gallery__image-item"}).find("a")["href"]
                    
                    print(product_name)
                    print(product_price1)
                    print(product_price2)
                    print(product_medidas)
                    print(product_structure)
                    print(product_form)
                    print(product_tela)
                    print(product_origin)
                    print(product_delivery_time)

                    print(product_paint)
                    print(product_certification)
                    print(product_materiales)
                    print(img_url)

                    product_data = {
                        "Categorias":categories,
                        "Linea":linea,
                        "Sublinea":sublinea,
                        "Nombre":product_name,
                        "Precio1":product_price1,
                        "Precio2":product_price2,
                        "Medidas":product_medidas,
                        "Estructura":product_structure,
                        "Espuma":product_form,
                        "Tela":product_tela,
                        "Origen":product_origin,
                        "Certifications":product_certification,
                        "Tiempo de entrega":product_delivery_time,
                        "Materiales": product_materiales,
                        "Img_url": img_url,
                        "Product_url": product

                    }

                    result.append(product_data)
                    i += 1
                    with open("./aristas/aristas.json","w") as file:
                        json.dump(result, file)

                    # JSON data
                    with open("./aristas/aristas.json", "r") as file:
                        json_data = json.load(file)

                    # Define CSV file name
                    csv_file = './aristas/aristas.csv'

                    # Define fieldnames for CSV header
                    fieldnames = json_data[0].keys()

                    # Write JSON data to CSV 
                    with open(csv_file, mode='w', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        for item in json_data:
                            writer.writerow(item)
            else:
                pass
    else:
        response = requests.get(url, headers=product_list_header)
        print(response.status_code)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Get category, linea, sublinea
            categories_txt = soup.find("nav").text
            categories = categories_txt.split("/ ")[1]
            linea = categories_txt.split("/ ")[1]
            sublinea = categories_txt.split(f'{linea}/ ')[1]

            # Get product URLs
            products = soup.find_all("div", {"class":"image-fade_in_back"})
            product_prices = str(soup).split("image-fade_in_back")[1:]
            # with open("products1.html", "w", encoding="utf-8") as file:
            #     file.write(str(product_prices))
            products_price1 = []
            products_price2 = []

            for product_price in product_prices:
                try:
                    product_price_range = product_price.split('<div class="price-wrapper">')[1].split('</span> </div> </div> </div> <span')[0]
                    
                    if "<ins>" in product_price:
                        try:
                            product_price1 = product_price_range.split('<ins><span class="woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">$</span>')[1].split('</bdi>')[0].replace(",","")
                            product_price2 = " "
                        except IndexError:
                            product_price1 = "N/A"
                            product_price2 = "N/A"
                    else:
                        try:
                            product_price1 = product_price_range.split('<bdi><span class="woocommerce-Price-currencySymbol">$</span>')[1].split('</bdi></span>')[0].replace(",","")
                            product_price2 = product_price_range.split('</span> – <span class="woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">$</span>')[1].split('</bdi></span>')[0].replace(",","")
                        except IndexError:
                            # If the second price is not found, set it to the same as the first price
                            try:
                                product_price1 = product_price_range.split('<bdi><span class="woocommerce-Price-currencySymbol">$</span>')[1].split('</bdi></span>')[0].replace(",","")
                                product_price2 = product_price1
                            except IndexError:
                                product_price1 = "N/A"
                                product_price2 = "N/A"
                    
                    products_price1.append(product_price1)
                    products_price2.append(product_price2)
                
                except IndexError:
                    # If the initial split fails, append "N/A" for both prices
                    products_price1.append("N/A")
                    products_price2.append("N/A")
            product_urls = []
            for product in products:
                product_url = product.find("a")["href"]
                product_urls.append(product_url)
            i = 0
            for product in product_urls:
                # Variables
                product_name = ""
                product_price1 = products_price1[i]
                product_price2 = products_price2[i]
                product_medidas = ""
                product_structure = ""
                product_form = ""
                product_tela = ""
                product_origin = ""
                product_delivery_time = ""

                product_paint = ""
                product_certification = ""
                product_materiales =""
                img_url = ""

                # Get content
                product_response = requests.get(product)
                product_soup = BeautifulSoup(product_response.content, "html.parser")

                # with open("dormitorisproduct.html", "w", encoding='utf-8') as file:
                #     file.write(str(product_soup))
                # Get Product Detail Info
                product_name = product_soup.find("h1", {"class":"product_title"}).get_text()

                if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_estructura"}):
                    product_structure = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_estructura"}).find("td").find("p").text
                if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_pa_tiempo-de-entrega"}):
                    product_structure = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_pa_tiempo-de-entrega"}).find("td").find("p").text
                if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_tiempo-de-entrega"}):
                    product_delivery_time = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_tiempo-de-entrega"}).find("td").find("p").text
                if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_espuma"}):
                    product_form = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_espuma"}).find("td").find("p").text
                if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_tela"}):
                    product_tela = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_tela"}).find("td").find("p").text
                if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_origen"}):
                    product_origin = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_origen"}).find("td").text
                if product_soup.find("tr",{"class":"woocommerce-product-attributes-item--attribute_madera-y-pintura"}):
                    product_paint = product_soup.find("tr",{"class":"woocommerce-product-attributes-item--attribute_madera-y-pintura"}).find("td").text
                if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_certificaciones"}):
                    product_certification = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_certificaciones"}).find("td").text
                if product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_materiales"}):
                    product_certification = product_soup.find("tr", {"class":"woocommerce-product-attributes-item--attribute_materiales"}).find("td").text
                if product_soup.find("div", {"class":"jet-woo-product-gallery__image-item"}):
                    img_url = product_soup.find("div", {"class":"jet-woo-product-gallery__image-item"}).find("a")["href"]
                
                # print(product_name)
                # print(product_price1)
                # print(product_price2)
                # print(product_medidas)
                # print(product_structure)
                # print(product_form)
                # print(product_tela)
                # print(product_origin)
                # print(product_delivery_time)

                # print(product_paint)
                # print(product_certification)
                # print(product_materiales)
                # print(img_url)

                product_data = {
                    "Categorias":categories,
                    "Linea":linea,
                    "Sublinea":sublinea,
                    "Nombre":product_name,
                    "Precio1":product_price1,
                    "Precio2":product_price2,
                    "Medidas":product_medidas,
                    "Estructura":product_structure,
                    "Espuma":product_form,
                    "Tela":product_tela,
                    "Origen":product_origin,
                    "Certifications":product_certification,
                    "Tiempo de entrega":product_delivery_time,
                    "Materiales": product_materiales,
                    "Img_url": img_url,
                    "Product_url": product

                }

                result.append(product_data)
                i += 1
                with open("aristas.json","w") as file:
                    json.dump(result, file)

                # JSON data
                with open("aristas.json", "r") as file:
                    json_data = json.load(file)

                # Define CSV file name
                csv_file = 'aristas.csv'

                # Define fieldnames for CSV header
                fieldnames = json_data[0].keys()

                # Write JSON data to CSV 
                with open(csv_file, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    for item in json_data:
                        writer.writerow(item)

        else:
            pass

# Get Subcategory urls
        

# url = "https://aristas.co/categoria-producto/dormitorios/"

# response = requests.get(url, headers=product_list_header)
# soup = BeautifulSoup(response.content, "html.parser")
# with open("newproduct.html", "w", encoding="utf-8") as file:
#     file.write(str(soup))
# subcategories = soup.find_all("h2", {"class":"subcategory-divider"})
# subcategory_urls = []
# for subcategory in subcategories:
#     text = subcategory.get_text()
#     import unicodedata
#     # Normalize the text such as "Sof*á" into "Sof*a"
#     normalized_text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
#     print(normalized_text)
#     # Configure the subcategory url
#     subcategory_url = ""
#     if " " in text:
#         subcategory_url = f'{url}{normalized_text.replace(" ", "-").lower()}'
#     else:
#         subcategory_url = f'{url}{normalized_text.lower()}'
#     subcategory_urls.append(subcategory_url)

# print(subcategory_urls)
