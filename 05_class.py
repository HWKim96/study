'''
모든 사원들은 각자
출근하시면 !!!
아침업무로 배달 온 박스 안에 물건을 전부 꺼내서
사과는 냉장실에
아이스크림은 냉동실에 넣어주시고
나머지는 전부 폐기처분 해주세요.
그리고 나서 아침업무를 확인해주세요.
'''

class 업무():
    
    def 아침업무(self, 박스): # self
    # self : 내부 변수를 움직이기 위해서 self 사용
        for 물건 in 박스:
            if 물건 == '사과':
                print(f"'{물건}'는 냉장실에 넣기")
            elif 물건 == '아이스크림':
                print(f"'{물건}'은 냉동실에 넣기")
            else:
                print(f"'{물건}'은 폐기처분")
                

출근 = True

if 출근:
    박스 = ['콩', '참치', '사과', '아이스크림','과자']
    
    출근후업무 = 업무()
    출근후업무.아침업무(박스)
    

class 필수업무():
    아침업무유무 = False # 초기값
    
    def 아침업무체크(self): 
        self.아침업무유무 = True
        
    def 아침업무(self, 박스): # self
    # self : 내부 변수를 움직이기 위해서 self 사용
        for 물건 in 박스:
            if 물건 == '사과':
                print(f"'{물건}'는 냉장실에 넣기")
            elif 물건 == '아이스크림':
                print(f"'{물건}'은 냉동실에 넣기")
            else:
                print(f"'{물건}'은 폐기처분")
                
        self.아침업무체크()

출근 = True

if 출근:
    박스 = ['콩', '참치', '사과', '아이스크림','과자']
    
    닥터윌_업무 = 필수업무()
    print(닥터윌_업무.아침업무유무)
    
    닥터윌_업무.아침업무(박스)
    print(닥터윌_업무.아침업무유무)
    
    쯔위_업무 = 필수업무()
    print(쯔위_업무.아침업무유무)
    
    희성_업무 = 필수업무()
    print(희성_업무.아침업무유무)
    
    # class: 