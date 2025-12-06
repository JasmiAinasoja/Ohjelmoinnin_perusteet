########################################################
# Task A9_T5
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################


def parse_byte(name: str, raw: str) -> int:
    """
    Validate that raw is a numeric integer string and within [0, 255].
    Returns the integer value or raises Exception with the exact messages required.
    """
    s = raw.strip()

    if not s.isdigit():
        raise Exception('"{}" is non-numeric value.'.format(raw))

    value = int(s)
    if not (0 <= value <= 255):
        raise Exception('Value "{}" is out of the range 0-255.'.format(raw))

    return value

def main():
    print("Program starting.")
    try:
        r_raw = input("Insert red: ")
        r = parse_byte("red", r_raw)

        g_raw = input("Insert green: ")
        g = parse_byte("green", g_raw)

        b_raw = input("Insert blue: ")
        b = parse_byte("blue", b_raw)

        print("RGB Details:")
        print("- Red {}".format(r))
        print("- Green {}".format(g))
        print("- Blue {}".format(b))
        hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
        print("- Hex {}".format(hex_code))
        print("- R-byte(base-2): {:08b}".format(r))
        print("- G-byte(base-2): {:08b}".format(g))
        print("- B-byte(base-2): {:08b}".format(b))

    except Exception as e:
        print(e)
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")

if __name__ == "__main__":
    main()
