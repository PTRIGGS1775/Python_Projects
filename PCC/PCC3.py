'''Chapter 3 Materials
#Combining Lists with others
list1 = ['tasty treats', 'sour sweet', 'melancholy meat']
print(list1[2].title())
message = f'Alton Brown does a great special on {list1[0].title()} and does a christmas special on {list1[-1].upper()}!'
print(message)

#Modifying values the easy way. This lets me replace positional information.
magical_cards = ['birds of paradis', 'black lotus', 'teferi']
print(magical_cards)
magical_cards[0] = 'bolt'
print(magical_cards)
magical_cards.append('elspeth conquers death')
print(magical_cards)
magical_cards.insert(1, 'Plains')
print(magical_cards)'''
'''
#Starting with an empty list
opening_hand = []
opening_hand.append('Plains')
opening_hand.append('Plains')
#print(opening_hand)
opening_hand.insert(1, 'elspeth')
#print(opening_hand)
opening_hand.insert(0, 'teferi')
opening_hand.insert(-2, 'Island')
opening_hand.insert(-2, 'Negate')
opening_hand.insert(-2, 'Neutralize')
#print(opening_hand)

#Deleting things
battlefield = ['birds of paradise', 'mountain', 'forrest']
print(battlefield)
battlefield.append('bolt')
print(battlefield)
del battlefield[0]
print(battlefield)

print(opening_hand)
mulligan = opening_hand.pop()
print(f'You put {mulligan} to the bottom of the library and now your opening hand is \n{opening_hand}')
mulligan2 = opening_hand.pop(0)
print(f'You were mana screwed and put {mulligan2} to the bottom and now your opening hand is \n{opening_hand}')
opening_hand.append('Plains')
print(opening_hand)
opening_hand.remove('Plains')
print(opening_hand)
'''

hand = ['Plains', 'Plains', 'Shatter the sky', 'Yorion', 'ECD', 'Absolve']
print(hand)
rhand = hand.reverse()
print(rhand)
shand = hand.sort()
print(shand)
rshand = hand.sort(reverse == True)
print(rshand)
