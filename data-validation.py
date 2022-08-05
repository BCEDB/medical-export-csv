import csv
from os import listdir, path

def read_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        try:
            data = [row for row in reader]
        except csv.Error as e:
            print(e)
        
    return data

def log_error(error):
    
    with open('log.csv', 'a', newline='') as logfile:
        writer = csv.writer(logfile)
        writer.writerow(error)

def is_valid_header(file, header):
    """ Checks header data is correct """
    for i, h in enumerate(header):
        error = ["ERROR", file, f"Invalid heading '{h}'"]
        if i == 0 and h != "batch_id":
            error += ["expecting: 'batch_id'"]
            log_error(error)
        if i == 1 and h != "timestamp":
            error += ["expecting: 'timestamp'"]
            log_error(error)
        if i >= 2 and h != f"reading{i-1}":
            error += [f"expecting: 'reading{i-1}'"]
            log_error(error)
    if len(error) <  4:
        return False
    else:
        return True


def main():
    data_path = "./test-files/invalid/"
    data = [f for f in listdir(data_path) if path.isfile(path.join(data_path, f))]

    batch_ids = {}
    for file in data:
        # Read file
        data = read_csv(path.join(data_path, file))
        
        # Validate headers
        header = data[0]
        is_valid_header(file, header)

        # Validate batch_id
        bid = data[1][0]
        if bid in batch_ids:
            error = ["ERROR", file, f"Invalid batch_id '{bid}'", f"Duplicate of {batch_ids[bid]}"]
            log_error(error)
        batch_ids[bid] = file
        


main()