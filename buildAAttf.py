import os
from shutil import copy, copytree, rmtree

os.system('chmod +x ./main/otfcc/*') 
os.makedirs('./src')
os.makedirs('./fonts')
os.system(f'wget -nc -P ./src https://github.com/GuiWonder/SourceHanToClassic/releases/download/test-ttfh-1.008/AdvocateAncientSansTTFs.7z') 
os.system(f'wget -nc -P ./src https://github.com/GuiWonder/SourceHanToClassic/releases/download/test-ttfh-1.008/AdvocateAncientSansFANTI.7z') 
os.system('7z x ./src/AdvocateAncientSansTTFs.7z -o./src')
os.system('7z x ./src/AdvocateAncientSansFANTI.7z -o./src')

fod='AdvocateAncientSans'
os.makedirs(f'./fonts/{fod}')
os.makedirs(f'./fonts/{fod}TC')
os.makedirs(f'./fonts/{fod}SC')
os.makedirs(f'./fonts/{fod}JP')
os.makedirs(f'./fonts/{fod}OTCs')
os.makedirs(f'./fonts/{fod}ST')
copy('./main/LICENSE.txt', f'./fonts/{fod}/')
copy('./main/LICENSE.txt', f'./fonts/{fod}TC/')
copy('./main/LICENSE.txt', f'./fonts/{fod}SC/')
copy('./main/LICENSE.txt', f'./fonts/{fod}JP/')
copy('./main/LICENSE.txt', f'./fonts/{fod}OTCs/')
copy('./main/LICENSE.txt', f'./fonts/{fod}ST/')

tocl='python3 ./main/metrfont.py'
tootc='python3 ./main/otf2otc.py -o'
for va in ('', 'TC', 'SC', 'JP'):
	for item in os.listdir(f'./src/{fod}{va}'):
		if item.lower().split('.')[-1] in ('otf', 'ttf'):
			os.system(f"{tocl} ./src/{fod}{va}/{item} ./fonts/{fod}{va}/{item}") 
for item in os.listdir(f'./src'):
	if item.lower().split('.')[-1] in ('otf', 'ttf'):
		os.system(f"{tocl} ./src/{item} ./fonts/{fod}ST/{item}")
for va in ('Bold', 'ExtraLight', 'Heavy', 'Light', 'Medium', 'Normal', 'Regular'):
	os.system(f"{tootc} ./fonts/{fod}OTCs/{fod}-{va}.ttc ./fonts/{fod}/{fod}-{va}.ttf ./fonts/{fod}TC/{fod}TC-{va}.ttf ./fonts/{fod}SC/{fod}SC-{va}.ttf ./fonts/{fod}JP/{fod}JP-{va}.ttf") 

os.system(f'7z a {fod}OTCs.7z ./fonts/{fod}OTCs/*') 
os.system(f'7z a {fod}OTFs.7z ./fonts/{fod} ./fonts/{fod}TC ./fonts/{fod}SC ./fonts/{fod}JP -mx=9 -mfb=256 -md=256m')
os.system(f'7z a {fod}FANTI.7z ./fonts/{fod}ST/*') 
