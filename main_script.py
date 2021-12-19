from retrieve import retrieve

from decompressor import decompress

from scraper import scraper

date = "20211217"

gz_file = retrieve(date)

xml_files = decompress(gz_file)

destination = f"daily_report_{date}.csv"  

scraper(xml_files, destination)
