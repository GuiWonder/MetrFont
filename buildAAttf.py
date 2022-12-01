import os
from shutil import copy, copytree, rmtree

os.system('chmod +x ./main/otfcc/*') 
os.makedirs('./src')
os.makedirs('./fonts')
os.system(f'wget -nc -P ./src https://github.com/GuiWonder/SourceHanToClassic/releases/download/1.010-ttf/AdvocateAncientSansTTFs.7z') 
os.system('7z x ./src/AdvocateAncientSansTTFs.7z -o./src')

fod='AdvocateAncientSans'
os.makedirs(f'./fonts/{fod}')
os.makedirs(f'./fonts/{fod}TC')
os.makedirs(f'./fonts/{fod}SC')
os.makedirs(f'./fonts/{fod}JP')
os.makedirs(f'./fonts/{fod}TTCs')
os.makedirs(f'./fonts/{fod}FANTI_TTFs')
copy('./main/LICENSE.txt', f'./fonts/{fod}/')
copy('./main/LICENSE.txt', f'./fonts/{fod}TC/')
copy('./main/LICENSE.txt', f'./fonts/{fod}SC/')
copy('./main/LICENSE.txt', f'./fonts/{fod}JP/')
copy('./main/LICENSE.txt', f'./fonts/{fod}TTCs/')
copy('./main/LICENSE.txt', f'./fonts/{fod}FANTI_TTFs/')

tocl='python3 ./main/metrfont.py'
tootc='python3 ./main/otf2otc.py -o'
for va in ('', 'TC', 'SC', 'JP', 'FANTI_TTFs'):
	for item in os.listdir(f'./src/{fod}{va}'):
		if item.lower().split('.')[-1] in ('otf', 'ttf'):
			os.system(f"{tocl} ./src/{fod}{va}/{item} ./fonts/{fod}{va}/{item}") 
for va in ('Bold', 'ExtraLight', 'Heavy', 'Light', 'Medium', 'Normal', 'Regular'):
	flst=[
		f'./fonts/{fod}/{fod}-{va}.ttf', 
		f'./fonts/{fod}TC/{fod}TC-{va}.ttf', 
		f'./fonts/{fod}SC/{fod}SC-{va}.ttf', 
		f'./fonts/{fod}JP/{fod}JP-{va}.ttf', 
		f'./fonts/{fod}FANTI_TTFs/{fod}ST-{va}.ttf', 
		f'./fonts/{fod}/{fod}HW-{va}.ttf', 
		f'./fonts/{fod}TC/{fod}HWTC-{va}.ttf', 
		f'./fonts/{fod}SC/{fod}HWSC-{va}.ttf', 
		f'./fonts/{fod}JP/{fod}HWJP-{va}.ttf', 
		f'./fonts/{fod}FANTI_TTFs/{fod}HWST-{va}.ttf', 
	]
	flsts=' '.join(flst)
	os.system(f"{tootc} ./fonts/{fod}TTCs/{fod}-{va}.ttc {flsts}") 

os.system(f'7z a {fod}TTCs.7z ./fonts/{fod}TTCs/*') 
os.system(f'7z a {fod}TTFs.7z ./fonts/{fod} ./fonts/{fod}TC ./fonts/{fod}SC ./fonts/{fod}JP -mx=9 -mfb=256 -md=256m')
