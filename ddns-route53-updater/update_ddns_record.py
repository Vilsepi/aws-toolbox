#!/usr/bin/env python

from boto.route53.connection import Route53Connection
import requests
import sys

import config_secrets

"""
Based on https://gist.github.com/willtrking/736875ad128a6d9b10dd
"""

my_public_ip = requests.get("http://httpbin.org/ip").json()['origin']
conn = Route53Connection(aws_access_key_id=config_secrets.AWS_ACCESS_KEY,
                         aws_secret_access_key=config_secrets.AWS_SECRET_KEY)
records = conn.get_all_rrsets(config_secrets.ZONE_ID, 'A', config_secrets.DOMAIN_NAME, maxitems=1)
record = records[0]

print "records"
print records

sys.exit(0) if record.name != config_secrets.DOMAIN_NAME

ip_in_record = record.resource_records[0]
sys.exit(0) if my_public_ip == ip_in_record

hosted_zone = conn.get_hosted_zone(config_secrets.ZONE_ID)

print "hosted_zone"
print hosted_zone

zone = conn.get_zone(hosted_zone['GetHostedZoneResponse']['HostedZone']['Name'])

print "zone"
print zone

#zone.update_a(name=config_secrets.DOMAIN_NAME,
#              value=my_public_ip,
#              ttl=record.ttl,
#              identifier=record.identifier)
