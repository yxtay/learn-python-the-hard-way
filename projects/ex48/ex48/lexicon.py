def scan(input):
    lexi = {
	    'north': 'direction',
		'south': 'direction',
		'east': 'direction',
		'west': 'direction',
		'down': 'direction',
		'up': 'direction',
		'left': 'direction',
		'right': 'direction',
		'back': 'direction',
		'go': 'verb',
		'stop': 'verb',
		'kill': 'verb',
		'eat': 'verb',
		'the': 'stop',
		'in': 'stop',
		'of': 'stop',
		'from': 'stop',
		'at': 'stop',
		'it': 'stop',
		'door': 'noun',
		'bear': 'noun',
		'princess': 'noun',
		'cabinet': 'noun'
	}
	
    words = input.split()
    
    output = []
    for word in words:
		num = convert_number(word)
		if num:
		    output.append(('number', num))
		else:
			try:
			    output.append((lexi[word], word))
			except KeyError:
			    output.append(('error', word))
		
    return output
	
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None