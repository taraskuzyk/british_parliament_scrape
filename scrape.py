import bs4
import pandas as pd
import requests


def get_petition_name(soup: bs4.BeautifulSoup):
    h1 = soup.find("h1")
    petition_name = h1.text.replace("Closed petition", "")
    petition_name = petition_name.replace("Rejected petition", "")
    return petition_name.strip()


def run_scrape():
    df = pd.read_csv("Scraped_Data.csv")
    df = pd.DataFrame(df)

    for i in range(len(df)):
        if isinstance(df["Text"][i], float) and df["Text"][i] != df["Text"][i]:
            df["Text"][i] = text_scrape(df["URL"][i])
            df.to_csv("Scraped_Data.csv")
            print(str(i / len(df) * 100) + "%", len(df))


def text_scrape(website):
    response = requests.get(website)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    text_bulk = ""
    text_bulk_array = soup.find_all("p")

    for i in text_bulk_array[2::]:

        try:
            if i["class"] == ["flash-notice"]:
                break
        except:
            pass

        text_bulk += i.text.strip()
        text_bulk = text_bulk.replace("\n", "")
        text_bulk = text_bulk.replace(",", "")
        text_bulk = text_bulk.replace(";", "")
    return text_bulk


if __name__ == "__main__":
    run_scrape()
