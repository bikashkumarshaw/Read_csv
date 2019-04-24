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

command to run the service:

### python read_csv.py --port 2288 --ip `your server ip`

```
Note you need flask installed in your system for this.
```
