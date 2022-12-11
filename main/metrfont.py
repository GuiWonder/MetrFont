import os, json, sys
from fontTools.ttLib import TTFont
pydir = os.path.abspath(os.path.dirname(__file__))

def ckfile(f):
	f=f.strip()
	if not os.path.isfile(f):
		if os.path.isfile(f.strip('"')):
			return f.strip('"')
		elif os.path.isfile(f.strip("'")):
			return f.strip("'")
	return f

print('====思源字体行宽调整====\n')
inf=str()
outf=str()
if len(sys.argv)<3:
	while not os.path.isfile(inf):
		inf=input('请输入字体文件路径（或拖入文件）：\n')
		inf=ckfile(inf)
		if not os.path.isfile(inf):
			print('文件不存在，请重新选择！\n')
	while not outf.strip():
		outf=input('请输入输出文件：\n')
else:
	inf=sys.argv[1]
	outf=sys.argv[2]

print('正在载入字体...')
font=TTFont(inf)
print('正在更改字体...')
cfg=json.load(open(os.path.join(pydir, 'config.json'), 'r', encoding = 'utf-8'))
font['hhea'].ascender=cfg['ascender']
font['hhea'].descender=cfg['descender']
font['OS/2'].usWinAscent=cfg['usWinAscent']
font['OS/2'].usWinDescent=cfg['usWinDescent']
if "CFF " in font:
	font["CFF "].cff[0].FontBBox='0 -120 1000 880'
xMax=981
font['head'].xMax=xMax
font['hhea'].xMaxExtent=xMax
xAvgCharWidth=990
font['OS/2'].xAvgCharWidth=xAvgCharWidth

print('正在生成字体...')
font.save(outf)
print('完成!')
