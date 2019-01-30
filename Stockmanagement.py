import requests
import logging
import sys
import json
import datetime
#import xlwt
import xlsxwriter

try:
    logging.basicConfig(format='%(levelname)-10s: %(message)s', filename='webAPI.log', filemode='w', level=logging.DEBUG)
    api_key = "gDczuumLx4wMVZmS6hLE"
    share_names = ['BOM531219', 'BOM500209', 'BOM530801', 'BOM538578', 'BOM538577', 'BOM538729', 'BOM539140', 'BOM539139']

    # share_names = ['BOM500209']
    dataset = {}
    companyData = []
    for i in share_names:
        url = 'https://www.quandl.com/api/v3/datasets/BSE/{}.json?api_key={}'.format(i, api_key)
        response = requests.get(url)
        if response.status_code != 200:
            logging.error('ERROR: response type {}'.format(response))
            sys.exit(1)

        content = json.loads(response.content)

        companyName = content['dataset']['name']
        symbol = content['dataset']['dataset_code']
        data = content['dataset']['data']
        print data

        if len(data) > 0:
            lastBusinessDate = data[0][0]
            lastBusinessDateTurnOver = data[0][8]
            secondLastBusinessDate = data[1][0]
            secondLastBusinessDateTurnOver = data[1][8]
            difference = lastBusinessDateTurnOver - secondLastBusinessDateTurnOver
            obj = dict()
            obj["companyName"] = companyName
            obj["symbol"] = symbol
            obj["lastBusinessDate"] = lastBusinessDate
            obj["secondLastBusinessDate"] = secondLastBusinessDate
            obj["lastBusinessDateTurnOver"] = lastBusinessDateTurnOver
            obj["secondLastBusinessDateTurnOver"] = secondLastBusinessDateTurnOver
            obj["difference"] = difference
            print companyData
            # companyData = dataset[data]

            companyData.append(obj)
            print obj

        else:
            print "No data for ", companyName
    else:
        print "Retriving Company data done"
        # Create a workbook and add a worksheet
        filename = "StockManagement.xlsx"
        # excel_file = xlsxwriter.Workbook()
        excel_file = xlsxwriter.Workbook(filename)
        # Light red fill with dark red text.
        format_red_color = excel_file.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})

        format_green_color = excel_file.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
        sheet2 = excel_file.add_worksheet('Company Stock Exchange')
        row = 0
        col = 0
        xf = 0
        # sheet2.write(row, col, value)
        rowCount = 0
        for i in companyData:
            value = i['companyName']
            sheet2.write(rowCount, 0, value)
            value = i['symbol']
            sheet2.write(rowCount, 1, value)
            value = i['lastBusinessDate']
            sheet2.write(rowCount, 2, value)
            value = i['secondLastBusinessDate']
            sheet2.write(rowCount, 3, value)
            value = i['difference']
            sheet2.write(rowCount, 4, value)
            rowCount += 1
        # excel_file.save(filename)
        ColumnRange = 'E1:E{}'.format(rowCount)
        # Write a conditional format over a range.
        sheet2.conditional_format(ColumnRange, {'type': 'cell', 'criteria': '>', 'value': 0, 'format': format_green_color})
        # Write a conditional format over a range.
        sheet2.conditional_format(ColumnRange, {'type': 'cell', 'criteria': '<=', 'value': 0, 'format': format_red_color})

        excel_file.close()
except Exception as E:
    print "Exception : ", E
finally:
    print "File Created Successfully..."
    pass
