
labelsV = {
	'success': {
		'success': 'success',
		'succesful_registration': 'Your account has been created! You are now able to log in',
	},
	'error': {
		'error': 'error',
		'command_error': 'Command not found',
		'unsuccessful_login': 'You can´t access with those credentials',
	}
}

def labels(path):
	label = labelsV.copy()
	for i in path.split('.'):
		label = label.get(i, {})
	return str(label)