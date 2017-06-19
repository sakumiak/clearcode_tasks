#Python intern task - task2 


#Function damage
#		Inputs spell: str
#		Outputs: dmg: int
#		This function check if spell is spell and counting damage points.
def damage (spell):
	dmg = 0
	subspells_dict = {'fe': 1, 'je': 2, 'jee': 3, 'ain': 3, 'dai': 5, 'ne': 2, 'ai': 2}
	subspells_list = ['fe','jee','je','ain','dai','ne','ai']	

	if not(type(spell) is str):
		return 'Pleas use str to cast your spell'
	if 'fe' in spell and 'ai' in spell and spell.count('fe') == 1 and spell.index('ai') > spell.index('fe'):
		spell = spell[spell.index('fe'):]
		dmg += subspells_dict['fe']
		spell = spell.replace('fe','')
		
		spell = spell[:spell.rfind('ai')]
		dmg += subspells_dict['ai']
		
		#In this loop function countin damage points and choose the one with the biggest damage.
		#Choose the biggest damage: 
		#		First function check str with length 3 cause 'jee' is more valuable than 'je'. The same thing is with 'ain' and 'ai'.
		#		'dai-n' is always more valueable than 'd-ain' and it is always checking first. Look at subspells_dict.
		#		If spell starts with 'ain' we check next character. If it's equal 'e' function use 'ai-ne' subspells cause it's more valuable than 'ain-e'
		#Damage counting:
		#		Function add to dmg variable value from subspells_dict if str[0:2] or str[0:3] is subspell else it add -1 to dmg variable
		while len(spell) > 0: 
			if spell[0:3] in subspells_list:
				if len(spell) > 3 and spell[0:3] == 'ain' and spell[3] == 'e':
					dmg += subspells_dict['ai'] + subspells_dict['ne']
					spell = spell[4:]
				else:
					dmg += subspells_dict[spell[0:3]]
					spell = spell[3:]
			elif spell[0:2] in subspells_list:
				dmg += subspells_dict[spell[0:2]]
				spell = spell[2:]
			else:
				dmg -= 1
				spell = spell[1:]
		
	if dmg < 0:
		dmg = 0				

	return dmg


if __name__ == '__main__':

	print(damage('jejejefedaiainanana'))
