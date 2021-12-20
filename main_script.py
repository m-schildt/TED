from retriever import retrieve
from decompressor import decompress
from extractor import extractor

# Date to retrieve:
date = "20210705"

# Run retrieve function
gz_file = retrieve(date)

# Run decompress function 
xml_files = decompress(gz_file)

# File name for CSV file
destination = f"daily_report_{date}.csv"  

# Run ectractor
extractor(xml_files, destination)
