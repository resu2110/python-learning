from sys import argv

arguments = argv[1:]
options = []
flags = []
positions = []

def print_help():
	print("%s help: "%argv[0])
	print("hihohe")
	exit(0)

def is_option(arg_value):
	if(arg_value[0] == '-'):
		return False
	return True

def is_flag(arg_value):
	if(arg_value[0] == '-'):
		return True
	return False

def is_positional(arg_value):
	if( not (is_option(arg_value)) and not(is_flag(arg_value))):
		return True
	return False

def die(message_to_reader):
	print("failed")
	print(message_to_reader)



print("script name: ",argv[0])

if( (arguments[0] == "-h") or (arguments[0] == "-help") ):
	print_help()


flag_count = 0
option_count = 0
position_count = 0

for i in range(0,len(arguments)):
	if (is_flag(arguments[i])):
		flags.append(arguments[i])
		flag_count += 1
		print("flag number ",flag_count)

	if (is_option(arguments[i])):
		options.append(arguments[i])		
		option_count += 1
		print("option number ",option_count)		
	
	if (is_positional(arguments[i])):
		positional_argument.append(arguments[i])
		position_count += 1
		print("position number ",position_count)
		

print("--options")
for i in range(0,len(options)):
	print(options[i])

print("--flags")
for i in range(0,len(flags)):
	print(flags[i])

print("--positions")
for i in range(0,len(positions)):
	print(positions[i])	

# for i in range(1:len(arguments)):
# 	if(arguments[i] == '-h' || arguments[i] == "-help"):
# 		print("bad syntax, you idiot")
# 	else:
# 		while(arguments_position)
