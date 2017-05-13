import csv
import codecs
d = {}
d2 = {}
d3 = {}
with codecs.open('123.csv', 'r', 'gb2312') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        sku = row['sku']
        raw_material = row['product']
        quantity = row['number']
        unit = row['unit']
#       print(sku, raw_material)
        if sku not in d:
            d[sku] = [raw_material]
            d2[sku] = [quantity]
            d3[sku] = [unit]
        else:
            d[sku] = d[sku] + [raw_material]
            d2[sku] = d2[sku] + [quantity]
            d3[sku] = d3[sku] + [unit]

with codecs.open('test.csv','w','gb2312') as f:
    for k in d:
        key = '"' + k + '"'
        v = d[k]
        value = ''
        for vv in v:
            value = value + ',' + vv
        value = '"' + value[1:] + '"'
        v2 = d2[k]
        value2 = ''
        for vv2 in v2:
            value2 = value2 + ',' + vv2
        value2 = '"' + value2[1:] + '"'
        v3 = d3[k]
        value3 = ''
        for vv3 in v3:
            value3 = value3 + ',' + vv3
        value3 = '"' + value3[1:] + '"'
            
        line = key + ',' + value + ',' + value2 + ',' + value3
        #print(line)
        f.write(line + '\n')

    f.close()
    
