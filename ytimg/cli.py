# -*- coding: utf-8 -*-

"""Console script for ytimg."""
import sys
import requests
import click

import ytimg.ytimg as ytimg

# TODO: Add destination option
@click.command()
@click.option('--which',default='0',help='Which thumbnail to retrieve')
@click.argument('url')
def main(url, which):
    """Console script for ytimg."""
    ytid = ytimg.youtube_id(url)
    img_url = "http://img.youtube.com/vi/{}/{}.jpg".format(ytid,which)
    filename = "{}_{}.jpg".format(ytid,which)
    response = requests.get(img_url)
    file = open(filename, "wb")
    file.write(response.content)
    file.close()

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
