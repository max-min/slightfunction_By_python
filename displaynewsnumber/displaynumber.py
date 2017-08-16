
'''
	实现类似微信未读消息样式
'''








'''
PIL.Image.open(fp, mode='r') 
	打开并辨认出图片，生成图片对象

PIL.ImageDraw.Draw.text(xy,text, fill=None, font=None, anchor=None) 
用来为图片对象绘制数字

PIL.ImageDraw.Draw.pieslice(xy, start, end, fill=None, outline=None)
 用来为图片对象绘制扇形（圆形也就是特殊的扇形辣）

PIL.ImageFont.truetype(font=None, size=10, index=0, encoding='') 
	用来读取 TrueType 和 OpenType 字体文件，同时生成字体对象，还能设定字体对象的大小

'''
from PIL import Image, ImageDraw, ImageFont

def addNewsNum(nums):
	news_pic = 'news.png'

	im = Image.open(news_pic)
	w,h = im.size  # 获取图片对象的宽和高
	
	

	

	# 不难发现坐标系是以左上角为原点，向下y递增，向右x递增
	if nums < 10:
		ImageDraw.Draw(im).pieslice([(w/3*2, 0), (w, h/6)], 0, 360, fill="red")
		# 绘制圆形，第一个参数界定绘制区域，我选择了宽高为原图1/3的右上角区域
		# 创建字体对象，我把字体的大小设为高度1/4，如果数字多于个位应该再小点
		font = ImageFont.truetype('kaiti.ttf', int(h/6))
		# 第一个参数是坐标，第二个参数是文本绘制内容，第三个是字体对象
		ImageDraw.Draw(im).text((w * 0.8, h * 0.01), str(nums), font=font, fill="white")
	elif nums < 99:
		ImageDraw.Draw(im).pieslice([(w/3*2, 0), (w, h/6)], 0, 360, fill="red")
		font = ImageFont.truetype('kaiti.ttf', int(h/6))
		ImageDraw.Draw(im).text((w * 0.75, h * 0.01), str(nums), font=font, fill="white")
	else:
		ImageDraw.Draw(im).pieslice([(w/3*2, 0), (w, h/6)], 0, 360, fill="red")
		font = ImageFont.truetype('kaiti.ttf', int(h/6))
		ImageDraw.Draw(im).text((w * 0.72, h * 0.01), '99+', font=font, fill="white")


	im.show()  # 展示绘制结果（使用系统默认的图片浏览器）
	#当然也可以用im.save()函数保存结果


if __name__ =='__main__':
	addNewsNum(500)

