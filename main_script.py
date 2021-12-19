from retrieve import retrieve

from decompressor import decompress

from extractor import extractor

date = "20200918"

gz_file = retrieve(date)

xml_files = decompress(gz_file)

destination = f"daily_report_{date}.csv"  

extractor(xml_files, destination)
