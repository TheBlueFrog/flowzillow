
from flowzillow.client import ZillowClient
import re

client = ZillowClient("X1-ZWz19v0zahxc7f_4eq90")

with open("addresses.txt") as addresses:
    for address in addresses:
        a = address.rstrip()
        if a != '':
            a = address.split('|')
            xml_response = client.get_search_results(a[0].strip(), a[1].strip())
            b = re.sub(r'.*<zestimate>', "", xml_response)
            b = re.sub(r'</zestimate>.*', "", b)

            b = re.sub(r' currency="USD"', "", b)
            b = re.sub(r'<last-updated>.*</last-updated>', "", b)
            b = re.sub(r'<oneWeekChange.*</oneWeekChange>', "", b)
            b = re.sub(r'<valueChange.*</valueChange>', "", b)
            b = re.sub(r'<percentile.*</percentile>', "", b)

            b = re.sub(r'<valuationRange>', "", b)
            b = re.sub(r'</valuationRange>', "", b)

            b = re.sub(r'<amount>', "", b)
            b = re.sub(r'</amount>', ",", b)

            b = re.sub(r'<low>', "", b)
            b = re.sub(r'</low>', ",", b)

            b = re.sub(r'<high>', "", b)
            b = re.sub(r'</high>', ",", b)
            print b, a[0].strip(), ', ', a[1].strip()

addresses.close()
