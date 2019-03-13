"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?
NOTE: suitable for optional matches
"""

def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """

	if pos<0 or pos>=len(text): return None

	c = text[pos]


	return c	# anything else



def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""

	# initial state
	pos = 0
	state = 'q0'
	# memory for last seen accepting states
	last_token = None
	last_pos = None


	while True:

		c = getchar(text,pos)	# get next char (category)

		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char

			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos

		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos

			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos

# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων
transitions = { 'q0': { '0':'q1', '1':'q1', '2':'q1', '3':'q2'},
       			'q1': { '0':'q3' , '1':'q3' , '2':'q3' , '3':'q3' , '4':'q3' ,'5':'q3' , '6':'q3' , '7':'q3' , '8':'q3' , '9':'q3' },
       			'q2': { '0':'q3' , '1':'q3' , '2':'q3' , '3':'q3' , '4':'q3' ,'5':'q3' },
       			'q3': { '0':'q4' },
                'q4': { '0':'q5','1':'q5','2':'q5','3':'q5','4':'q5','5':'q5','6':'q5','7':'q5','8':'q5','9':'q5'},
                'q5': { '0':'q6','1':'q6','2':'q6','3':'q6','4':'q6','5':'q6','6':'q6','7':'q6','8':'q6','9':'q6' },
       			'q6': { 'K':'q7' , 'M':'q8' , 'G':'q11' },
       			'q7': { 'T':'q10'},
       			'q8': { 'P':'q9',},
       			'q9': { 'S':'q10'},
       			#s10 WIND_TOKEN
       			'q11': {'0':'q12','1':'q12','2':'q12','3':'q12','4':'q12','5':'q12','6':'q12','7':'q12','8':'q12','9':'q12'},
       			'q12': {'0':'q13','1':'q13','2':'q13','3':'q13','4':'q13','5':'q13','6':'q13','7':'q13','8':'q13','9':'q13'},
       			'q13': { 'M':'q8','K':'q7'}
     		  }

# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = { 'q10':'WIND_TOKEN',# s1 off !!!!!!!!!!!!!!!!
     	  }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('unrecognized input at position',pos,'of',text)
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
