ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"     # Aakkosto jota Enigma-kone käyttää

def load_config(filename):     # Lataa roottori- ja reflektori-konfiguraatiot tiedostosta
    rotors = []     # Lista roottoreille (3 kpl)
    reflector = ""      # Reflektori-merkkijono
    try:        # Yritetään lukea konfiguraatiotiedosto
        with open(filename, "r") as f:      # Avataan tiedosto lukutilassa
            for line in f:      # Käydään läpi jokainen rivi
                line = line.strip()     # Poistetaan ylimääräiset välilyönnit
                if line.startswith("Rotor"):        # Jos rivi alkaa "Rotor"-sanalla
                    rotors.append(line.split(":")[1].strip())       # Erotetaan roottoridata ja lisätään listaan
                elif line.startswith("Reflector"):      # Jos rivi alkaa "Reflector"-sanalla
                    reflector = line.split(":")[1].strip()      # Erotetaan reflektoridata
    except FileNotFoundError:       # Jos tiedostoa ei löydy
        print(f"Config file '{filename}' not found. Using default rotors and reflector.")
        rotors = [      # Käytetään oletusroottoreita (historialliset Enigma I rotors)
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        ]
        reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"     # Käytetään oletusreflektoria (Enigma B)
    return rotors, reflector        # Palautetaan rotorit ja reflektori

# MIRA MUUTTI TÄMÄN KOODIN 
def rotate_rotors(positions):      # Pyörittää roottoreita yhden askeleen (kuten mekaaninen Enigma)
    positions[0] = (positions[0] + 1) % 26      # Pyöritetään ensimmäistä roottoria aina
    if positions[0] == 0:       # Jos ensimmäinen roottori teki täyden kierroksen (palasi 0:aan)
        positions[1] = (positions[1] + 1) % 26      # Pyöritetään toista roottoria
        if positions[1] == 0:       # Jos toinen roottori teki täyden kierroksen
            positions[2] = (positions[2] + 1) % 26      # Pyöritetään kolmatta roottoria
    return positions        # Palautetaan päivitetyt positiot

def encode_letter(letter, rotors, positions, reflector):        # Salaa yksittäisen kirjaimen Enigma-algoritmin mukaan
    index = ALPHABET.index(letter)      # Haetaan kirjaimen indeksi aakkostossa

    # Forward pass - signaali kulkee läpi kolmen roottorin
    for i in range(3):      # Käydään läpi kaikki kolme roottoria
        rotor = rotors[i]       # Haetaan nykyinen roottori
        pos = positions[i]      # Haetaan roottorin nykyinen positio
        shifted_letter = ALPHABET[(index + pos) % 26]       # Siirretään kirjainta roottorin position verran
        index = (rotor.index(shifted_letter) - pos + 26) % 26       # Haetaan uusi indeksi roottorin kytkeytymisestä

    # Reflector - signaali kimpoaa takaisin reflektorista
    index = ALPHABET.index(reflector[index])        # Reflektori vaihtaa kirjaimen toiseen

    # Reverse pass - signaali kulkee takaisin roottoreiden läpi käänteisessä järjestyksessä
    for i in reversed(range(3)):        # Käydään läpi rotorit käänteisessä järjestyksessä
        rotor = rotors[i]       # Haetaan nykyinen roottori
        pos = positions[i]      # Haetaan roottorin positio
        shifted_index = (index + pos) % 26      # Siirretään indeksiä position verran
        letter_at_pos = rotor[shifted_index]        # Haetaan kirjain roottorin kyseisestä kohdasta
        index = (ALPHABET.index(letter_at_pos) - pos + 26) % 26     # Palautetaan alkuperäiseen aakkostoon

    return ALPHABET[index]      # Palautetaan salattu kirjain

def encode_row(row, rotor_positions, rotors, reflector):        # Salaa kokonaisen rivin merkki kerrallaan
    converted_row = ""      # Salattu rivi (aluksi tyhjä)
    positions = rotor_positions.copy()      # Kopioidaan roottoreiden aloituspositiot (muutokset eivät vaikuta alkuperäiseen)

    for char in row.upper():        # Käydään läpi jokainen merkki (muutetaan isoiksi kirjaimiksi)
        if char not in ALPHABET:        # Jos merkki ei ole kirjain (esim. välilyönti, numero)
            converted_row += char       # Lisätään merkki sellaisenaan (ei salata)
            continue        # Siirrytään seuraavaan merkkiin

        # Step rotors BEFORE encoding - rootorit pyörivät ENNEN kuin kirjain salataan (kuten oikea Enigma)
        positions = rotate_rotors(positions)        # Pyöritetään roottoreita

        encoded_char = encode_letter(char, rotors, positions, reflector)        # Salataan kirjain
        converted_row += encoded_char       # Lisätään salattu kirjain tulokseen

    return converted_row # Tämä rivi on tärkeä! Palautetaan salattu rivi

def main():     # Pääohjelma: Enigma-koneen käyttöliittymä
    filename = input("Insert config(filename):").strip()        # Pyydetään konfiguraatiotiedoston nimi
    rotors, reflector = load_config(filename)       # Ladataan rotorit ja reflektori

    # Poistettu käännöt
    rotor_positions_init = [0, 0, 0]        # Roottoreiden alkupositiot (0=A, 1=B, 2=C, ...)

    plugs = input("Insert plugs (y/n)?: ").strip().lower()      # Kysytään plugboard-asetuksia
    if plugs == "y":        # Jos käyttäjä haluaa käyttää plugboardia
        print("No extra plugs implemented. Continuing without plugboard.")     # Plugboard ei ole toteutettu
    else:
        print("No extra plugs inserted.")
    print("Enigma initialized.\n")

    while True:     # Pääsilmukka: salataan rivejä kunnes käyttäjä syöttää tyhjän rivin
        row = input("Insert row (empty stops): ").upper()       # Pyydetään salattava rivi (muunnetaan isoiksi)
        if not row:     # Jos rivi on tyhjä
            print("\nEnigma closing.")
            break       # Lopetetaan ohjelma

        rotor_positions = rotor_positions_init.copy()       # Nollataan roottoreiden positiot joka riville

        print()
        converted = encode_row(row, rotor_positions, rotors, reflector)     # Salataan rivi
        for c_in, c_out in zip(row, converted):     # Käydään läpi jokainen merkki ja sen salattu vastine
            print(f'Character "{c_in}" illuminated as "{c_out}"')       # Tulostetaan merkki ja sen salattu muoto
        print(f'Converted row - "{converted}".\n')      # Tulostetaan koko salattu rivi

if __name__ == "__main__":
    main()      # Käynnistetään ohjelma