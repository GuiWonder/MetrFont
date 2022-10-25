import os, json, subprocess, platform, tempfile, gc, sys
from collections import defaultdict

pydir = os.path.abspath(os.path.dirname(__file__))
otfccdump = os.path.join(pydir, 'otfccdump')
otfccbuild = os.path.join(pydir, 'otfccbuild')
if platform.system() in ('Mac', 'Darwin'):
	otfccdump += '1'
	otfccbuild += '1'
if platform.system() == 'Linux':
	otfccdump += '2'
	otfccbuild += '2'

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
font = json.loads(subprocess.check_output((otfccdump, '--no-bom', inf)).decode("utf-8", "ignore"))
print('正在更改字体...')
cfg=json.load(open(os.path.join(pydir, 'config.json'), 'r', encoding = 'utf-8'))
font['hhea']['ascender']=cfg['ascender']
font['hhea']['descender']=cfg['descender']
font['OS_2']['usWinAscent']=cfg['usWinAscent']
font['OS_2']['usWinDescent']=cfg['usWinDescent']
if 'CFF_' in font:
	font['CFF_']['fontBBoxLeft']=0
	font['CFF_']['fontBBoxBottom']=-120
	font['CFF_']['fontBBoxRight']=1000
	font['CFF_']['fontBBoxTop']=880

xMax=981
font['head']['xMax']=xMax
font['hhea']['xMaxExtent']=xMax
xAvgCharWidth=990
font['OS_2']['xAvgCharWidth']=xAvgCharWidth


print('正在生成字体...')
tmpfile = tempfile.mktemp('.json')
with open(tmpfile, 'w', encoding='utf-8') as f:
	f.write(json.dumps(font))
for x in set(locals().keys()):
	if x not in ('os', 'subprocess', 'otfccbuild', 'outf', 'tmpfile', 'gc'):
		del locals()[x]
gc.collect()

subprocess.run((otfccbuild, '--keep-modified-time', '--keep-average-char-width', '-O3', '-q', '-o', outf, tmpfile))
os.remove(tmpfile)
print('完成!')
