# coding:utf-8
from pymysql import *

def main():
    conn = connect(host='localhost', port=3306, database='ihome', user='root', password='root', charset='utf8')
    cs1 = conn.cursor()
    # # 非安全的方式
    # # 输入 " or 1=1 or "   (双引号也要输入)
    # find_name = '"or 1=1 or"'
    # sql = 'select * from goods where name="%s"' % find_name
    # print("""sql===>%s<====""" % sql)
    # # 执行select语句，并返回受影响的行数：查询所有数据
    # count = cs1.execute(sql)
    # print(count)
    # 安全方式：
    # 构造参数列表
    # find_name = '"or 1=1 or"'
    # params = [find_name]
    # # 执行select语句，并返回受影响的行数：查询所有数据
    # count = cs1.execute('select * from goods where name=%s', params)

    mobile = '18565676726'
    passwd = "dong159753"
    # sql = "insert into ih_user_profile(up_name,up_mobile,up_passwd) values(%s,%s,%s);"
    # params = [mobile, mobile, passwd]
    # user_id = cs1.execute(sql, params)
    params = [mobile]
    res = cs1.execute("select up_user_id,up_name,up_passwd from ih_user_profile where up_mobile=%s",params)

    # 打印受影响的行数
    print(res)
    result = cs1.fetchall()
    print(result[0][0])
    print(result[0][1])
    print(result[0][2])
    conn.commit()
    res1 = cs1.close()
    res2 = conn.close()
    print(res1,res2)


if __name__ == '__main__':
    main()