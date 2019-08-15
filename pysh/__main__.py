import sys
import argparse

from .code import interact

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', action='store_true',
                       help="don't print version and copyright messages")
    args = parser.parse_args()
    if args.q or sys.flags.quiet:
        banner = ''
    else:
        banner = None
    interact(banner)

if __name__ == '__main__':
    main()

