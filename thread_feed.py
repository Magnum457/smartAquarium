# import
from threading import Thread
import feed
import time

feed_thread = Thread(target = feed.loop_feed)
