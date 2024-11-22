import argparse
import requests

# Cool to add
# Karat to Karat Conversion. Example enter 14k output wieght in 10k, 18, 22k and pure gold
# Current Price per gram for all Karats

OUNCE_TO_GRAMS = 31.1035
TROY_OUNCE_TO_GRAMS = 28.3495

def calculate_gold_weight(pure_gold, karat, weight_unit, gold_price):
    if karat == '10k':
        gold_percentage = 0.4167
    elif karat == '14k':
        gold_percentage = 0.5854
    elif karat == '18k':
        gold_percentage = 0.75
    elif karat == '22k':
        gold_percentage = 0.9167
    else:
        print("Invalid karat value. Please enter a valid karat value (10k, 14k, 18k, or 22k).")
        return

    if weight_unit == 'gram':
        pure_gold_grams = pure_gold
        pure_gold_troy_oz = pure_gold / OUNCE_TO_GRAMS
    else:
        pure_gold_troy_oz = pure_gold
        pure_gold_grams = pure_gold * OUNCE_TO_GRAMS

    total_weight = pure_gold_troy_oz / gold_percentage
    weight_in_grams = total_weight * OUNCE_TO_GRAMS
    weight_in_ounces = weight_in_grams / TROY_OUNCE_TO_GRAMS

    total_price = gold_price * pure_gold_troy_oz

    print(f"{pure_gold:.2f} {weight_unit} of pure gold will yield {weight_in_grams:.2f} grams or {weight_in_ounces:.2f} troy ounces of {karat} gold.")
    print(f"The current gold price is {gold_price:.2f} USD per troy ounce.")
    print(f"The total value of {pure_gold:.2f} {weight_unit} of pure gold at {gold_price:.2f} USD per troy ounce is {total_price:.2f} USD.")

def main():
    parser = argparse.ArgumentParser(description='Calculate weight and value of gold in different karats.')
    parser.add_argument('-g', '--pure_gold', type=float, help='Amount of pure gold', required=True)
    parser.add_argument('-k', '--karat', type=str, help='Karat of gold (10k, 14k, 18k, or 22k)', required=True)
    parser.add_argument('-u', '--weight_unit', type=str, help='Unit of weight (gram or oz)', required=True)

    args = parser.parse_args()

    url = 'https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD'
    response = requests.get(url)
    data = response.json()[0]
    gold_price = data['spreadProfilePrices'][0]['bid']

    calculate_gold_weight(args.pure_gold, args.karat, args.weight_unit, gold_price)

if __name__ == '__main__':
    main()

