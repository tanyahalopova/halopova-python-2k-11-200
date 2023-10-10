import re


def is_valid_youtube_link(link):
    pattern = r"(?:(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=|https?:\/\/youtu.be\/)[A-Za-z0-9_-]+(?:(?:\?|&)t=\d+)?"
    return re.search(pattern, link, re.MULTILINE) is not None


text = ["https://www.youtube.com/watch?v=zI48YAa-Jec",
        "https://youtu.be/zI48YAa-Jec",
        "https://youtu.be/zI48YAa-Jec?t=1",
        "https://www.youtube.com/watch?v=zI48YAa-Jec&t=1",
        "Https://www.youtube.com/watch?v"]
for string in text:
    print(is_valid_youtube_link(string))
