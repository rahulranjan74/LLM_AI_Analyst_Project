from sec_edgar_downloader import Downloader
from bs4 import BeautifulSoup
import os

def sec_filling_downloader(input_ticker):
    download_dir = "D:\PROJECTS\LLM based financial statement Analyser"
    dl = Downloader("IIT Kgp", "aaryanawadh@gmail.com", download_dir)
    dl.get("10-K", input_ticker, limit=29)

    directory_path = f"D:\PROJECTS\LLM based financial statement Analyser\sec-edgar-filings\{input_ticker}\\10-K"
    for root, dirs, files in os.walk(directory_path):
        
        for filename in files:
            file_path = os.path.join(root, filename)
            # Access file using its full path
            with open(file_path, "r") as f1:
                html_content = f1.read()
            soup = BeautifulSoup(html_content, 'lxml')
            text_data = soup.get_text()

            # Save the text data to a file
            with open(f"{download_dir}/{input_ticker}_10k_text.txt", "w", encoding="utf-8") as f:
                f.write(text_data)