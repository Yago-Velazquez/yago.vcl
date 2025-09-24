import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.match(r'^<iframe (?:width="560" height="315" )?src="(https?://(?:www\.)?youtube.com/embed/xvFZjo5PgG0)"(?: title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)?></iframe>$', s, re.IGNORECASE):
        if "www." in matches.groups(1): return matches.groups(1).replace("youtube.com/embed", "youtu.be").replace("www.", "")
        else: return matches.group(1).replace("youtube.com/embed", "youtu.be")
    else:
        return sys.exit("ERROR")

if __name__ == "__main__":
    main()