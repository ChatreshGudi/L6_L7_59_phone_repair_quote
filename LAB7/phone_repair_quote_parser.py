def mask_imei(imei):
    """
    Keep only ASCII digits and mask all but the last four.

    Invalid input returns an empty string. Short values are fully masked so
    the function never reveals an entire partial IMEI.
    """
    if not isinstance(imei, str):
        return ""

    digits = "".join(character for character in imei if "0" <= character <= "9")
    if not digits:
        return ""
    if len(digits) <= 4:
        return "*" * len(digits)
    return "*" * (len(digits) - 4) + digits[-4:]

def parse_parts_order(text):
    """
    Parse valid 'part xQTY' items into a {part: quantity} dictionary.

    Malformed items, non-positive quantities, and non-string input are ignored.
    """
    order = {}
    if not isinstance(text, str):
        return order

    for item in text.split(";"):
        if "x" not in item:
            continue
        part, qty_text = item.rsplit("x", 1)
        part = part.strip()
        qty_text = qty_text.strip()
        if not part or not qty_text:
            continue
        try:
            quantity = int(qty_text)
        except ValueError:
            continue
        if quantity > 0:
            order[part] = quantity
    return order

def parse_model(text):
    """
    Split 'Brand Model name' into a (brand, model) tuple.

    Missing or invalid values return an empty pair; a one-word value becomes
    the brand with an empty model.
    """
    if not isinstance(text, str):
        return "", ""

    words = text.split()
    if not words:
        return "", ""
    if len(words) == 1:
        return words[0].title(), ""
    return words[0].title(), " ".join(words[1:])

def main():
    print("==== Running mask_imei ====")
    value = input("Enter an IMEI number (e.g. 35-209900-176148-1): ")
    print("Masked IMEI:", mask_imei(value))

    print("\n==== Running parse_parts_order ====")
    value = input("Enter parts and quantities as PART xQTY separated by ; (e.g. screen x1; battery x2): ")
    print("Parts order:", parse_parts_order(value))

    print("\n==== Running parse_model ====")
    value = input("Enter the phone brand and model (e.g. Samsung Galaxy S23): ")
    print("Brand and model:", parse_model(value))

if __name__ == "__main__":
    main()
