
from flowzillow.client import ZillowClient
import re
import datetime

client = ZillowClient("X1-ZWz19v0zahxc7f_4eq90")

now = datetime.date.today().strftime("%m/%d/%Y,")
price = 0.0
count = 0

with open("addresses.txt") as addresses:
    for address in addresses:
        a = address.rstrip()
        if a != '':
            if a[0] != '#' :
                if a.startswith('!average') :
                    print now, (price / count), ',', re.sub(r'!average', "", a)
                    price = 0.0
                    count = 0
                else :
                    a = a.split('|')
                    xml_response = client.get_search_results(a[0].strip(), a[1].strip())
                    err = re.match('.*Error: no exact match', xml_response)

                    if err :
                        print 'Error: bad address', a[0], a[1]
                    else :
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
                        b = re.sub(r'</high>', "", b)

                        # b should now have just csv of zestimate prices

                        # this from SO using comprehensions, don't quite follow
                        # (p, l, h) = [t(s) for t, s in zip((float, float, float), b.split(','))]

                        (p, l, h) = b.split(',')
                        price += float(p)

                        count += 1

                        print now, b, ', ', a[0].strip(), ', ', a[1].strip()


addresses.close()
