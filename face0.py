# -*- coding:utf-8 -*-
import cv2
import urllib2
import urllib
import time
import sys
import pyttsx

img = cv2.imread("text.jpg")
cv2.namedWindow("原图")
cv2.imshow("原图", img)

#URL
http_url='https://api-cn.faceplusplus.com/facepp/v3/detect' 
#用户信息
key = "ieSzJ4NhWjAVsXkqpVACM4XmkvZ5h0oF"    
secret = "H6Hfq0UoNe59MYNy8LbXUyMn49xC39xE"
#图片存储路径
filepath = r"/home/pi/text/text.jpg"


boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(data)
#buld http request
req=urllib2.Request(http_url)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)
try:
    #req.add_header('Referer','http://remotserver.com/')
    #post data to server
    resp = urllib2.urlopen(req, timeout=5)
    #get response
    qrcont=resp.read()
    print qrcont       

except urllib2.HTTPError as e:
    print e.read()


mydict = eval(qrcont)
faces = mydict["faces"]
faceNum = len(faces)
print("识别到了%d个人脸"%(faceNum))



f=open('out.txt','w')
print >>f,"出勤人数为%d人"%(faceNum)
f.close()



# print type(resp)
