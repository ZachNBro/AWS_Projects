"""
    File name: animal_quiz.py
    Author: Zachary Brown
    
    ***USERS GUIDE***
    
    Choose one of the menu options listed. Once you
    have chosen a quiz, open the downloaded jpg files
    to view the assoiated animal. Guess the animal's name
    correctly to receive one point. At the end, your points
    will be tallied and stored in a leaderboard. 
    
    You may check the leaderboard at any time. The leaderboard
    will display the top scorers who have gotten all questions
    correct followed by all others. Try to get the highest score 
    and prove your animal identification knowledge! The concept 
    of this application was developed based on the numerous quizes 
    available online that utilize visuals with questions.
    
"""

import boto3
import sys
import datetime

# create an S3 client
s3 = boto3.client('s3')

# create dynamo resource
dynamodb = boto3.resource('dynamodb')

# main menu
def menu():
    print("***Welcome to the animal quiz!***: \n" \
    "1. Spider Quiz >> \n" \
    "2. Snake Quiz >> \n" \
    "3. Mammal Quiz >> \n" \
    "4. Spider Leaderboard >> \n" \
    "5. Snake Leaderboard >> \n" \
    "6. Mammal Leaderboard >> \n" \
    "7. Exit")
    
    selection = input()
    if selection == "1":
            spider_quiz()
    elif selection == "2":
            snake_quiz()  
    elif selection == "3":
            mammal_quiz()
    elif selection == "4":
            spider_leaderboard()
    elif selection =="5":
             snake_leaderboard()
    elif selection == "6":
             mammal_leaderboard()
    elif selection=="7":
        x = datetime.datetime.now()
        print(x)
        sys.exit()
    else:
        print("Please enter a valid selection" + "\n")
        menu()

def spider_quiz():
	
	# set point counter
	points = 0

	print("***Please open the image***")
	
	# download image file from associated bucket
	boto3.resource('s3').Bucket("quiz.spiders").download_file("tarantula.jpg", 'spider_one.jpg') 
	answer_one = input("Enter the name of spider one:")
	if answer_one.lower() == "tarantula":
		print("Correct!")
		# increment point counter if correct answer
		points = points + 1
	else:
		print("Incorrect!")
	
	boto3.resource('s3').Bucket("quiz.spiders").download_file("daddy_long_legs.jpg", 'spider_two.jpg')   
	answer_two = input("Enter the name of spider two:")
	if answer_two.lower() == "daddy long legs":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
		
	boto3.resource('s3').Bucket("quiz.spiders").download_file("wolf_spider.jpg", 'spider_three.jpg')  
	answer_three = input("Enter the name of spider three:")
	if answer_three.lower() == "wolf spider":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
	
	boto3.resource('s3').Bucket("quiz.spiders").download_file("huntsman_spider.jpg", 'spider_four.jpg')  
	answer_four = input("Enter the name of spider four:")
	if answer_four.lower() == "huntsman":
		print("Correct!")
		points = points + 1
	else:
	    print("Incorrect!")
	    
	boto3.resource('s3').Bucket("quiz.spiders").download_file("widow.jpg", 'spider_five.jpg')  
	answer_five = input("Enter the name of spider five:")
	if answer_five.lower() == "widow" or answer_five == "black widow":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
	
	# enter player name variable and add credentials to dynamodb table
	player_name = input("Enter your alias:")
	table = dynamodb.Table('SpidersLeaderboard')
	table.put_item(
			Item={
	         'PlayerName': player_name,
	         'Score': points    
	         }
	    	)
	menu()

