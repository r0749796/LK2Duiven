
#####
# This is a custom 'getting started' script, made with care for r0738081@student.thomasmore.be.
# If you have any questions, please email us! support@initialstate.com
#####

# Import the ISStreamer module
from ISStreamer.Streamer import Streamer
# Import time for delays
import time

# Streamer constructor, this will create a bucket called Python Stream Example
# you'll be able to see this name in your list of logs on initialstate.com
# your access_key is a secret and is specific to you, don't share it!
streamer = Streamer(bucket_name="Sofie.py", bucket_key="Sofie", access_key="ist_kh_4Iv3IJuAd4mH82Km0H0yHD5CU9QJh")

# example data logging

for num in range(1, 20):
	time.sleep(0.1)
	if num%1 == 0:
		streamer.log("Number", "2")
	if num%2 == 0:
		streamer.log("Naam", "Sofie")
	if num%3 == 0:
		streamer.log("Energie", "40")
	if num%4 == 0:
		streamer.log("myNumber", "51.16257, 4.99084")
	


## This is just an example, try something of your own!
##   ideas:
##     - solve world hunger, one bug fix at a time
##     - create the worlds first widget
##     - build an army of bug-free robot kittens


# Once you're finished, close the stream to properly dispose
streamer.close()
