#coding=utf-8
import Leap
import sys
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SampleListener(Leap.Listener):
    def on_connect(self, controller):
        #Before using gestures in your application, you must ensure that every gesture you want to use can be recognized.
        #You need to use the enableGesture() method in the Controller class to make the gestures you want to use recognized.
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()

        print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" \
              % ( frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

def main():
    # Create listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Add listener event to controller
    controller.add_listener(listener)

    # Remove listener at the end
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()