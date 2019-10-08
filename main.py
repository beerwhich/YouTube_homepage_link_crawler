import requests
import re


def main():

    r = requests.get('https://www.youtube.com')

    file = open("YouTube_Homepage.txt", 'w+')
    file.write(r.text)
    file.close()

    file = open("YouTube_Homepage.txt", 'r')

    for line in file:

        pattern = r'<a href="(.+?)"\sclass.+title="(.+?)"\saria'
        match = re.search(pattern, line)
        if match is not None:
            video_link = "https://www.youtube.com" + match.group(1)
            video_title = match.group(2)
            print(video_link + ", " + video_title)
    file.close()


if __name__ == '__main__':
    main()