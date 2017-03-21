import os
import platform
import sys
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument(
    '-p',
    help = 'path of partition to make iso backup',
    type = str,
    default = 'full'
)
args = parser.parse_args()

if platform.system() == 'Linux':
    try:
        backup_string = ('sudo dd if={0} status=progress '
                        '|gzip > {1}.img.gz').format(args.p, int(time.time()))
        os.system(backup_string)
    except ValueError:
        print('something went horribly wrong')
elif platform.system() == 'Windows':
    os.system('dir')
    print('Windows isn\'t supported yet')