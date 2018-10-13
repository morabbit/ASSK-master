import os, sys

currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
# print(parentUrl)
sys.path.append(parentUrl)