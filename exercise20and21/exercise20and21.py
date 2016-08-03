#!/usr/bin/env python

import re

class VersionParser():
    def __init__(self, filename):
        self.show_vers = self.get_show_vers(filename)
        self.serial = self.get_serial_num()
        self.vendor = self.get_vendor()
        self.model = self.get_model()
        self.os_vers = self.get_os_vers()
        self.uptime = self.get_uptime()

    def get_show_vers(self, filename):
        with open(filename) as data:
            return data.read()
    
    def get_serial_num(self):
        matches = re.search(r'Processor board ID (\w+)', self.show_vers)
        return matches.group(1)
    
    def get_vendor(self):
        matches = re.search(r'Copyright.+by (.+)', self.show_vers)
        return matches.group(1)
    
    def get_model(self):
        matches = re.search(r'\*0 +(\S+)', self.show_vers)
        return matches.group(1)
    
    def get_os_vers(self):
        matches = re.search(r'Version ([^,]+), RELEASE SOFTWARE', self.show_vers)
        return matches.group(1)
    
    def get_uptime(self):
        matches = re.search(r'uptime is (.+)', self.show_vers)
        return matches.group(1)

    def get_facts(self):
        facts_dict = {
            'Serial Number': self.serial,
            'Vendor': self.vendor,
            'Model': self.model,
            'OS Version': self.os_vers,
            'Uptime': self.uptime
        }
        return facts_dict


filename = 'data_show_version.txt'

parser = VersionParser(filename)
output_dict = parser.get_facts()

for key, value in output_dict.items():
    print '{:<14}: {}'.format(key, value)

