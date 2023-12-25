# machine-learning
## 动漫人脸生成系统

### 环境配置

Django项目配置

python==3.9

Django==3.2.1

mysqlclient == 2.2.0

MySQL: mysql-5.7.41-winx64



animeGAN模型运行配置：

torch==2.1.1+cu121

numpy==1.26.0

opencv-python==4.8.1.78



**说明：**使用上述配置下的模型可以切换设备（本系统默认使用CPU）

方法①：

修改 app01/views/style_conversion.py 中第76行如下使用GPU运行

```python
cmd = "python test.py --origin_img " + filename " --device cuda:0"
```

方法②：

修改 test.py 中第78行如下使用GPU运行

```python
default='cpu',
```



### 运行前准备

1. 创建数据库

   管理员CMD命令启用MySQL服务后执行命令：

   ```
   create database animegandb DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
   ```

2. Pycharm终端顺序执行命令：

   ```
   python manage.py makemigrations
   ```

   ```
   python manage.py migrate
   ```



### 运行

1. 点击Pycharm运行按钮后在运行窗口点击 http://127.0.0.1:8000/ 跳转至浏览器可见：

   ```
   Using the URLconf defined in animeGAN.urls, Django tried these URL patterns, in this order:
   	1. media/(?P<path>.*)$ [name='media']
   	2. homepage/
   	3. upload/
   	4. exhibition1/
   	5. exhibition2/
   	6. login/
   	7. signup/
   	8. logout/
   	9. forget/
   The empty path didn’t match any of these.
   ```

2. 前往  http://127.0.0.1:8000/login/ 进行登录即可

