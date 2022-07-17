import argparse



def get_params() -> dict:
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--customers_location', required=False, default="./input_data/starter/customers.csv")
    parser.add_argument('--products_location', required=False, default="./input_data/starter/products.csv")
    parser.add_argument('--transactions_location', required=False, default="./input_data/starter/transactions/")
    parser.add_argument('--output_location', required=False, default="./output_data/outputs/")
    return vars(parser.parse_args())

f_a = open(customers.csv, 'r')
f_b = open(products.csv, 'r')
while True:
    where_a = f_a.tell()
    line_a = f_a.readline()
    where_b = f_b.tell()
    line_b = f_b.readline()
    if not line_a and not line_b:
        time.sleep(1)
        f_a.seek(where_a)
        f_b.seek(where_b)
        continue
    else:
        if line_a:
            line = line_a
        else:
            line = line_b




def main():
    params = get_params()
    

if __name__ == "__main__":
    main()
