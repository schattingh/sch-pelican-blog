import hashlib
import logging
import os
import time
import subprocess
import io
from pelican import signals, generators, settings, contents
from bs4 import BeautifulSoup
from PIL import Image, ImageFilter

logger = logging.getLogger(__name__)


def agf(content_generators):
    for generator in content_generators:
        widths = generator.settings.get('IMAGE_WIDTHS')
        max_width = max(widths)
        siteurl = generator.settings.get('SITEURL')
        content_path = generator.settings.get('PATH')
        image_output_path = os.path.join(generator.settings.get('OUTPUT_PATH'), generator.settings.get('IMAGES_OUTPUT_PATH'))
        if isinstance(generator, generators.ArticlesGenerator):
            for article in generator.articles:
                soup = BeautifulSoup(article._content, 'html.parser')
                imgs = soup.find_all('img')
                if imgs:
                    for img in imgs:
                        # clean up path
                        if '{static}' in img['src']:
                            img['src'] = img['src'].replace('{static}', '')
                        if img['src'][0] == '/':
                            img['src'] = img['src'][1:]
                        img['data-original'] = img['src']
                        source_image_path = os.path.join(content_path, img['src'])
                        with open(source_image_path, 'rb') as f:
                            bytes = f.read()
                        hash = hashlib.sha256(bytes).hexdigest()
                        paths = [ f'{siteurl}/imgs/{width}/{hash}.jpg {width}w' for width in widths ]
                        print(paths)
                        print('\n')
                        strpath = ', '.join(paths)
                        img['srcset'] = strpath
                        img['src'] = f'{siteurl}/imgs/{max_width}/{hash}.jpg'
                        # create image
                        # sent once per image tag found
                        create_responsive_images(source_image_path, hash, widths, image_output_path)
                article._content = soup.decode()


def create_responsive_images(source_image_path, hash, widths, image_output_path):
    for width in widths:
        width_path = os.path.join(image_output_path, str(width))
        if not os.path.isdir(width_path):
            os.makedirs(width_path)
        if not os.path.isfile(f'{width_path}/{hash}.jpg'):
            with Image.open(source_image_path) as img:
                size = img.size
                newheight = round(int(width) / size[0] * size[1], 0)
                opt_img = img.resize((int(width), int(newheight)), resample=Image.LANCZOS)
                opt_img.save(f'{width_path}/{hash}.jpg', quality=90, progressive=True)


def register():
    signals.all_generators_finalized.connect(agf)
