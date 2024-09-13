import re
def validate_credit_card(card_number):
    pattern = r"^[456]\d{3}(-?\d{4}){3}$"
    if not re.match(pattern, card_number):
           return "Invalid: Incorrect format or length"
    card_number_cleaned = card_number.replace("-", "")
    if len(card_number_cleaned) != 16:
           return "Invalid: Must contain exactly 16 digits"
    if re.search(r"(\d)\1{3,}", card_number_cleaned):
           return "Invalid: Contains 4 or more consecutive repeated digits"
    
    return "Valid"
if __name__ == "__main__":
       card_numbers = [
           "6"
           "4123456789123456"
           "5123-4567-8912-3456",
           "61234-567-8912-3456",
           "4123356789123456",
           "5133-3367-8912-3456",
           "5123 - 3567 - 8912 - 3456",
           
       ]
       for card in card_numbers:
             result = validate_credit_card(card)
             print(f"{card}: {result}")