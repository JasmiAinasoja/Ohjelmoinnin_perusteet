import random      # Tuodaan random-kirjasto satunnaislukujen generointiin
random.seed(1234)       # Asetetaan satunnaislukugeneraattorin siemen toistettavuuden varmistamiseksi

ascii_art = {       # Dictionary ASCII-taiteelle (kivi, paperi, sakset)
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""" 
}

def options():      # Tulostaa pelivalinnat käyttäjälle
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")

def main():     # Pääohjelma: kivi-paperi-sakset-pelin logiikka
    player_wins = 0     # Pelaajan voittojen laskuri
    player_losses = 0       # Pelaajan häviöiden laskuri
    player_draws = 0        # Pelaajan tasapelien laskuri
    bot_wins = 0        # Botin voittojen laskuri
    bot_losses = 0      # Botin häviöiden laskuri
    bot_draws = 0       # Botin tasapelien laskuri
    
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")     # Pyydetään pelaajan nimi
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")

    choices = {"1": "rock", "2": "paper", "3": "scissors"}     # Dictionary joka kääntää numerovalinnat merkkijonoiksi

    while True:     # Pääpeli-silmukka, jatkuu kunnes pelaaja valitsee "0"
        options()       # Näytetään valintavalikko

        choice = input("Your choice: ").strip()     # Pyydetään pelaajan valinta ja poistetaan tyhjät välilyönnit

        if choice == "0":       # Jos pelaaja valitsee "0"
            break       # Lopetetaan peli

        elif choice not in choices:     # Jos valinta ei ole kelvollinen (ei "1", "2" tai "3")
            print("Invalid choice! Please choose 1, 2, 3, or 0.\n")
            continue        # Pyydetään uusi valinta

        player_choice = choices[choice]     # Haetaan pelaajan valinta merkkijonona
        bot_choice_num = random.randint(1,3)        # Arvotaan botille satunnainen numero 1-3
        bot_choice = choices[str(bot_choice_num)]       # Muunnetaan botin valinta merkkijonoksi

        print("\nRock! Paper! Scissors! Shoot!\n")
        print("#"*25)       # Tulostaa visuaalinen erotin
        print(f"{player_name} chose {player_choice}.\n{ascii_art[player_choice]}")     # Näytetään pelaajan valinta ASCII-taidella
        print("#"*25)
        print(f"RPS-3PO chose {bot_choice}.\n{ascii_art[bot_choice]}")     # Näytetään botin valinta ASCII-taidella
        print("#"*25)

        if player_choice == bot_choice:        # Jos molemmat valitsivat saman
            print(f"Draw! Both players chose {player_choice}.\n")
            player_draws += 1       # Kasvatetaan pelaajan tasapelilaskuria
            bot_draws += 1      # Kasvatetaan botin tasapelilaskuria

        # Pelaaja voittaa: kivi voittaa sakset, paperi voittaa kiven, sakset voittaa paperin
        elif (player_choice == "rock" and bot_choice == "scissors") \
            or (player_choice == "paper" and bot_choice == "rock") \
            or (player_choice == "scissors" and bot_choice == "paper"):
            print(f"{player_name} {player_choice} beats RPS-3PO {bot_choice}.\n")
            player_wins += 1        # Kasvatetaan pelaajan voittolaskuria
            bot_losses += 1     # Kasvatetaan botin häviölaskuria
        else:       # Kaikki muut tapaukset: botti voittaa
            print(f"RPS-3PO {bot_choice} beats {player_name} {player_choice}.\n")
            bot_wins += 1       # Kasvatetaan botin voittolaskuria
            player_losses += 1      # Kasvatetaan pelaajan häviölaskuria

    print("\nResults:")      # Tulostetaan lopputulokset
    print(f"{player_name} - wins ({player_wins}), losses ({player_losses}), draws ({player_draws})")
    print(f"RPS-3PO - wins ({bot_wins}), losses ({bot_losses}), draws ({bot_draws})")
    print("\nProgram ending.")

if __name__ == "__main__":
    main()      # Käynnistetään ohjelma