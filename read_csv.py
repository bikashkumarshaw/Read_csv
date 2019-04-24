import csv
from flask import Flask, request
import json
import glob
from args import _define_args

app = Flask(__name__)

ARGS = _define_args()

@app.route("/api/read_csv")
def read_csv():
    csv_file = request.args.get("csv_file")
    csv_file = "csv_files/"+csv_file
    columns = request.args.get("columns")
    page = request.args.get("page")
    csvfile = open(csv_file)
    headers = csvfile.readline().strip().split(",")
    if columns:
       fieldnames  = columns.split(",")
    else:
        fieldnames = headers

    if page:
        page = int(page)
    else:
        page = 1

    line = (page-1)*500+1
    reader = csv.DictReader( csvfile, headers)

    resp = {}
    count = 0
    for row in reader:
        count = count+1
        if count<(line+500) and count>=line:
            for field in fieldnames:
                resp.setdefault(field, []).append(row.get(field, ""))

    return json.dumps(resp)

@app.route("/api/list_csv_files")
def list_csv_files():
    csv_files = []
    resp = {}
    for file_name in glob.glob("csv_files/*.csv"):
        f = open(file_name)
        headers = f.readline().strip().split(",")
        resp[file_name.split("/")[1]] = headers

    return json.dumps(resp)

if __name__=="__main__":
    app.run(debug=True, host=ARGS.ip, port=ARGS.port)
