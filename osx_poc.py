import keycode
import pygame
import Quartz
import sys
import time


def main():
    pygame.init()
    #pygame.joystick.init()

    print pygame.joystick.get_count()

    joy = pygame.joystick.Joystick(0)
    joy.init()
    print 'Init: %s' % (joy.get_init(),)
    print 'ID: %s' % (joy.get_id(),)
    print 'Name: %s' % (joy.get_name(),)
    print '# Axes: %s' % (joy.get_numaxes(),)
    print '# Balls: %s' % (joy.get_numballs(),)
    print '# Buttons: %s' % (joy.get_numbuttons(),)
    print '# Hats: %s' % (joy.get_numhats(),)
    down = {}
    axes = {}
    pygame.event.pump()
    for i in xrange(joy.get_numaxes()):
        axes[i] = joy.get_axis(i)
    while True:
        """
        print
        print joy.get_axis(0)
        print joy.get_axis(1)
        print joy.get_axis(2)
        print joy.get_axis(3)
        """
        for i in xrange(joy.get_numbuttons()):
            if joy.get_button(i) == 1:
                if not down.get(i, False):
                    print 'button %i: v' % (i,)

                    """
                    source = Quartz.CGEventSourceCreate(Quartz.kCGEventSourceStateCombinedSessionState)
                    saveCommandDown = Quartz.CGEventCreateKeyboardEvent(source, keycode.tokeycode('w'), True)
                    #Quartz.CGEventSetFlags(saveCommandDown, Quartz.kCGEventFlagMaskCommand)
                    saveCommandUp = Quartz.CGEventCreateKeyboardEvent(source, keycode.tokeycode('w'), False)

                    Quartz.CGEventPost(Quartz.kCGAnnotatedSessionEventTap, saveCommandDown)
                    Quartz.CGEventPost(Quartz.kCGAnnotatedSessionEventTap, saveCommandUp)
                    """

                    #Quartz.CFRelease(saveCommandUp)
                    #Quartz.CFRelease(saveCommandDown)
                    #Quartz.CFRelease(source)

                    #evt = Quartz.CGEventCreateKeyboardEvent(None, 125, True)
                    #evt = Quartz.CGEventCreateKeyboardEvent(None, 125, False)
                    #evt = Quartz.CGEventCreateKeyboardEvent(None, 32, True)
                    #evt = Quartz.CGEventCreateKeyboardEvent(None, 32, False)
                    down[i] = True
                    #import ipdb; ipdb.set_trace()
            else:
                if down.get(i, False):
                    print 'button %i: ^' % (i,)
                    down[i] = False

            for i in xrange(joy.get_numaxes()):
                val = joy.get_axis(i)
                if abs(val - axes.get(i, 0)) > 0.1:
                    axes[i] = val
                    print 'axis %i: %f' % (i, val)

        pygame.event.pump()
        time.sleep(0.01)
        #sys.exit()

if __name__ == '__main__':
    main()
