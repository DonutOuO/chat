def read_file(filename):
	chat=[]
	with open (filename,'r' , encoding='utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat


def convert(chat):
	person =None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count=0
	viki_sticker_count=0
	allen_photo_count=0
	viki_photo_count =0
	for line in chat:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] =='貼圖':
				allen_sticker_count = allen_sticker_count +1
			elif s[2] == '圖片':
				allen_photo_count = allen_photo_count +1
			else:
				for m in s[2:]:
					allen_word_count = allen_word_count + len(m)
		elif name == 'Viki':
			if s[2] =='貼圖':
				viki_sticker_count = viki_sticker_count +1
			elif s[2] == '圖片':
				viki_photo_count = viki_photo_count +1				
			else:
				for m in s[2:]:
					viki_word_count = viki_word_count + len(m)
	print('Allen說了' , allen_word_count,'個字')
	print('Allen傳了',allen_sticker_count, '個貼圖','和',allen_photo_count,'個圖片')
	print('Viki說了' , viki_word_count,'個字') 
	print('Viki傳了'	,viki_sticker_count ,'個貼圖','和',viki_photo_count,'個圖片')
		#print(s)
	return()


def write_file(filename, chat):
	with open(filename,'w') as f:
		for line in chat:
			f.write(line + '\n')


def main():
	chat = read_file('LINE-viki.txt')
	chat = convert(chat)
	#write_file('output_2.txt', chat)


main()
