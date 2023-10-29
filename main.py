# ConnectionSpeedChecker program.
# Description: This program is intended to be used to periodically test an internet connection to determine any issues low speed events.
# Author: Julian Rich
# Licence: MIT
import logging
import time
import datetime
from SpeedChecker import SpeedChecker

def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p %z', filename='speedchecker.log', level=logging.INFO)
    logging.info("speedtest log started.")
    speed_checker = SpeedChecker()
    counter = 0
    # do a speed test.
    while counter < 1:
        print(f'speedtest started.')
        download_speed = round(speed_checker.do_speed_test("download"),1)
        print(f"{datetime.datetime.now().isoformat()} - download speed = {download_speed} mbps.")
        if download_speed < 5.0 and download_speed > 0.1:
            logging.warning(f"download speed low - download speed = {download_speed} mbps.")
        elif download_speed > 5.0:
            logging.info(f"download speed normal - download speed = {download_speed} mbps.")
        else:
            logging.warning(f'very low download speed - download speed = {download_speed} mbps.')
        # wait one minute then do another speed test.
        print('waiting for one minute...')
        time.sleep(60)
    logging.info("speedtest log finished.")

if __name__ == "__main__":
    main()
