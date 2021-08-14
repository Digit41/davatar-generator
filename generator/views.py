from django.shortcuts import render

from PIL import Image, ImageOps
from django.http import HttpResponse
from rest_framework.views import APIView


def resize_with_padding(img, expected_size):
    img.thumbnail((expected_size[0], expected_size[1]))

    padding = (250, 250, 250, 250)

    return ImageOps.expand(img, padding)


def generator_avatar():
    try:
        me = Image.open("MEDIA/apache.png")

        # Relative Path
        # Image on which we want to paste
        img = Image.open("MEDIA/digit41.png")

        # Relative Path
        # Image which we want to paste
        img2 = Image.open("MEDIA/picture2.png")

        width, height = img2.size

        img2 = img2.resize((int(width / 14), int(height / 14)))

        img.paste(img2, (600, 380))

        # Saved in the same relative location
        # img.save("pasted_picture.png")
        #
        # pasted_picture = Image.open("pasted_picture.png")

        me = me.resize((1000, 1000))

        #
        me = resize_with_padding(me, (510, 510))

        me.paste(img, (0, 0), img)

        r = HttpResponse(content_type="image/png")

        me.save(r, 'PNG')

        return r

    except IOError:
        pass


class Avatar(APIView):

    def get(self, request):
        return generator_avatar()
