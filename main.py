import json


def open_json():
    with open("suppliers.json", encoding="UTF-8") as file:
        res = json.load(file)
    return res


def write_sql(data):
    with open('suppliers.sql', 'a', encoding='UTF-8') as file:
        table_suppliers = """CREATE TABLE IF NOT EXISTS suppliers (
        id INT PRIMARY KEY NOT NULL,
        company_name VARCHAR(50),
        contact_name VARCHAR(100),
        contact_title VARCHAR(100),
        country VARCHAR(50),
        region VARCHAR(50),
        post_code VARCHAR(50),
        city VARCHAR(50),
        address VARCHAR(225),
        phone VARCHAR(25),
        fax VARCHAR(25),
        homepage VARCHAR(225)
        );\n\n"""

        file.write(table_suppliers)
        count = 1
        for i in data:
            i['id'] = count
            contact = i['contact'].split(', ')
            address = i['address'].split('; ')

            i['company_name'] = i['company_name'].replace("'", "''")
            address[4] = address[4].replace("'", "''")
            i['homepage'] = i['homepage'].replace("'", "''")

            req = \
                f"INSERT INTO suppliers VALUES ({i['id']}, '{i['company_name']}', '{contact[0]}', '{contact[1]}'" \
                f", '{address[0]}', '{address[1]}', '{address[2]}', '{address[3]}', '{address[4]}', '{i['phone']}'" \
                f", '{i['fax']}', '{i['homepage']}');\n"
            count += 1
            file.write(req)

        update_sql = "\nALTER TABLE products ADD COLUMN id_suppliers INT REFERENCES suppliers(id);\n\n"
        file.write(update_sql)

        for i in data:
            product = [j.replace("'", "''") for j in i['products']]

            up = f"""UPDATE products SET id_suppliers = {i['id']} WHERE product_name IN ('{"', '".join(product)}');\n"""
            file.write(up)


def main():
    data = open_json()
    write_sql(data)


if __name__ == '__main__':
    main()
