# Section01
# 파이썬 소개 및 작업 환경 설정

# 기본 출력
print('Hello Python!')

import simplejson as json

test_dict = {'1':32, '3':53, '6':23, '2':56}

print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))
