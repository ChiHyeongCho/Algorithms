
# 정규표현식 : 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어
#            복잡한 문자열의 검색과 치환을 위해 사용

# 메타문자 종류 : . ^ $ * + ? \ | ( ) { } [ ]

import re

variable_name = re.compile('정규펴현식') #sre.SRE_Pattern 클래스 객체

p = re.compile('[a-z]+')

# 매치를 검색할 수 있는 메서드
p.match('aaaaa') #시작부터 일치하는 패턴 찾기
p.search('aaaaa') #처음으로 매치되는 문자열 탐색
p.findall('aaaa') #일치하는 모든 패턴을 찾아 리스트로 반환
p.fullmatch('aaaa') #시작과 끝이 정확하게 패턴과 일치하는지 찾기