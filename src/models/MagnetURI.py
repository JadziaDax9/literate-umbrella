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
