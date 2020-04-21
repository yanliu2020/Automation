# -*- coding: utf-8 -*-


class Img:

    def __init__(self):
        self.imgs = []

    def clear_img(self):
        self.imgs.clear()

    def add_img(self, driver):
        self.imgs.append(driver.get_screenshot_as_base64())

    def get_imgs(self):
        return self.imgs


img = Img()
