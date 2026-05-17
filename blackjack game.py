class game:
    def play(self):
        game_number = 0
        game_to_play = 0

    while games_to_play <= 0:
        try:
            
           games_to_play = int(input("How many games do you want to play? "))

        except:

            print("you must enter a number")

        while game_number < games_to_play:
            game_number += 1


            deck = deck()
            deck.shuffle()

            player_hand = hand()
            dealer_hand = hand(dealer = True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"game{game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value < 21 and choice not in ["s","stand"]:
                choice = input("please choose 'hit' or 'stand': ").lower()
                print()

            while choice not in ["h", "s", "hit", "stand"]:
                choice = input("please enter 'hit' or 'stand' (or h/s) ").loweer()
                print()
            if choice in ["hit", "h"]:
                player_hand.add_card(deck.deal())
                player_hand.display()
            
        if self.check_winner(player_hand, dealer_hand):
            continue
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards= True)

            if  self.check_winner(player_hand. dealer_hand):
                 continue

            print("final result")
            print("your hand:", player_hand_value)
            print("dealer's hand:", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)

        print ("\nthanks for playing")
        
        def check_winner(self,player_hand, dealer_hand, game_over=False):
          if not game_over:
            if player_hand.get_value() > 21:
                print("you busted.dealer wins")
                return True
            elif dealer_hand.get_value() > 21:
                print("dealer busted")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("both players have blackjack tie")
                return True
            elif player_hand.is_blackjack():
                print("both players have blackjack tie")
                return True
            elif dealer_hand.is_blackjack():
                print("dealer has blackjack.dealer wins")
                return True

          else:
              
            if player_hand.get_value() > dealer_hand.get_value():
                print("you win")
            elif player_hand.get_valu() == dealer_hand.get_value():
                print("tie")
            else:
                print("dealer win")
                return True
            return False

g = game()
g.play()
    
