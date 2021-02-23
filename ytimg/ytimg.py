# -*- coding: utf-8 -*-

"""Main module."""

from urllib.parse import urlsplit, parse_qs
from pathlib import PurePosixPath

def youtube_id(url):
    """Extract the YouTube ID from a YouTube URL

    >>> youtube_id("http://www.youtube.com/user/Scobleizer#p/u/1/1p3vcRhsYGo")
    '1p3vcRhsYGo'

    >>> youtube_id("http://www.youtube.com/watch?v=cKZDdG9FTKY&feature=channel")
    'cKZDdG9FTKY'

    >>> youtube_id('http://www.youtube.com/watch?v=yZ-K7nCVnBI&playnext_from=TL&videos=osPknwzXEas&feature=sub')
    'yZ-K7nCVnBI'

    >>> youtube_id('http://www.youtube.com/ytscreeningroom?v=NRHVzbJVx8I')
    'NRHVzbJVx8I'

    >>> youtube_id('http://www.youtube.com/user/SilkRoadTheatre#p/a/u/2/6dwqZw0j_jY')
    '6dwqZw0j_jY'

    >>> youtube_id('http://youtu.be/6dwqZw0j_jY')
    '6dwqZw0j_jY'

    >>> youtube_id('http://www.youtube.com/watch?v=6dwqZw0j_jY&feature=youtu.be')
    '6dwqZw0j_jY'

    >>> youtube_id('http://youtu.be/afa-5HQHiAs')
    'afa-5HQHiAs'

    >>> youtube_id('http://www.youtube.com/watch?v=cKZDdG9FTKY&feature=channel')
    'cKZDdG9FTKY'

    >>> youtube_id('http://www.youtube.com/user/Scobleizer#p/u/1/1p3vcRhsYGo?rel=0')
    '1p3vcRhsYGo'

    >>> youtube_id('//www.youtube-nocookie.com/embed/up_lNV-yoK4?rel=0')
    'up_lNV-yoK4'


    More from :url:`https://stackoverflow.com/a/27728417/297797`:

    ,
    'http://www.youtube.com/watch?v=yZ-K7nCVnBI&playnext_from=TL&videos=osPknwzXEas&feature=sub',
    'http://www.youtube.com/ytscreeningroom?v=NRHVzbJVx8I',
    'http://www.youtube.com/embed/nas1rJpm7wY?rel=0',
    'http://www.youtube.com/watch?v=peFZbP64dsU',
    'http://youtube.com/v/dQw4w9WgXcQ?feature=youtube_gdata_player',
    'http://youtube.com/vi/dQw4w9WgXcQ?feature=youtube_gdata_player',
    'http://youtube.com/?v=dQw4w9WgXcQ&feature=youtube_gdata_player',
    'http://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtube_gdata_player',
    'http://youtube.com/?vi=dQw4w9WgXcQ&feature=youtube_gdata_player',
    'http://youtube.com/watch?v=dQw4w9WgXcQ&feature=youtube_gdata_player',
    'http://youtube.com/watch?vi=dQw4w9WgXcQ&feature=youtube_gdata_player',
    'http://youtu.be/dQw4w9WgXcQ?feature=youtube_gdata_player',
    

    """
    url_parts = urlsplit(url)
    p = PurePosixPath(url_parts.path)
    q = parse_qs(url_parts.query)
    f = url_parts.fragment
    if (q and 'v' in q):
        return q['v'][0]
    elif f:
        # f is a URL!
        fp = PurePosixPath(urlsplit(f).path)
        if fp.match("u/*/*"):
            return fp.name
    else:
        return p.name

if __name__ == "__main__":
    import doctest
    doctest.testmod()            