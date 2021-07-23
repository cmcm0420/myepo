import pymysql
conn = 0
curs = 0
def db_connect():
        global conn, curs
        try:
            conn = pymysql.connect(host='###', user='###', password='###', db='###', charset='utf8')
        except:
            print("DB 연결을 실패했습니다.")
            return False
        # print(conn)
        curs = conn.cursor(pymysql.cursors.DictCursor)
        return True
def db_close():
        curs.close()
        conn.close()
def check_member(mem_no, mem_name):
        sql = f'select mem_name from member_t where mem_no = {mem_no}'
        curs.execute(sql)
        row = curs.fetchone()
        if row == None:
            return False
        if row['mem_name'] == mem_name:
            return True
        else:
            return False
def get_member():
        mem_no = int(input('고객 번호> '))
        mem_name = input('고객 이름> ')
        if check_member(mem_no, mem_name) == False:
            return None
        mem_addr = input('수정할 주소>')
        mem_phone = input('수정할 전화번호>')
        mem_num = input('수정할 총 인원수>')
        member = {}
        member['mem_no'] = mem_no
        member['mem_name'] = mem_name
        member['mem_addr'] = mem_addr
        member['mem_phone'] = mem_phone
        member['mem_num'] = mem_num
        return member
def add_member(mem_name, mem_addr, mem_phone, mem_num):
        sql = f'insert into member_t ( mem_name, mem_addr, mem_phone, mem_num) values ( "{mem_name}", "{mem_addr}","{mem_phone}","{mem_num}" )'
        curs.execute(sql)
        conn.commit()
        print("해당 데이터 입력 완료되었습니다")
def show_travelmember():
        #f'{"고객번호":^6} {"고객이름":^3} {"총 인원 수":^5} {"여행지":^10} {"금액":^15} {"기간":^8} ')
        sql = f'''select a.mem_no, a.mem_name, a.mem_num, b.trav_site, b.trav_price, b.trav_date 
            from member_t a,travel_t b where a.mem_no = b.mem_no '''
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
                print("  ",row['mem_no'],"  ", row['mem_name'],"  ", row['mem_num'],"  ", row['trav_site'],"  ", row['trav_price'],"  ",row['trav_date'])
def show_member():
        sql = f'''select mem_no, mem_name, mem_addr, mem_phone, mem_num from member_t '''
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
            print("  ",row['mem_no'],"    ", row['mem_name'],"   ", row['mem_addr'],"    ", row['mem_phone'],"     ", row['mem_num'])
def show_travel():
        sql = f'''select trav_no, trav_site, trav_price, trav_date from travel_t '''
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
            print("  ", row['trav_no'], "     ",row['trav_site'],"    ",row['trav_price'],"   ",row['trav_date'])
def update_member(update_info):
        sql = f'''update member_t 
        set mem_num = "{update_info["mem_num"]}", mem_addr = "{update_info["mem_addr"]}", mem_phone = "{update_info["mem_phone"]}"  
        where mem_no = {update_info["mem_no"]}'''
        curs.execute(sql)
        conn.commit()
        return True
def delete_member(delete_info):
        sql=f'delete from member_t where mem_no="{delete_info}"'
        curs.execute(sql)
        conn.commit()
        return True
def add_travel(trav_no, trav_site, trav_price, trav_date, mem_no):
        sql = f'insert into travel_t (trav_no, trav_site, trav_price, trav_date, mem_no) values ( "{trav_no}", "{trav_site}","{trav_price}","{trav_date}","{mem_no}" )'
        curs.execute(sql)
        conn.commit()
if __name__ == '__main__':
    if db_connect() == False:
        exit(1)
    db_close()