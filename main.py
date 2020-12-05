import argparse
import Picamera

def parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-ip", type = str, help="the ip form the PLC", default="192.168.1.10")
    parser.add_argument("--Password", type = str, help="password of the PLC", default="")
    parser.add_argument("--username", type=str, help="username for the PLC", default="admin")
    return parser.parse_args()

def main(arg):
    

if __name__ == '__main__':
    main(parser())