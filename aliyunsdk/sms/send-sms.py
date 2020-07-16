#!/usr/bin/env python
#coding=utf-8
#阿里云中国站-短信发送模板

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('xxxxxxxxxxx01', 'xxxxxxxxxxxxxxxxxxxx02', 'cn-hangzhou')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('dysmsapi.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https') # https | http
request.set_version('2017-05-25')
request.set_action_name('SendSms')

request.add_query_param('RegionId', "cn-hangzhou")
request.add_query_param('PhoneNumbers', "86xxxxxxxxxxxxxx03")
request.add_query_param('SignName', "xxx04")
#request.add_query_param('TemplateCode', "SMS_xxx05")#国内模板
request.add_query_param('TemplateCode', "SMS_xxx06")#国际模板
#request.add_query_param('TemplateParam',{"time":"2020-7-2","number":"23","code":"123456","urlcode":"order/detail?goodsOrderNo=12345678"})
request.add_query_param('TemplateParam',{"time":"2020-7-8","name":"测试短信","number":"23","code":"123456","urlcode":"orderd?goodsOrderNo=12345678"})
response = client.do_action(request)
print(str(response, encoding = 'utf-8'))
#x01 x02 accesskey
#x03 接收号码
#x04 短信签名
#x05 x06 短信模板
#2020-7-17
