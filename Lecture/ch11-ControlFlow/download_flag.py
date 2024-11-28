################################################################################
# python std library                                                           #
################################################################################
import os
import time
import sys

################################################################################
# pip library                                                                  #
################################################################################
import requests

# 인구가 많은 순서의 ISO 3166 국가 코드
# https://en.wikipedia.org/wiki/ISO_3166
# https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
# 
POP20_CC =  ('CN IN US ID BR PK NG BD RU JP '
                'MX PH VN ET EG DE IR TR CD FR').split() 

BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'downloads'



