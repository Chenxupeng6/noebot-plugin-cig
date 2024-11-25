# 获取星际公民人员账号信息
import requests
import re
from lxml import etree
from datetime import datetime
from nonebot import on_message, on_command, require
from PIL import Image, ImageDraw, ImageFont
from PIL import Image
import random
import os
from PIL import Image
import requests
import json
import httpx
import nonebot
from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.plugin.on import on_regex
from nonebot.typing import T_State
import nonebot
from nonebot.adapters.onebot.v11.event import MessageEvent as V11MessageEvent
from nonebot.adapters.onebot.v11.message import MessageSegment as V11MessageSegment
from nonebot import on_command
# from aiocqhttp import MessageSegment

# exchange = on_command("查ID", aliases={'查id', '游戏ID'}, priority=1)
exchange = on_regex(r'查id',priority=1)

@exchange.handle()
async def handle_exchange(bot: Bot, event: V11MessageEvent, state: T_State):
    # 获取用户输入的金额和目标货币
    args = str(event.get_message()).strip().split()
    nonebot.logger.info(args)

    if len(args) < 2:
        await exchange.reject("请输入有效的游戏名称")

    amount_str, target_currency = args[0], args[1]
    # if not target_currency.isdigit():
    #     await exchange.reject("游戏名称为字母")
    # 获取游戏ID
    amount = (target_currency)


    async def get_exchange_rate():
        async with httpx.AsyncClient() as client:
            url = f'https://robertsspaceindustries.com/citizens/{amount}'
            headers = {
                'User-Agen': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
                'Cookie': '_stripe_mid=aa9fd994-2374-4abc-824c-44482860cfa75b8636; _ga_RDZLK16ZQE=GS1.2.1706190454.1.1.1706190513.1.0.0; _ga_V6MWYXRQNP=GS1.1.1706190160.7.1.1706193485.60.0.0; _ga_FBVH2Q6FPF=GS1.1.1706256647.9.0.1706256647.0.0.0; _ga=GA1.2.1204761305.1672919631; _rsi_device=9i8ii5qjebyoryfogn9edlyaod; wsc_hide=false; _ga_XGSMCBZNFM=GS1.2.1713508397.2.0.1713508397.60.0.0; wsc_view_count=2; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1715387933455%2Cregion:%27CN%27}; _gcl_au=1.1.321275428.1715387935; Rsi-Token=262f98c6b8a6af04ef549e5903304f8e; _gid=GA1.2.631157703.1716423455; Rsi-XSRF=vTRQZg%3AZKQQi%2Bv7pvggF7%2Ft1X7yMQ%3AmRiKcClHXxeyCV%2B1ncxcxQ%3A1716534216493'
                }

            response = await client.get(url,headers=headers)
            html1 = etree.HTML(response.text)
            picture5 = 'https://cdn.robertsspaceindustries.com/static/images/account/avatar_default_big.jpg'
            picture = html1.xpath('//div[@class="thumb"]/img/@src')[0]
            if picture == picture5:
                url1 = picture
                res1 = requests.get(url1)
                # print(res1.content)
                with open(f'video/{amount}.jpg', 'wb') as f:
                    f.write(res1.content)
            else:
                picture1 = 'https://robertsspaceindustries.com/' + picture
                # input(picture1)
                # 保存玩家照片
                url1 = picture1
                res1 = requests.get(url1)
                # print(res1.content)
                with open(f'video/{amount}.jpg', 'wb') as f:
                    f.write(res1.content)
            # 玩家舰队照片
            picture2 = html1.xpath('//div[@class="thumb"]/a/img/@src')[0]
            picture3 = 'https://robertsspaceindustries.com/' + picture2
            url2 = picture3
            res2 = requests.get(url2)
            # print(picture3)
            # 保存玩家照片
            with open(f'video/{amount}1.jpg', 'wb') as f:
                f.write(res2.content)

            # 舰队名字
            name = html1.xpath('//p[@class="entry"]/a/text()')[0]
            # 舰队小名字
            name1 = html1.xpath(
                '//div[@class="main-org right-col visibility-V"]/div[@class="inner clearfix"]/div[@class="info"]/p[2]/strong/text()')[
                0]
            # 舰队职位
            name2 = html1.xpath('//div[@class="info"]/p[3]/strong/text()')[0]
            # 加入公民时间
            name3 = html1.xpath('//div[@class="inner"]/p[1]/strong/text()')[0]
            # 勋章
            name4 = html1.xpath('//div[@class="inner clearfix"]/div[@class="info"]/p[3]/span/text()')[2]
            # name4 = [p.strip() for p in res][2]
            # print(name4)
            # 地区
            name5 = html1.xpath('normalize-space(//div[@class="inner"]/p[2]/strong/text())')
            # input(name5)
            # name7 = [p.strip() for p in name5][0]
            # input(name7)
            name7 = name5
            # 语言
            name6 = html1.xpath('normalize-space(//div[@class="inner"]/p[3]/strong/text())')
            # name8 = [p.strip() for p in name6][0]
            name8 = name6
            # 日期转换
            from dateutil import parser
            # import datetime

            # 定义英文日期字符串
            english_date = name3

            # 将英文日期字符串转换为datetime对象
            dt = parser.parse(english_date)

            # 获取月份、日期和年份信息
            month = str(dt.month).zfill(2)
            day = str(dt.day).zfill(2)
            year = str(dt.year)

            # 构建中文日期字符串
            chinese_date = f"{year},{month} {day}"
            # print(f"中文日期：{chinese_date}")

            # 写入Excel表保存
            import pandas as pd
            # 读取excel表
            original_data = pd.read_excel('星际公民玩家信息.xlsx')
            # 创建一个DataFrame
            data2 = {'玩家ID': [amount], '舰队名字': [name], '舰队小名字': [name1], '舰队职位': [name2],
                     '加入公民时间': [chinese_date], '勋章': [name4], '地区': [name7], '语言': [name8]}
            data2 = pd.DataFrame(data2)
            # 将DataFrame写入Excel文件
            save_data = pd.concat([original_data, data2], axis=0)
            save_data.to_excel('星际公民玩家信息.xlsx', index=False)
            # 删除重名的数据
            original_data = pd.read_excel('星际公民玩家信息.xlsx')
            # print(original_data)
            df_unique = original_data.drop_duplicates(
                subset=['舰队名字', '舰队小名字', '舰队职位', '加入公民时间', '勋章', '地区', '语言'])
            df_unique.to_excel('星际公民玩家信息.xlsx', index=False)

            # 获取当前目录下所有图片文件名列表
            images_dir = 'C:/Users/Lenovo/PycharmProjects/pythonProject/CSTU/测试4.png'  # 指定存放图片的目录路径
            file_list = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]

            # 从图片文件名列表中随机选择一张图片进行打开
            random_index = random.randint(0, len(file_list) - 1)
            random_filename = file_list[random_index]

            # 使用Image.open()函数打开图片
            # 打开已有图片
            image = Image.open(os.path.join(images_dir, random_filename))

            # 创建一个可以在给定图像上绘画的对象
            draw = ImageDraw.Draw(image)

            # 日期
            import time

            # 获取当前日期
            current_date = time.strftime("%Y-%m-%d", time.localtime())
            # print(current_date)
            text16 = '日期:'

            # 定义要添加的文本
            text8 = '游戏  ID: '
            text9 = '入坑时间:'
            text10 = '勋      章:'
            text11 = '地      区:'
            text12 = '语      言:'
            text13 = '舰队名称:'
            text14 = '舰队旗帜:'
            text15 = '舰队职位:'

            text = amount
            text1 = chinese_date
            text2 = name4
            text3 = name7
            text4 = name8
            text5 = name
            text6 = name1
            text7 = name2

            # 定义字体和大小（需要指定字体文件的路径）
            font = ImageFont.truetype('C:/users/Lenovo/AppData/Local/Microsoft/Windows/Fonts/STZHONGS.TTF', 42)

            # 定义文本的位置（例如，左上角）
            text_position = (750, 400)
            text_position1 = (750, 500)
            text_position2 = (750, 600)
            text_position3 = (750, 700)
            text_position4 = (750, 800)
            text_position5 = (2000, 540)
            text_position6 = (2000, 640)
            text_position7 = (2000, 740)

            text_position8 = (500, 400)
            text_position9 = (500, 500)
            text_position10 = (500, 600)
            text_position11 = (500, 700)
            text_position12 = (500, 800)
            text_position13 = (1750, 540)
            text_position14 = (1750, 640)
            text_position15 = (1750, 740)
            text_position18 = (1300, 1200)
            text_position16 = (1200, 1199)

            # 将文本添加到图像上
            draw.text(text_position, text, font=font, fill=(255, 159, 168))
            draw.text(text_position1, text1, font=font, fill=(255, 159, 168))
            draw.text(text_position2, text2, font=font, fill=(255, 159, 168))
            draw.text(text_position3, text3, font=font, fill=(255, 159, 168))
            draw.text(text_position4, text4, font=font, fill=(255, 159, 168))
            draw.text(text_position5, text5, font=font, fill    =(255, 159, 168))
            draw.text(text_position6, text6, font=font, fill=(255, 159, 168))
            draw.text(text_position7, text7, font=font, fill=(255, 159, 168))

            draw.text(text_position8, text8, font=font, fill=(255, 159, 168))
            draw.text(text_position9, text9, font=font, fill=(255, 159, 168))
            draw.text(text_position10, text10, font=font, fill=(255, 159, 168))
            draw.text(text_position11, text11, font=font, fill=(255, 159, 168))
            draw.text(text_position12, text12, font=font, fill=(255, 159, 168))
            draw.text(text_position13, text13, font=font, fill=(255, 159, 168))
            draw.text(text_position14, text14, font=font, fill=(255, 159, 168))
            draw.text(text_position15, text15, font=font, fill=(255, 159, 168))

            draw.text(text_position18, current_date, font=font, fill=(255, 159, 168))
            draw.text(text_position16, text16, font=font, fill=(255, 159, 168))
            # 保存修改后的图像
            overlay = Image.open(F'video/{amount}.jpg')
            overlay1 = Image.open(F'video/{amount}1.jpg')
            # overlay2 = Image.open(f'video/logo.jpg')
            # overlay3 = Image.open(f'video/logo2.jpg')
            # 设定要添加的图像的左上角位置
            position = (79, 450)  # x、y为相对于原始图像的坐标值
            position1 = (1450, 550)
            # position2 = (2260, 10)
            # position3 = (800, 10)
            # 调整要添加的图像的大小
            size = overlay.resize((320, 320))  # width、height为新的宽度和高度
            size1 = overlay1.resize((250, 250))
            # size2 = overlay2.resize((220, 250))
            # size3 = overlay3.resize((1000, 100))
            # 将要添加的图像粘贴到原始图像中指定位置
            image.paste(size, position)
            image.paste(size1, position1)
            # image.paste(size2, position2)
            # image.paste(size3, position3)
            image.save(f'CIG1/{amount}卡片.png')
            geme = f'C:/Users/Lenovo/PycharmProjects/pythonProject/bot1/CIG1/{amount}卡片.png'
            exchange_rate = geme
            await bot.call_api('send_group_msg', **{  # 发送退出应用群聊消息
                'group_id': int(181143547),
                'message': [
                    {
                        "type": "text",
                        "data": {
                            "text": '斯曼达洛舰队专属'
                        }
                    },
                    {
                        "type": "image",
                        "data": {
                            "file": exchange_rate
                        }
                    }
                ]
            })

            # await session.send(MessageSegment.image(image_path))
        return exchange_rate

    # 调用函数获取玩家卡片
    exchange_rate = await get_exchange_rate()
    exchange_rate= 'Spartan Mandalorian Fleet'
    # 返回结果给用户
    await exchange.finish(exchange_rate)
#
# @exchange.handle()
# async def _handle_v11(event: V11MessageEvent):
#    pic_content = ''
#    msg = V11MessageSegment.image(pic_content)
#    await exchange.finish(msg)




