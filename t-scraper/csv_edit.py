import csv

with open('./daru1000.csv', 'r', newline='', encoding='utf-16') as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t', quoting=csv.QUOTE_ALL)
    for line in reader:
        if line[9] == "Image_URL":
            continue
        print(line[0])
        with open('./daru1000_edit.csv', 'a', newline='', encoding='utf-16') as f:
            writer = csv.writer(f, dialect='excel', delimiter='\t', quoting=csv.QUOTE_ALL)
            writer.writerow(
                ['deru1000_' + line[0], line[1], line[2].replace("\n", ""), line[3], line[4], line[5], line[6], line[7],
                 line[8],
                 'deru1000_' + line[0]])
