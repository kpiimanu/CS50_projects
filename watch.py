# Program to extract url from an HTML input and print if valid

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Searching for a match in html <iframe ... ></iframe>
    if re.search(r"<iframe(.)*><\/iframe>", s):
        # Searching for a match that includes http(s) with or without www
        # Any alphanumeric will be accepted following the embed/
        youtube_link = re.search(
            r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([\w]+)", s
        )
        if youtube_link:
            embed_link = youtube_link.groups()
            return "https://youtu.be/" + embed_link[3]


if __name__ == "__main__":
    main()