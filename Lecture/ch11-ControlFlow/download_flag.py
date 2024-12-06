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
print(type(POP20_CC)) # list


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
DEST_DIR = '/Users/mjhans/workspaces/personal/python_class/2024-2-kbu-advanced-programming/Lecture/ch11-ControlFlow/downloads'


"https://www.fluentpython.com/data/flags/gm/gm.gif"
"""
1. url을 만드는것
2. requests.get() 함수로 호출
3. 반환값을 받는것
4. 반환된 값을 파일로 저장하는것 
5. 1~4번을 반복
"""
def get_flag(cc): 
    """_summary_

    Args:
        cc (string): 국가 코드 대문자

    Returns:
        response.content: _description_
    """
    url = f'{BASE_URL}/{cc.lower()}/{cc.lower()}.gif'
    resp = requests.get(url) # blocking 
    return resp.content



def save_flag(img, filename): 
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR, exist_ok=True) # 없으면 디렉토리 생성
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)



def show(text): 
    print(text, end=' ')
    sys.stdout.flush()

def download_many(cc_list): 
    for cc in sorted(cc_list): 
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')

    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = f'\n{count} flags downloaded in {elapsed:.2f}s'
    print(msg)


if __name__ == '__main__':
    main(download_many)
    
    
    
    