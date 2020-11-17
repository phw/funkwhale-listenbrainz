# Copyright (c) 2020 Philipp Wolfer <ph.wolfer@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from config import plugins
from .funkwhale_startup import PLUGIN
from .client import ListenBrainzClient, Track

@plugins.register_hook(plugins.LISTENING_CREATED, PLUGIN)
def submit_listen(listening, conf, **kwargs):
    user_token = conf['listenbrainz_token']
    if not user_token:
        return

    logger = PLUGIN['logger']
    logger.info('Submitting listen to ListenBrainz')
    client = ListenBrainzClient(user_token=user_token, logger=logger)
    track = get_track(listening.track)
    client.listen(int(listening.creation_date.timestamp()), track)


def get_track(track):
    artist = track.artist.name
    title = track.title
    album = None
    additional_info = {
        'listening_from': 'Funkwhale',
        'recording_mbid': str(track.mbid),
        'tracknumber': track.position,
        'discnumber': track.disc_number,
    }

    if track.album:
        if track.album.title:
            album = track.album.title
        if track.album.mbid:
            additional_info['release_mbid'] = str(track.album.mbid)

    if track.artist.mbid:
        additional_info['artist_mbids'] = [str(track.artist.mbid)]

    return Track(artist, title, album, additional_info)