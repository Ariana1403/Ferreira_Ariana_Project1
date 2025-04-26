# Ariana Ferreira
# Project : Lego inventory System
# Description : This program manages LEGO sets in a inventory.


# Function to Load LEGO data from a file
def load_lego_data(file_name):
    lego_data = []

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')

                # Create a dictionaty for each Lego Set
                lego_set = {
                    'set_number': data[0],
                    'title': data[1],
                    'pieces': int(data[2]),
                    'price': float(data[3]),
                    'stock_status': int(data[4]),
                }

                lego_data.append(lego_set)

        return lego_data

    except FileNotFoundError:
        print(f"Error:The file {lego_data} was not found")
        return []

    except Exception as e:
        print(f"An unnexpexcted error occured {e}")
        return []


def display_inventory(lego_data):
    print("\nLego Sets")
    print("_" * 75)

    for lego_set in lego_data:
        set_number = lego_set['set_number']
        title = lego_set['title']
        pieces = f"{lego_set['pieces']:,}"
        price = lego_set['price']

        if lego_set['stock_status'] == 1:
            stock_icon = "✅"
        else:
            stock_icon = "❌"

        retired_marker = ""
        if lego_set['price'] == 0.00:
            retired_marker = "#"

        print(f"{set_number:<7} {title:<40} {pieces:>8} {stock_icon:^5} {price:>8.2f} {retired_marker}")


lego_data = load_lego_data("lego_data.txt")
display_inventory(lego_data)
