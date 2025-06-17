
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="ReliLab Test Runner CLI")
    parser.add_argument('--test', type=str, default="recovery", help="Test to run (default: recovery)")
    return parser.parse_args()
