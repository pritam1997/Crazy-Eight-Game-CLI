import random
import sys
sys.path.append(r"C:\Users\Pritam\Desktop\Card games\card.py")
from card import *

class Dealer_card:

	temp_deck = deck.copy()

	def __init__(self, player1 = 0, player2 = 0, dealer=0):
		self.player1 = player1
		self.player2 = player2
		self.dealer = dealer

	def shuffle_card(self):
		random.shuffle(Dealer_card.temp_deck)

	def display_player1(self, list_pass):
		self.player1 = list_pass
		print(("\n"+"-"*50+"No Cheating"+"-"*50)*100)
		print("\n"*10)
		print("$"*50+" Player 1 "+"$"*50)
		print("\n"*10)
		self.player1 = set(self.player1)
		self.player1 = list(self.player1)
		self.player1.sort()
		print()
		print("-"*110)
		print("\nPlayer1 : ",self.player1)
		print("-"*110)
		# print("\n",len(self.player1),"card")
		print()
		print("-"*20)
		print("\nDealer : ",self.dealer)
		print("-"*20)
		print("\n"*10)
		return self.player1


	def display_player2(self, list_pass):
		self.player2 = list_pass
		print(("\n"+"-"*50+"No Cheating"+"-"*50)*100)
		print("\n"*10)
		print("$"*50+" Player 2 "+"$"*50)
		print("\n"*10)
		self.player2 = set(self.player2)
		self.player2 = list(self.player2)
		self.player2.sort()
		
		print()
		print("-"*110)
		print("\nPlayer2 : ",self.player2)
		print("-"*110)
		# print("\n",len(self.player2),"card")
		print()
		print("-"*20)
		print("\nDealer : ",self.dealer)
		print("-"*20)
		print("\n"*10)
		return self.player2

	def distribute(self):
		self.player1 = random.sample(Dealer_card.temp_deck, k=8)
		
		for i in range(len(self.player1)):
			Dealer_card.temp_deck.remove(self.player1[i])
		
		self.player2 = random.sample(Dealer_card.temp_deck, k=8)
		for i in range(len(self.player2)):
			Dealer_card.temp_deck.remove(self.player2[i])

		self.dealer = random.choice(Dealer_card.temp_deck)
		Dealer_card.temp_deck.remove(self.dealer)
		print(len(Dealer_card.temp_deck))


class Players(Dealer_card):		

	
	player_chance=1

	def __init__(self):
		super().__init__()



	def play(self):
		if len(self.player1) ==0:
			Players.winner(self)
		elif len(self.player2) == 0:
			Players.winner(self)

		if Players.player_chance % 2 == 0:
			Players.play_player2(self)
		else:
			Players.play_player1(self)


	def play_player1(self):
		global picked_count
		picked_count = 0
		i = Dealer_card.display_player1(self, self.player1)
		Players.player_single_card(self, i)
		

	def play_player2(self):
		global picked_count
		picked_count = 0
		j = Dealer_card.display_player2(self, self.player2)
		Players.player_single_card(self, j)

	def player_single_card(self,for_player):		# arg i.e player 1 or player 2
		
		c = Players.checking_card_with_deal(self,for_player)	

		if c < 1:
			n = Players.check_card_with8(self, for_player)

			if n > 0:
				Players.choose_8(self,for_player)
			else:
				Players.draw_card(self,for_player)
		else:
			Players.card_choose(self, for_player)


	def checking_card_with_deal(self, which_player):
		d_single = self.dealer.split()
		global count
		count=0
		for i in range(len(which_player)):
			single_card = which_player[i].split()
			if d_single.count(single_card[0]) >0 or d_single.count(single_card[1]) > 0:
				count += 1
		return count


	def draw_card(self,playerno):		# arg i.e player 1 or player 2
		# global picked_count

		if len(Dealer_card.temp_deck) == 1:
			Dealer_card.temp_deck = deck.copy()

		i=0
		while i<1:
			ch = input("\nYou must draw (y): ")
			if ch.lower() == 'y':
				global picked_count
				picked_count += 1

				mno = 0
				while mno <1:
					# print(len(Dealer_card.temp_deck))
					pick = random.choice(Dealer_card.temp_deck)
					if playerno.count(pick) <1 and self.player1.count(pick) <1 and self.player2.count(pick) <1:
						Dealer_card.temp_deck.remove(pick)
						mno += 1

			playerno.append(pick)
			# s1 = set(playerno)
			playerno = list(playerno)
			playerno.sort()
			
			print("\nYour card :",playerno)
				
			if picked_count > 3:
				print("\n                         "+"!"*60+".............. Pass ..............."+"!"*60)
				Players.player_chance += 1
				Players.play(self)
				i += 1

			Players.player_single_card(self,playerno)


	def card_choose(self, player_card):
		
		a=0
		while a<1:
			s = 0

			while True:
				choose_card = input("\nChoose card (SUIT_NAME RANK): ").split(",")
				if ' ' in choose_card[0]:
					break				
			
			for c in range(len(choose_card)):
				single_suit_of_ch = choose_card[0]
				if player_card.count(single_suit_of_ch):				
					if single_suit_of_ch.count('8'):
						Players.choose_8(self, player_card)
				
				for d in range(len(player_card)):
					single_suit = player_card[d].split()
					if single_suit_of_ch.count(single_suit[0]) > 0 and single_suit_of_ch.count(single_suit[1])>0:
						s += 1

			if s == len(choose_card):
				Players.check_deal_with_choosed_card(self,choose_card)
				if z > 0:
					a += 1
			
		if a > 0:
			for i in range(len(choose_card)):
				self.dealer = choose_card[i]
				player_card.remove(choose_card[i])
				l = 0
				l2 = 0
				for m in range(len(player_card)):
					if self.player1.count(player_card[m]) >0:
						l += 1
					elif self.player2.count(player_card[m]) >0:
						l2 += 1
				
				if l == len(player_card):
					self.player1 = player_card
				elif l2 == len(player_card):
					self.player2 = player_card
				

				Players.player_chance += 1
				Players.play(self)
# player 2		

	def check_deal_with_choosed_card(self,ch_card):
		global z
		z=0
		single_suit = self.dealer.split()
		for i in range(len(ch_card)):
			if ch_card[i].count(single_suit[0]) > 0 or ch_card[i].count(single_suit[1])>0:
				z+=1
		return z

	def check_card_with8(self, card):
		x=0
		for i in range(len(card)):
			card_list = card[i].split()
			if card_list.count('8') > 0:
				x += 1
		return x


	def choose_8(self,player_card):
		i=0
		while i<1:
			while True:
				ch = input("\n!!!...You have to choose 8th rank card :")
				if ' ' in ch :
					break		
			
			n=0
			for x in range(len(player_card)):
				
				if player_card[x].count(ch) >0 and ch.count('8')>0:
					j=0
					while j<1:
						change = input("\nYou must change suit now [Enter suit name]:")
						if change.count('spade')==1 or change.count('club')==1 or change.count('heart')==1 or change.count('diamond')==1:
							player_card.remove(ch)
							print(player_card)
							s = change+' '+'8' 
							self.dealer = s
							j += 1
					n+=1
					break
			if n > 0:
				Players.player_chance += 1

				Players.play(self)
				i += 1
		# end loop

	def winner(self):
		if len(self.player1) ==0:
			print("\n!!!.....Congratulations Player 1 Win........!!!!!!!!!")
			exit()
		elif len(self.player2) == 0:
			print("\n!!!.....Congratulations Player 2 Win........!!!!!!!!!")
			exit()

o1 = Players()
o1.shuffle_card()
o1.distribute()
o1.play()
