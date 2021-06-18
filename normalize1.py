import pandas
import scipy
import numpy
from sklearn.preprocessing import MinMaxScaler
import Leap
import sys


class Leapmotionlistner(Leap.Listener):
    finger_name = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_name = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    def on_init(self, controller):
        print("Initialized")

    def on_connect(self, controller):
        print("Motion Sensor Connected!")

        controller.enable_gesture(Leap.Gesture,TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture, TYPE_KRY_TAP);
        controller.enable_gesture(Leap.Gesture, TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture, TYPE_SMIPE);

        def on_disconnect(self, controller):
            print("Motion Sensor Disconnected!")

        def on_exit(self, controller):
            print("Exited")

        def on_frame(self, controller):
#frame_data
           frame = controller.frame()
           print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
               frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

        #   print "Frame ID:" + str(frame.id)\
        #  +"Timestamp:" + str(frame.timestamp)\
        #   +"# of Hands" + str(len(frame.hands)) \
        #  + "# of Fingers" + str(len(frame.fingers))
        #  +"# of Tools" + str(len(frame.tools)) \
        # + "# of Gestures" + str(len(frame.gestures()))
def main():
            listener = Leapmotionlistner()
            controller = Leap.Controller()

            controller.add_listener(listener)
            print("press enter to quit")
            try:
                sys.stdin.readline()
            except KeyboardInterrupt:
                pass
            finally:
                controller.remove_listener(listener)
            if _name_ =="_main_":
                main()
names = ['frame']
dataframe = pandas.read_csv(url, names=frame)
array = dataframe.values
# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)
# summarize transformed data
numpy.set_printoptions(precision=3)
print(rescaledX[0:5,:])