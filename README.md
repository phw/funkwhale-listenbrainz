# ListenBrainz plugin for Funkwhale

Submit your listens to [ListenBrainz](https://listenbrainz.org) when listening
to your music with [Funkwhale](https://funkwhale.audio/).

## Installation

Place the `listenbrainz` directory with all included files in the Funkwhale
plugins directory in `FUNKWHALE_PLUGINS_PATH`. By default this is `/srv/funkwhale/plugins`.

Then enable the ListenBrainz plugin by adding it to the `FUNKWHALE_PLUGINS`
environment variable, e.g.

    FUNKWHALE_PLUGINS=listenbrainz

See the [Funkwhale plugin documentation](https://docs.funkwhale.audio/developers/plugins.html) for details.

## Usage

The ListenBrainz plugins needs to be configured per user. Each user needs to
configure their ListenBrainz user token in the user's settings. The ListenBrainz
user token can be found at https://listenbrainz.org/profile/
