from src.models import MagnetURI


def main():
    info_hash = "6D1C4DF9EE2A6D63C82B961BF2FB6FA5E5E92511"
    display_name = "Example Torrent"
    trackers = [
        "https://tracker.example.com/announce",
        "https://tracker2.example.com/announce",
    ]

magnet = MagnetURI(info_hash, display_name, trackers)
print(magnet)
