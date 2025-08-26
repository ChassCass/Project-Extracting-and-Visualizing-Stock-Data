# Importar las librerías necesarias
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Hacer una petición HTTP a la página web
url = "https://lottery.mt/lotto/results/history"
res = requests.get(url)

# Crear un objeto BeautifulSoup con el contenido de la respuesta
soup = BeautifulSoup(res.text, "html.parser")

# Buscar la tabla que contiene los datos de los sorteos
table = soup.find("table", class_="table table-striped table-bordered table-hover")

# Obtener los nombres de las columnas de la tabla
columns = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]

# Obtener los datos de cada fila de la tabla
data = []
for tr in table.find("tbody").find_all("tr"):
    row = [td.get_text(strip=True) for td in tr.find_all("td")]
    data.append(row)

# Crear un DataFrame de pandas con los datos y las columnas
df = pd.DataFrame(data, columns=columns)

# Filtrar el DataFrame por el periodo de tiempo deseado
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
start_date = "2023-01-01"
end_date = "2023-12-19"
mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
df = df.loc[mask]

# Guardar el DataFrame en un archivo CSV
df.to_csv("lottery_data.csv", index=False)

#https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/
#https://www.octoparse.com/blog/scraping-data-from-website-to-excel
#https://careerfoundry.com/en/blog/data-analytics/web-scraping-guide/




#Codigo ChatGPT 3.5
Asegúrate de tener instaladas las bibliotecas necesarias ejecutando:
pip install requests
pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv

url = "https://lottery.mt/lotto/results/history"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Aquí necesitarás inspeccionar la página para encontrar la estructura HTML específica de los datos que deseas extraer.
    # Reemplaza las etiquetas y atributos según la estructura real de la página.
    data_table = soup.find("table", {"class": "table-class"})
    
    # Crear un archivo CSV para escribir los datos
    csv_filename = "lottery_data.csv"
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Escribir encabezados
        csv_writer.writerow(["Día", "Fecha", "Sorteo", "Resultados"])

        # Iterar a través de las filas de la tabla
        for row in data_table.find_all("tr")[1:]:
            columns = row.find_all("td")
            day = columns[0].text.strip()
            date = columns[1].text.strip()
            draw = columns[2].text.strip()
            results = columns[3].text.strip()

            # Escribir la fila en el archivo CSV
            csv_writer.writerow([day, date, draw, results])

    print(f"Los datos se han guardado en {csv_filename}")
else:
    print(f"No se pudo acceder a la página. Código de estado: {response.status_code}")


#Ten en cuenta que este código es solo un ejemplo genérico y puede no funcionar directamente en tu caso. Necesitarás ajustar las etiquetas y atributos específicos según la estructura HTML de la página que estás consultando. Además, ten en cuenta las restricciones legales y éticas al acceder y utilizar datos de sitios web. Asegúrate de cumplir con los términos de servicio del sitio web en cuestión.#