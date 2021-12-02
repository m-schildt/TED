## Retrieve XML for given date
from ftplib import FTP

# Next iteration: turn into a function that takes the date in YYYYMMDD format

# Connect
ftp = FTP("ted.europa.eu")
ftp.login("guest", "guest")

# Parse date
date = "20120516"
year = date[0:4]
month = date[4:6]
day = date[6:8]

# Retrieve directory contents for given year/month combination
ftp.cwd("daily-packages/" + year + "/" + month)
# Couldn't find a way to do this without Pandas, should be possible and more efficient
file_names = ftp.nlst()

# Determine filename (should make robust if it doesn't exist)
file_name = [file_name for file_name in file_names if file_name.startswith(date)][0]

# Retrieve file
ftp.retrbinary("RETR " + file_name, open(file_name, 'wb').write)
# Possible improvement for next iteration: add some feedback on status of download.

# Close connection
ftp.quit()

