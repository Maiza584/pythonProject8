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
        frame = controller.frame()

        print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
            frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))
        #hands data
        for hand in frame.hands:
            handType = "Left hand" if hand.is_left else "Right hand"

            print "  %s, id %d, position: %s" % (
                handType, hand.id, hand.palm_position)

            normal = hand.palm_normal
            direction = hand.direction

            print "  pitch: %d degrees, roll: %d degrees, yaw: %d degrees" % (
                direction.pitch * Leap.RAD_TO_DEG,
                normal.roll * Leap.RAD_TO_DEG,
                direction.yaw * Leap.RAD_TO_DEG)

#fingers data
            for finger in hand.fingers:

                print "    %s finger, id: %d, length: %fmm, width: %fmm" % (
                    self.finger_names[finger.type],
                    finger.id,
                    finger.length,
                    finger.width)

#bones data
                for b in range(0, 4):
                    bone = finger.bone(b)
                    print "      Bone: %s, start: %s, end: %s, direction: %s" % (
                        self.bone_names[bone.type],
                        bone.prev_joint,
                        bone.next_joint,
                        bone.direction)


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