import xml.etree.ElementTree as ET
tree=ET.parse('Task.xml')
root= tree.getroot()
pagename=raw_input()
fr=raw_input()
for elem in root: 
    for Page in root.iter('Page'):
        name=Page.get('name')
        for step in Page.iter('step'):
            pose=step.get('pose')
            frame=step.get('frame')
            p1=pose.split(" ")
            if name==pagename:
                if(frame==fr):
                    for i in xrange(len(p1)):
                        print p1[i]

            