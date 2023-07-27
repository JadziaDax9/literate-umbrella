import urllib.parse

class MagnetURI:
    def __init__(self, info_hash, display_name=None, trackers=None):
        self.info_hash = info_hash
        self.display_name = display_name
        self.trackers = trackers or []

    def __str__(self):
        magnet_uri = "magnet:?"

        # Add the info hash parameter
        magnet_uri += f"xt=urn:btih:{self.info_hash}"

        # Add the display name parameter if provided
        if self.display_name:
            display_name_encoded = urllib.parse.quote(self.display_name)
            magnet_uri += f"&dn={display_name_encoded}"

        # Add the trackers if available
        if self.trackers:
            trackers_encoded = [urllib.parse.quote(tracker) for tracker in self.trackers]
            magnet_uri += f"&tr={'&tr='.join(trackers_encoded)}"

        return magnet_uri



info_hash = "6D1C4DF9EE2A6D63C82B961BF2FB6FA5E5E92511"
display_name = "Example Torrent"
trackers = [
    "https://33pag.es/announce"
]

magnet = MagnetURI(info_hash, display_name, trackers)


print(magnet)

magnet:?xt=urn:btih:c9e15763f722f23e98a29decdfae341b98d53056&dn=Cosmos+Laundromat&tr=udp%3A%2F%2Fexplodie.org%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.empire-js.us%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=wss%3A%2F%2Ftracker.btorrent.xyz&tr=wss%3A%2F%2Ftracker.fastcast.nz&tr=wss%3A%2F%2Ftracker.openwebtorrent.com&ws=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2F&xs=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2Fcosmos-laundromat.torrent