#db connect
from time import sleep
from selenium import webdriver
from instapy import InstaPy

session = InstaPy(username="<your_username>", password="<your_password>")
session.login()
session.like_by_tags(["bmw", "mercedes"], amount=5)
#crud