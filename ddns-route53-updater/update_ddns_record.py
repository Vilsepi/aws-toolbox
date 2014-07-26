#!/usr/bin/env python

from boto.route53.connection import Route53Connection
import requests
import sys
import config_secrets

my_public_ip = requests.get("http://httpbin.org/ip").json()['origin']
conn = Route53Connection(aws_access_key_id=config_secrets.aws_access_key_id,
                         aws_secret_access_key=config_secrets.aws_secret_access_key)

record = conn.get_all_rrsets(config_secrets.aws_route53_hosted_zone_id, 'A', config_secrets.domain_name, maxitems=1)[0]
assert record.name == config_secrets.domain_name

if my_public_ip == record.resource_records[0]: sys.exit(0)

zone = conn.get_zone(conn.get_hosted_zone(config_secrets.aws_route53_hosted_zone_id)['GetHostedZoneResponse']['HostedZone']['Name'])
zone.update_a(name=config_secrets.domain_name,
              value=my_public_ip,
              ttl=record.ttl,
              identifier=record.identifier)
