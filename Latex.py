import os
import re
from PIL import Image

'''a4=(297mm,210)*0.9'''
a4ratio=float(297)/210

chapters=[]
with open('content.txt','r')as f:

    for line in f.readlines():
        chapter,*_=line.split('\t')
        if '武庚纪第二部' in chapter:
            chapters.append(chapter)

    for i in range(len(chapters)):
        chapter = chapters[len(chapters) - i - 1]
        newchapter = chapter.split()[0]
        output=''.join(chapter.split())
        output = open('tex/%s.tex'%output, 'w')
        # output.write('% !TEX program = XeLaTeX\n% !TEX encoding = UTF-8')
        output.write('''\\documentclass[hyperref, UTF8]{ctexart}\n''')
        # output.write('\\usepackage[unicode]{hyperref}\n')
        output.write('''\\usepackage{graphicx}\n
        \\usepackage{geometry}\n
        \\geometry{a4paper,scale=0.9}''')
        output.write('''\\begin{document}\n
        ''')
        output.write('\\tableofcontents\n')
        output.write('\\title{武庚纪}\n')

        output.write('''\\newpage\n
        \\section{%s} %s\n
        \\newpage\n'''%(chapter,chapter))
        with open(os.path.join('wugengji/'+chapter,'download.txt'),'r')as f2:
            for page in range(1,len(f2.readlines())+1):
                try:
                    img = Image.open(os.path.join('wugengji/'+chapter,'%s.eps'%page))
                #    img.save(os.path.join(chapter, '%s.eps' % page), 'EPS')
                except:
                    continue
#                output.write('\\subsection{%d}\n'%(page))

             #   output.write('\\subsection{%d}%d\n' % (page, page))
                #chapter=re.sub(' ','\ ',chapter)
                ratio=img.size[0]/img.size[1]
                if ratio>a4ratio:
                    scale=float(a4ratio)/ratio
                    output.write('''\\includegraphics[height=0.85
                    \\paperheight,scale=0.5]{%s.eps}\n
                    \\newpage\n'''%(os.path.join(newchapter,str(page))))
                else:
                    scale = float(ratio) / a4ratio
                    output.write('''\\includegraphics[width=0.85
                    \\paperwidth,scale=0.5]{%s.eps}\n
                    \\newpage\n''' % (os.path.join('/Users/ryan/PycharmProjects/comics/pdf/'+newchapter, str(page))))
        output.write('''\\end{document}''')
        output.close()