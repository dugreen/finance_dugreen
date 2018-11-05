#!coding:utf-8

import csv
from collections import namedtuple

def read_csv():
    with open("./601318.csv","rt") as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        # print(headings)
        # exit()
        Row = namedtuple('Row',headings)
        for r in f_csv:
            row = Row(*r)
            print(row.date,'  ',row.close)

def write_csv():
    headers = ['Symbol','Price','Date','Time','Change','Volume']
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),\
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),\
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),]
    
    with open('temp.csv','w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

def main():
    write_csv()

if __name__ == "__main__":
    main()
