import argparse
import nmap3

parser = argparse.ArgumentParser()
parser.add_argument('--url')
url = parser.parse_args().url

results = nmap3.Nmap().scan_top_ports(url)

print(f'Top Ports Scan \n {results}')