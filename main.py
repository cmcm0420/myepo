import function as sf
print('--여행 예약 관리 시스템 --')
if sf.db_connect() == False:
    exit(1)
while (True):
    try:
        print('1. 고객 등록\n2. 전체 고객 목록 조회\n3. 고객 정보 수정\n4. 고객 정보 삭제\n5. 여행 상품 조회\n6. 여행 예약 고객 목록 조회\n7. 고객의 여행 상품 등록\n8. 프로그램 종료 ')
        try:
            action = int(input('실행할 프로그램 번호 입력>'))
        except ValueError:
            print('숫자 1~8를 입력하십시오')
            continue
        if action >= 1 and action <= 8:
            pass
        else:
            print('1 ~ 8 사이의 번호를 입력해주세요')
        if action == 1:
            print("등록할 고객 정보를 입력해주십시오")
            f_mem_name = input('이름> ')
            f_mem_addr = input('주소> ')
            f_mem_phone = input('전화번호> ')
            f_mem_num = input('총 인원 수> ')
            sf.add_member(f_mem_name, f_mem_addr, f_mem_phone, f_mem_num)
        elif action == 2:
            print('고객 목록 조회 화면')
            print(f'{"고객번호":^6} {"고객이름":^3} {"주소":^10} {"전화번호":^15} {"총 인원 수":^5}')
            sf.show_member()
        elif action == 3:
            print('고객 정보 수정 화면')
            print('다음의 목록 중 수정할 고객의 정보를 입력해주세요.')
            sf.show_member()
            update_info = sf.get_member()
            if update_info == None:
                print('고객 정보가 잘못 입력되었습니다.')
                continue
            if sf.update_member(update_info) == True:
                print("수정이 완료되었습니다.")
            else:
                print("수정이 실패했습니다. 다시 진행해주십시오")
        elif action == 4:
            print('고객 정보 삭제 화면')
            sf.show_member()
            delete_info = input("삭제할 고객 번호>")
            if delete_info == None:
                print("고객 번호가 잘못 입력되었습니다.")
                continue
            if sf.delete_member(delete_info) == True:
                print("고객 정보가 삭제되었습니다.")
            else:
                print("삭제가 실패되었습니다. 다시 진행해주십시오")
        elif action == 5:
            print('여행상품 목록 조회 화면')
            print(f'{"여행지 코드":^4} {"여행지":^8} {"금액":^7} {"기간":^8}')
            sf.show_travel()
        elif action == 6:
            print('여행 예약 고객 목록 조회 화면')
            print(f'{"고객번호":^6} {"고객이름":^3} {"총 인원 수":^5} {"여행지":^10} {"금액":^15} {"기간":^8} ')
            sf.show_travelmember()
        elif action == 7:
            print('고객의 여행 상품 등록 화면')
            mem_no = input('여행갈 고객>')
            print("여행 정보를 입력해주십시오")
            trav_no = input('여행지 코드> ')
            trav_site = input('여행지> ')
            trav_price = input('금액> ')
            trav_date = input('여행기간> ')
            sf.add_travel(trav_no, trav_site, trav_price, trav_date,mem_no)
        elif action == 8:
            print('프로그램 종료')
            sf.db_close()
            break
    except KeyboardInterrupt:
        print("Program을 종료합니다.")
    sf.db_close()
    break