import Leap
import sys


class Leapmotionlistner(leap, listener):
    finger_name = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_name = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    def on_init(self, controller):
        print("Initialized")

    def on_connect(self, controller, TYPE_CIRCLE=None):
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
           pass

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