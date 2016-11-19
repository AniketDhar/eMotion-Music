import os;
import easygui
def runner():
	os.system('cheese');
	return;
	
y=int(easygui.ynbox('Allow permission to launch webcam?', 'Title', ('Yes', 'No')))
if y==1:
	z=0
	while z==0:
		runner()
		z=int(easygui.ynbox('Are you happy with the picture?', 'Title', ('Yes', 'No')))
else:
	easygui.msgbox('Hey! chill, don\'t sweat it', 'It \' Ok')
	
	
	
