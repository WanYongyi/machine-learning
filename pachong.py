from urllib import request
import os
import re #正则表达式库

#输入类别名称,子类别名称，文件名，输出图片路径
def get_path(classname,subclassname,filename):
    #获取当前工作路径
    cwd = os.getcwd()
    #获取图像的保存目录
    dir_path = cwd+'/vcg_test/' + classname +'/'+ subclassname
    #目录是否存在,不存在则创建目录
    if os.path.exists(dir_path):
        pass
    else:
        os.makedirs(dir_path)
    #获取图像的绝对路径
    file_path = dir_path +'/'+ filename
    return file_path


classnames = ['super_star', 'cartoon']  # 假设我们分类是明星和动漫人物
keypoints = ['%E6%98%8E%E6%98%9F', '%E5%8A%A8%E6%BC%AB%E4%BA%BA%E7%89%A9']  # 关键字对应
gender_file_path = ['male', 'female']  # 对于人的分类检索可以按性别筛选
all_page = 1  # 想要下载的总页数,其中每页与检索相同,为100张
for class_index, phrase in enumerate(classnames):
    sum_all_num = 0
    if class_index >= 0:  # 从某一类断开则选择该类为起始点
        # if class_index == 1  : #例如下载动漫人物时被服务器Kill掉可以改为该行继续下载
        for gender_index, gender in enumerate(gender_file_path):
            if gender_index >= 0:  # 从性别某类断开则选择该类为起始点
                for page in range(1, all_page + 1):
                    num_in_page = 1
                    # 获得url链接,这里额外增加了筛选条件:图片中仅有一个人
                    url = 'https://www.vcg.com/creative/search?phrase=' + keypoints[
                        class_index] + '&creativePeopleNum=2&creativeGender=' + str(gender_index + 1) + '&page=' + str(
                        page)
                    header = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
                        #                'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
                    }
                    req = request.Request(url=url, headers=header)
                    openhtml = request.urlopen(req).read().decode('utf8')

                    # 正则表达式
                    com = re.compile('"url800":.*?/creative/.*?.jpg"')

                    # 匹配URl地址
                    urladds = com.findall(openhtml)
                    for urladd in urladds:
                        # try ... except防止匹配出错后程序停止
                        try:
                            add = 'http:' + urladd.strip('"url800":')
                            # 获取文件名称,格式:vcg+性别+获取方式+page+page中的第几张图片，vcg_raw代表原vcg网站对性别分类
                            filename = classnames[class_index] + '_' + gender_file_path[
                                gender_index] + '_vcg_raw_page' + str(page) + '_' + str(num_in_page) + '.jpg'
                            path = get_path(classnames[class_index], gender_file_path[gender_index], filename)
                            print('当前下载...', filename)

                            dom = request.urlopen(add).read()
                            with open(path, 'wb') as f:
                                f.write(dom)
                                sum_all_num += 1
                                num_in_page += 1
                        except:
                            print('当前该任务总共总共下载:', sum_all_num)  # 监控进度
                        if sum_all_num % 50 == 0:  # 监控进度
                            print('当前该任务总共下载:', sum_all_num)
