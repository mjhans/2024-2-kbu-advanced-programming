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

# 대부분의 나라들의 ISO 3166 국가 코드
ALL_CC = ('AD AE AF AG AL AM AO AR AT AU AZ BA BB BD BE BF BG BH BI BJ BN BO BR BS BT'
'BW BY BZ CA CD CF CG CH CI CL CM CN CO CR CU CV CY CZ DE DJ DK DM DZ EC EE'
'EG ER ES ET FI FJ FM FR GA GB GD GE GH GM GN GQ GR GT GW GY HN HR HT HU ID'
'IE IL IN IQ IR IS IT JM JO JP KE KG KH KI KM KN KP KR KW KZ LA LB LC LI LK'
'LR LS LT LU LV LY MA MC MD ME MG MH MK ML MM MN MR MT MU MV MW MX MY MZ NA'
'NE NG NI NL NO NP NR NZ OM PA PE PG PH PK PL PT PW PY QA RO RS RU RW SA SB'
'SC SD SE SG SI SK SL SM SN SO SR SS ST SV SY SZ TD TG TH TJ TL TM TN TO TR'
'TT TV TW TZ UA UG US UY UZ VA VC VE VN VU WS YE ZA ZM ZW').split()

BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'downloads'



