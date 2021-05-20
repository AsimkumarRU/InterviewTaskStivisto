from dummy_server.server import get_random_request
import datetime
import numpy
from collections import Counter


class Handler:

    def __init__(self, message):
        self.type = message.get("type")
        self.ts = message.get("ts")
        self.content = message.get("content")

    # Determining the day of the week
    def get_weekday(self):
        return datetime.datetime.weekday(self.ts)

    # Processing a text file
    def get_text(self):
        holiday = {
            6: "6️⃣",
            7: "7️⃣"
        }
        text = self.content
        words = text.split()

        if self.get_weekday() == (6 or 7):
            return holiday[self.get_weekday()]
        return len(numpy.unique(words))

    # Processing a image file
    def get_image(self):
        type_img = (self.content).split('.')
        time = self.ts
        if type_img[1] == "jpg":
            return type_img[0]
        return time - datetime.timedelta(hours=24)

    # Processing a video file
    def get_video(self):
        type_video = (self.content).split('.')
        if self.get_weekday() == (6 or 7):
            if len(type_video) == 4:
                return "OK"
            return "REJECT"
        else:
            if len(type_video) == 3:
                return "OK"
            return "REJECT"

    # Processing a sound file
    def get_sound(self):
        c = Counter(self.content)
        for char in self.content:
            if c[char] == 1:
                return char
            elif char == self.content[-1]:
                return None


def main():
    for _ in range(10):
        request = get_random_request()
        print(request)
        func = Handler(request)
        type = request.get("type")
        if type == "text":
            print(func.get_text())
        elif type == "image":
            print(func.get_image())
        elif type == "video":
            print(func.get_video())
        else:
            print(func.get_sound())


if __name__ == "__main__":
    main()
