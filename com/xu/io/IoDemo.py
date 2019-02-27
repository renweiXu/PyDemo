'''
文件打开模式
    mode的主要参数
        打开模式    描述
        r           以只读方式打开文件，文件的指针将会放在文件开始的位置，默认模式
        rb          以二进制格式打开一个文件
        r+          打开一个文件用于读写，文件指针在文件开始位置
        w           打开一个文件只用于写入。如果该文件已存在，则打开文件，并从文件开始位置开始编辑，即原有内容会被删除，如果该文件不存在创建新文件
        wb          以二进制格式打开一个文件，只写
        w+          打开一个文件，可读写
        a           打开一个文件，只追加
        ab           以二进制格式打开一个文件，只追加
        a+            打开一个文件，可读写。如果该文件已存在，文件指针将会放在文件的结尾
'''
#相对路径打开
#news = open('news.txt')
#绝对路径打开
file = open('E:/python/projects/PyDemo/com/xu/io/news.txt',mode='w',encoding='GBK')
#写入内容
file.write("浙江省杭州市西湖区")
#关闭文件
file.close();
file2 = open('news.txt',mode='r+');
#
#追加文件
# file2.write("\nzhangsan")
'''
文件读写位置
    编辑文本是，光标位置是当前的读写位置
    使用seek（）方法可以改变文件开始位置
'''
content = file2.read();
file2.seek(0,0)
file2.write("地址：\r"+content)
file2.read()
file2.close()