# Read_csv

### Please Keep your csv files into the csv_files folder.

### Use the api link below to get the list of all csv files and their headers
```
http://159.69.60.242:2288/api/list_csv_files
```

#### Use the api link below to read the csv files, you can choose the csf file you want to view and choose the specific colums as well if ou dont specify the colun all the colums are seen
```
http://159.69.60.242:2288/api/read_csv?csv_file=data.csv&columns=user_id,vehicle_model_id&page=2
```

### Api parameters:

**csv_file:** name of the csv file you want to see. (you can use list_csv_files api to get all csv file names)

**columns:** the colums you want to see from the csv file (use list_csv_files api to get the colums of each csv files)

**page:** on each page we show only 500 results we can scroll by increasing the page number.

command to run the service:

### python read_csv.py --port 2288 --ip `your server ip`

```
Note you need flask installed in your system for this.
```

**Note:** its not mandatory for each csv file to have same headers.
