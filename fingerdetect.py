from sklearn.preprocessing import data
from pandas.core import frame
import Leap



def on_frame(self, controller, fingers, hand):
   # Get the most recent frame and report some basic information
   frame = controller.frame()
   data = frame # see if data array gets filled up?
   import Leap, sys, thread, time

   from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
   import csv

   data = {
'id':345345123,
    'timestamp':0,
    'hands':1,
    'hand':1,
    'fingers':2,
    'tool':False,
    'numfingers':2,
    'finger1pos':(0.0,0.0,0.0),
    'finger2pos':(0.0,0.0,0.0),
    'finger3pos':(0.0,0.0,0.0),
    'finger4pos':(0.0,0.0,0.0),
    'finger5pos':(0.0,0.0,0.0),  # if you need all ten, just add to list
    'avg_pos':(234.33,345.33,123.54), # This is partial of total lines.
   }
 # Check if the hand has any fingers
def hand():


    fingers= hand.fingers
    def finger():
        if not finger.is_empty:
        	fingertip_position_table = []
            # Calculate the hand's average finger tip position
avg_pos = Leap.Vector
pos = Leap.Vector
pos = Leap.Vector
           	#try:
for finger in frame.fingers:
                #print("132 -fingertip_position",(finger.tip_position.x,finger.tip_position.y,finger.tip_position.z))  # no quotes

                #posi = frame.finger.tip_position
                posi = Leap.Vector(finger.tip_position.x,finger.tip_position.y,finger.tip_position.z)
                pos += posi
                #fingertip_position_table +=  posi
                fingertip_position_table.append(("%f, %f, %f" % (finger.tip_position.x,finger.tip_position.y,finger.tip_position.z)))
            #except:
            #print("123 - EXCEPTION - SKIPPING")

avg_pos = pos.__div__(len(frame.fingers))
            #print("133 - Length of fingertip_position_table:",len(fingertip_position_table))

x = 0
for finger in fingertip_position_table:         #frame.fingers:  # gives "Finger ID:nn"
                try:
                    x = x + 1
                    #print("139 - Working on finger",x)
                    if x == 1:
                        d2 = {
                        'finger1pos':str("%s" % (finger))
                        }
                        #print("143 - finger 1 position:",d2)
                        data.update(d2)
                        pass
                    if x == 2:
                        d2 = {
                        'finger2pos':str("%s" % (finger))
                        }
                        #print("149 - finger 2 position:",d2)
                        data.update(d2)
                        pass
                    if x == 3:
                        d2 = {
                        'finger3pos':str("%s" % (finger))
                        }
                        #print("155 - finger 3 position:",d2)
                        data.update(d2)
                        pass
                    if x == 4:
                        d2 = {
                        'finger4pos':str("%s" % (finger))
                        }
                        #print("160 - finger 4 position:",d2)
                        data.update(d2)
                        pass
                    if x == 5:
                        d2 = {
                        'finger5pos':str("%s" % (finger))
                        }
                        #print("167 - finger 5 position:",d2)
                        data.update(d2)
                        pass
                    if x == 6:
                        d2 = {
                        'finger6pos':str("%s" % (finger))
                        }
                        #print("173 - finger 6 position:",d2)
                        data.update(d2)
                        pass
                    if x == 7:
                        d2 = {
                        'finger7pos':str("%s" % (finger))
                        }
                        #print("179 - finger 7 position:",d2)
                        data.update(d2)
                        pass
                    if x == 8:
                        d2 = {
                        'finger8pos':str("%s" % (finger))
                        }
                        #print("185 - finger 8 position:",d2)
                        data.update(d2)
                        pass
                    if x == 9:
                        d2 = {
                        'finger9pos':str("%s" % (finger))
                        }
                        #print("191 - finger 9 position:",d2)
                        data.update(d2)
                        pass
                    if x == 10:
                        d2 = {
                        'finger10pos':str("%s" % (finger))
                        }
                        #print("197 - finger 10 position:",d2)
                        data.update(d2)
                        pass

                except:
                    print("163 - EXCEPTION ERROR - SKIPPING",x)
                    pass


last_finger_one = Leap.Vector
last_finger_two = Leap.Vector
