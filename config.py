# Configuration File for the game
# You will have to provide your own images and sounds and then configure them below for the game to work
# I have used a simple random.choice method to randomly choose sounds, images for player and weights
# these random.choice methods take lists as arguments, and these lists contain the names of these files, and these names refer to the files in the local working directory
# Feel free to read the above para again, otherwise its pointless to try run this poorly commented pygame project
# The initial game characters were based on Robots, and a robot named Botley and a falling weight, so the name confusions might be apparent throughout the program's .py files
# Images used in the game
# Format is :
# image = image_name.image_type (preferably png)
# make sure the image size doesn't overshoot the pygame window size

#In order for the game to work you will have to provide 

#The following are Lists, which contain lists of images from which the game will choose for usage at runtime, for each level
# the player List contains a list of all player images
# the weightimages List contains a list of all weight images
p1 = "player.png"
w1 = "weight.png"
player = [p1]
weightimages = [w1]
# image to show when the game is paused
gamepaused = ""
# image to show when everything's ready
ready = ""
# sound to play when the game is over
cry = ""
# image to display on game startup, on the frame
startupimage = ""
# image to display on gameover
out = ""
# sound to play on collision between player and object
soundfile = ""

#the escapesounds list contains a list of sounds that play when the player evades a falling object
# add escape sounds by the following format:
# escapesound_name = escapesoundfilename.format
# then add them to the list below
escapesound1 = "escapesound.wav"
escapesounds = [escapesound1]
# the gameoversounds list contains a list of sounds that will be played when the game is over
# feel free to add sounds, then add the names of those sounds here, to get the game to choose one randomly
gameoversound1 = "gameoversound1.wav"
gameoversounds = [gameoversound1]
# Attributes
screen_size = 1000,800
background_colour = 255,255,255
margin = 30
full_screen = 1
font_size = 48

# the speed with which the objects drop
drop_speed = 3
# the speed with which the player moves
botley_speed = 7
# the speed increase per level
speed_increase = 1
# the number of weights per level 
weights_per_level = 5
# the padding for the player image
botley_pad_top = 40
botley_pad_side = 20
# the following are for pygame.mixer() for it to initialize
FREQ = 44100   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 30 # how often to check if playback has finished