def snake_quiz():
	
	points = 0
	
	print("***Please open the image***")

	boto3.resource('s3').Bucket("quiz.snakes").download_file("python.jpg", 'snake_one.jpg')   	
	answer_one = input("Enter the name of snake one:")
	if answer_one.lower() == "python":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
	
	boto3.resource('s3').Bucket("quiz.snakes").download_file("cobra.jpg", 'snake_two.jpg')
	answer_two = input("Enter the name of snake two:")
	if answer_two.lower() == "cobra":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
	
	boto3.resource('s3').Bucket("quiz.snakes").download_file("anaconda.jpg", 'snake_three.jpg')
	answer_three = input("Enter the name of snake three:")
	if answer_three.lower() == "anaconda":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
	
	boto3.resource('s3').Bucket("quiz.snakes").download_file("viper.jpg", 'snake_four.jpg')   
	answer_four = input("Enter the name of snake four:")
	if answer_four.lower() == "viper":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
	
	boto3.resource('s3').Bucket("quiz.snakes").download_file("boa.jpg", 'snake_five.jpg')   
	answer_five = input("Enter the name of snake five:")
	if answer_five.lower() == "boa" or answer_five == "boa constrictor":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
	
	player_name = input("Enter your alias:")
	table = dynamodb.Table('SnakesLeaderboard')
	table.put_item(
		Item={
	         'PlayerName': player_name,
	         'Score': points    
	         }
	    	)
	menu()

def mammal_quiz():
	
	points = 0
	
	print("***Please open the image***")

	boto3.resource('s3').Bucket("quiz.mammals").download_file("elephant.jpg", 'mammal_one.jpg')   
	answer_one = input("Enter the name of mammal one:")
	if answer_one.lower() == "elephant":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
	
	boto3.resource('s3').Bucket("quiz.mammals").download_file("tiger.jpg", 'mammal_two.jpg')   
	answer_two = input("Enter the name of mammal two:")
	if answer_two.lower() == "tiger":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
	
	boto3.resource('s3').Bucket("quiz.mammals").download_file("wolf.jpg", 'mammal_three.jpg')   	
	answer_three = input("Enter the name of mammal three:")
	if answer_three.lower() == "wolf":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
	
	boto3.resource('s3').Bucket("quiz.mammals").download_file("wombat.jpg", 'mammal_four.jpg')   
	answer_four = input("Enter the name of mammal four:")
	if answer_four.lower() == "wombat":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
	
	boto3.resource('s3').Bucket("quiz.mammals").download_file("opossum.jpg", 'mammal_five.jpg')   
	answer_five = input("Enter the name of mammal five:")
	if answer_five.lower() == "opossum":
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect!")
		
	player_name = input("Enter your alias:")
	table = dynamodb.Table('MammalsLeaderboard')
	table.put_item(
		Item={
	         'PlayerName': player_name,
	         'Score': points    
	         }
	    	)
	menu()

def spider_leaderboard():

	table = dynamodb.Table('SpidersLeaderboard')
	
	# use scan function to pull items and display player names and scores
	response = table.scan()
	data = response['Items']
	print("***Our top scorers are:*** " + '\n')
	for i in response['Items']:
		# display top scorers with 5 points
		if i['Score'] == 5:
			print("**%s** with **%i** points" % (i['PlayerName'], i['Score']) + '\n')
	# display rest of players
	for i in response['Items']:
			print("The score of player %s is %i" % (i['PlayerName'], i['Score']) + '\n')
	menu()
	
def snake_leaderboard():
	
	table = dynamodb.Table('SnakesLeaderboard')

	response = table.scan()
	data = response['Items']
	print("***Our top scorers are:*** " + '\n')
	for i in response['Items']:
		if i['Score'] == 5:
			print("**%s** with **%i** points" % (i['PlayerName'], i['Score']) + '\n')
	for i in response['Items']:
			print("The score of player %s is %i" % (i['PlayerName'], i['Score']) + '\n')
	menu()
    
def mammal_leaderboard():
	
	table = dynamodb.Table('MammalsLeaderboard')

	response = table.scan()
	data = response['Items']
	print("***Our top scorers are:*** " + '\n')
	for i in response['Items']:
		if i['Score'] == 5:
			print("**%s** with **%i** points" % (i['PlayerName'], i['Score']) + '\n')
	for i in response['Items']:
			print("The score of player %s is %i" % (i['PlayerName'], i['Score']) + '\n')
	menu()
    
menu()
