import sys, getopt, csv

import datetime

def main(argv):
    inputfile = ''
    outputfile = ''
    ordernumber = ''
    sonumber = ''
    
    try:
        opts, args = getopt.getopt(argv,"hu:i:o:n:s:",["username=","ifile=","ofile=","norder=","soorder="])
    except getopt.GetoptError:
        print ('test.py -u <username> -i <inputfile> -o <outputfile> -n <ordernumber> -s <sonumber>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile> -n <ordernumber> -s <sonumber>')
            sys.exit()
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n","--norder"):
            ordernumber = arg
        elif opt in ("-s","--soorder"):
            sonumber = arg
    print ('Fishbowl username of the data importer is "', username,'"')
    print ('Input file is "', inputfile,'"')
    print ('Output file is "', outputfile,'"')
    print ('Order number is "', ordernumber,'"')
    print ('Sale Order number is "', sonumber,'"')
    
    with open(inputfile+'.csv') as inFile:

        data = list ((csv.reader(inFile)))

        orders = []
        orders_occurences = [data[o][0] for o in range(1,len(data))]
        for o in orders_occurences:
            if o not in orders:
                orders.append(o)
        
        items = []
        first_line_order_index = [2]
        for o in orders:
            items.append(sum([1 for d in data if o in d]))

        for i in range(len(items)):
            first_line_order_index.append(1+sum(items[:i+1]))
        first_line_order_index=first_line_order_index[:-1]

        orders_items = list()
        sonumbers = []
        sonumber_int = int(sonumber)
        for i in range(len(orders)):
            orders_items.append([orders[i],first_line_order_index[i]])
            sonumbers.append([orders[i],sonumber_int])
            sonumber_int += 1
        
        orders_dict = dict(orders_items)
        sonumbers_dict = dict(sonumbers)
        
        for d in data[1:]:
            for i in orders:
                if i in d and data.index(d)==orders_dict[i]:
                    if d[41]!='CA':
                        TaxCode='Out of State'
                    else:
                        TaxCode=d[39]
                    print (['SO',sonumbers_dict[i],'10',d[24],d[24],d[24],d[26]+d[27],d[29],d[31],d[30],d[32],d[34],d[36]+d[37],d[39],d[41],d[40],d[42],'FALSE',d[14],TaxCode,'30',d[0],'',d[15][0:10],username,'','','Origin',d[44],'None','Main',datetime.date.today().strftime('%m/%d/%Y'),'','','',d[33],d[1],'','','',''])
                    print (['Item','10',d[20],'',d[16],'',d[18]])
                elif i in d and data.index(d)!=orders_dict[i]:
                    if d[41]!='CA':
                        TaxCode='Out of State'
                    else:
                        TaxCode=d[39]
                    print (['Item','10',d[20],'',d[16],'',d[18]])
                                
 
#    with open(outputfile+'.csv', 'wt', newline='') as outFile:
#        writer = csv.writer(outFile)
#        writer.writerow(['Flag','SONum','Status','CustomerName','CustomerContact','BillToName','BillToAddress','BillToCity','BillToState','BillToZip','BillToCountry','ShipToName','ShipToAddress','ShipToCity','ShipToState','ShipToZip','ShipToCountry','ShipToResidential','CarrierName','TaxRateName','PriorityId','PONum','VendorPONum','Date','Salesman','ShippingTerms','PaymentTerms','FOB','Note','QuickBooksClassName','LocationGroupName','OrderDateScheduled','URL','CarrierService','DateExpired','Phone','Email','CF-Custom 1','CF-Custom 2','CF-Custom 3','CF-Custom 4'])
#        writer.writerow(['Flag','SOItemTypeID','ProductNumber','ProductDescription','ProductQuantity','UOM','ProductPrice','Taxable','TaxCode','Note','QuickBooksClassName','ItemDateScheduled','ShowItem','KitItem','RevisionLevel'])

#        i=0
        
#        for row in fileReader:
#            if row['Shipping Province']!='CA':
#                TaxCode='Out of State'
#            else:
#                TaxCode=row['Shipping City'] 

            #if row['Name']=='#'+ordernumber:
#                if i==0:
#                    writer.writerow (['SO',sonumber,'10',row['Billing Name'],row['Billing Name'],row['Billing Name'],row['Billing Address1']+row['Billing Address2'],row['Billing City'],row['Billing Province'],row['Billing Zip'],row['Billing Country'],row['Shipping Name'],row['Shipping Address1']+row['Shipping Address2'],row['Shipping City'],row['Shipping Province'],row['Shipping Zip'],row['Shipping Country'],'FALSE',row['Shipping Method'],TaxCode,'30',ordernumber,'',row['Created at'][0:10],username,'','','Origin',row['Notes'],'None','Main',datetime.date.today(),'','','',row['Billing Phone'],row['Email'],'','','',''])
#                    writer.writerow (['Item','10',row['Lineitem sku'],'',row['Lineitem quantity'],'',row['Lineitem price']])
#                    i+=1
#                else:
#                    writer.writerow (['Item','10',row['Lineitem sku'],'',row['Lineitem quantity'],'',row['Lineitem price']])
#                    i+=1
#    outFile.close()

    inFile.close()

if __name__ == "__main__":
   main(sys.argv[1:])
