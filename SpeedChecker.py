import speedtest as sp
import logging
import datetime as dt

class SpeedChecker:
    '''Class used to perform speed tests.'''

    def do_speed_test(self, test_type:str)-> float:
        '''Takes a "download" or "upload" string and returns the result of the chosen test.'''
        speed = 0.0
        speedtest = sp.Speedtest()
        speedtest.get_best_server()
        if test_type == "download":
            logging.info("download speed test started.")
            speed = speedtest.download()/1000000
        elif test_type == "upload":
            logging.info("upload speed test started.")
            speed = speedtest.upload()/1000000
        else:
            speed = None
        return speed
    




