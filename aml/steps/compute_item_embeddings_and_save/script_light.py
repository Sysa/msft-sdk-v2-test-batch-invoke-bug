import argparse
import sys

sys.path.insert(0, ".")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hello")
    args, _ = parser.parse_known_args()

    print(args.hello)
