#!/usr/bin/env python3

import sys
import json
import argparse

import singer
from singer import metadata

from tap_receptive.client import ReceptiveClient
from tap_receptive.discover import discover
from tap_receptive.sync import sync

LOGGER = singer.get_logger()

REQUIRED_CONFIG_KEYS = [
]

def do_discover(client):
    LOGGER.info('Testing authentication')
    try:
        client.request('GET', path='/accounts')
    except:
        raise Exception('Error could not authenticate with Receptive')

    LOGGER.info('Starting discover')
    catalog = discover()
    json.dump(catalog.to_dict(), sys.stdout, indent=2)
    LOGGER.info('Finished discover')

@singer.utils.handle_top_exception(LOGGER)
def main():
    parsed_args = singer.utils.parse_args(REQUIRED_CONFIG_KEYS)

    with ReceptiveClient(parsed_args.config) as client:
        if parsed_args.discover:
            do_discover(client)
        else:
            sync(client,
                 parsed_args.config,
                 parsed_args.catalog,
                 parsed_args.state)
