'''
Author: Aidan Ouckama
 
    Takes in an input for username and stores music artist
    preferences in a text file database. This database is then
    referenced to find recommendations by pinpointing a user
    with the most similar artist preferences.
 
CS 115
'''
 
# user preference
username = ''
isPrivate = False
isRegistered = False
 
# user information
user_preferences = []
 
# options dictionary
options = {
    'e' : 'Enter preferences',
    'r' : 'Get recommendations',
    'p' : 'Show most popular artists',
    'h' : 'How popular is the most popular',
    'm' : 'Which use has the most likes',
    'q' : 'Save and quit',
}
 
# database information
database = ''
data = {} # stores most up to date user information
#
#   DATA FORMAT:
#
#   {
#       'username1': ['artist1', 'artist2', 'artist3'],
#       'username2': ['artist3', 'artist4', 'artist5'],
#   }
#

 
def __main__():
    '''
    First execution of the program. Takes in username input
    and references text database to check if user exists.
 
    INPUT  --   None
    OUTPUT --   None (Main Program)
    '''
 
    # create / reference database
    global database
    global data
 
    # if file exists ignore if not create file
    try: 
        open('musicrecplus.txt')
    except FileNotFoundError:
        database = open('musicrecplus.txt', 'w')
    database = open('musicrecplus.txt', 'r')
 
    # read data from database and append to dictionary data
    lines = database.readlines()
    for line in lines:
        [user, artistList] = line.split(':')
        artists = artistList.split(',')
 
        # clean data
        artists = list(map(lambda x: x.strip().title(), artists))
        artists = list(filter(None, artists))
        
        # write data to dictionary
        data[user] = artists
 
    # ask for username
    global username
    username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
 
    # check if user wants preferences private
    global isPrivate
    isPrivate = username[-1] == '$'
 
    # check if user is already registered
    global isRegistered
    isRegistered = username in data.keys()
 
    if not isRegistered:
 
        # add username to database and add user as registered
        data[username] = []
        isRegistered = True
        enterPreferences()
    else:
        # set user preferences
        global user_preferences
        user_preferences = data[username] 
 
        # directly give registered user menu
        optionsHandler()
 
def optionsHandler():
    '''
    Handles the options that are provided by the user
    (seen in global options variable). Takes input from
    the user as shown in options and runs the 
    corresponding function associated to the option.
 
    INPUT  --   User Input (Keyboard)
    OUTPUT --   None (designated function run)
    '''
 
    # print menu
    print('Enter a letter to choose an option:')
    for option in options.keys():
        print(option, '-', options[option])
    response = input()
 
    # check if response is within options dictionary
    if response in options.keys():
 
        # enter preferences
        if response == 'e':
            enterPreferences()
        
        # get recommendations
        if response == 'r':
            getRecommendations()
 
        # show most popular artists
        if response == 'p':
            pass # TODO
 
        # how popular is most popular
        if response == 'h':
            howPopular()
 
        # which user has the most likes
        if response == 'm':
            mostPopular()
            
        # save and quit
        if response == 'q':
            writeToDatabase()
            pass # TODO
 
    # invalid input
    else:
        print('\n Invalid input! \n')
        optionsHandler()
 
def enterPreferences():
    '''
    Asks the user through print statements to enter artists
    they enjoy. The input is then added to a user_preferences
    list. Loop continues until blank Enter is inputted.
 
    INPUT  --   User Input (Keyboard)
    OUTPUT --   None (appended artists to user_preferences)
    '''
 
    # initialize user preferences
    user_preferences = []
    response = ' '
 
    # ask for artists until a blank response is given
    while response != '':
        response = input('Enter an artist that you like (Enter to finish):\n')
        if response == '':
            data[username] = user_preferences # add artists to current data dictionary
            optionsHandler() # once artists are inputted open option menu
        else:
            user_preferences.append(response.strip().title()) # clean data and add to user_preferences
 
def getRecommendations():
    '''
    Finds a similarity score for all users compared to the
    current user. Uses these scores to make recommendations
    for the current user.
 
    INPUT  --   None (data in data dictionary)
    OUTPUT --   None (print of recommended artists)
    '''
 
    similarity = {}
 
    # get every username in current data
    for user in data.keys():
        name = user
        artists = data[user]
 
        # dont compare user to itself
        if not name == username:
            count = 0
 
            # loop through each artist and count how many similarities there are
            for artist in artists:
                if artist in user_preferences:
                    count += 1
 
            # make sure users have something in common and dont have exact same artists and users are not private
            if not count == 0 and not count == len(artists) and not name[-1] == '$':
                similarity[name] = count
    
    # print recommended artists based on a recommended user
    if not max(similarity.values()) == 0:
        recUser = max(similarity) # recommended user
        recArtists = data[recUser]
        for artist in recArtists:
            count = 0
 
            # only print 3 recommendations and artists not in current users preferences 
            if not artist in user_preferences and count < 3:
                print(artist)
                count += 1
    
    # loop back to options
    optionsHandler()
 
def writeToDatabase():
    '''
    Takes the information in dictionary data and
    writes it in recommended format to
    musicrecplus.txt
 
    INPUT  --   None (data in data dictionary)
    OUTPUT --   None (data writted to musicrecplus.txt)
    '''
 
    database = open('musicrecplus.txt', 'w') # no need to check for avaliability because at this point file was created
    
    # check every user in current data
    for user in data.keys():
 
        # write username
        database.write(user + ':')
 
        # write artists following username
        i = 0
        for artist in data[user]:
            database.write(artist + ',' if i < len(data[user]) - 1 else artist + '\n') # dont print a comma if at last artist
            i += 1

def mostPopular():
    popular={}
    if artist ==[]:
        print("No artist found")
    else:
        for user in data:
            if not isPrivate:
                for artist in data[user]:
                    if artist in popular:
                        popular[artist]+=1
                    else:   
                        popular[artist]=1
                    
        x=sorted(popular)
        i=0                
        if len(x)<3:
            print (x)
        else:
            while i<=2:
                print (x[i])
                i+=1

def howPopular():
    popular={}
    if artist==[]:
        print("Sorry, no artists found")
    else:
        for user in data:
            if not isPrivate:
                for artist in data[user]:
                    if artist in popular:
                        popular[artist]+=1
                    else:
                        popular[artist]=1
                    
        print(max(popular.values()))
        
        
 
__main__()

