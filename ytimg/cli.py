# -*- coding: utf-8 -*-

"""Console script for ytimg."""
import sys
import requests
import click

import ytimg.ytimg as ytimg

# TODO: Add destination option
@click.command()
@click.argument('url')
def main(url):
    """Console script for ytimg."""
    ytid = ytimg.youtube_id(url)
    img_url = "http://img.youtube.com/vi/{}/0.jpg".format(ytid)
    filename = "{}.jpg".format(ytid)
    response = requests.get(img_url)
    file = open(filename, "wb")
    file.write(response.content)
    file.close()

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
