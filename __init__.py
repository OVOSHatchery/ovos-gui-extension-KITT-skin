from os.path import join, dirname

from ovos_workshop.decorators import resting_screen_handler
from ovos_workshop.skills import OVOSSkill


class KittSkinSkill(OVOSSkill):

    def initialize(self):
        self.gui_busy = False
        self.register_gui_handlers()

    def handle_gui_status(self, message):
        # detect if some other skill is displaying stuff
        if 'KITT-skin' not in message.data.get('__from', ''):
            self.gui_busy = True

    def register_gui_handlers(self):
        self.add_event('gui.page.show', self.handle_gui_status)

        self.add_event('recognizer_loop:audio_output_start',
                       self.handle_speak_start)
        self.add_event('recognizer_loop:record_begin', self.handle_listen)

        self.add_event('recognizer_loop:audio_output_end', self.handle_idle)
        self.add_event('recognizer_loop:record_end', self.handle_idle)
        self.add_event("mycroft.skill.handler.complete", self.handle_idle)

        # TODO: Register handlers for standard (Mark 1) events
        # self.add_event('enclosure.eyes.on', self.on)
        # self.add_event('enclosure.eyes.off', self.off)
        # self.add_event('enclosure.eyes.blink', self.blink)
        # self.add_event('enclosure.eyes.narrow', self.narrow)
        # self.add_event('enclosure.eyes.look', self.look)
        # self.add_event('enclosure.eyes.color', self.color)
        # self.add_event('enclosure.eyes.level', self.brightness)
        # self.add_event('enclosure.eyes.volume', self.volume)
        # self.add_event('enclosure.eyes.spin', self.spin)
        # self.add_event('enclosure.eyes.timedspin', self.timed_spin)
        # self.add_event('enclosure.eyes.reset', self.reset)
        # self.add_event('enclosure.eyes.setpixel', self.set_pixel)
        # self.add_event('enclosure.eyes.fill', self.fill)

        # self.add_event('enclosure.mouth.smile', self.smile)
        # self.add_event('enclosure.mouth.viseme', self.viseme)
        self.add_event('enclosure.mouth.reset', self.handle_reset)
        self.add_event('enclosure.mouth.think', self.handle_think)
        self.add_event('enclosure.mouth.talk', self.handle_speak_start)
        self.add_event('enclosure.mouth.listen', self.handle_listen)

    @resting_screen_handler("KITT")
    def idle(self, message=None):
        self.gui_busy = False
        self.gui.clear()
        self.gui.show_animated_image(join(dirname(__file__), "ui", "idle.gif"),
                                     override_idle=True)

    def handle_speak_start(self, message=None):
        if self.gui_busy:
            return
        self.gui.show_animated_image(join(dirname(__file__), "ui",
                                          "speak.gif"),
                                     override_idle=True)

    def handle_idle(self, message=None):
        if self.gui_busy:
            return
        self.idle()

    def handle_reset(self, message=None):
        self.gui.clear()
        self.gui_busy = False

    def handle_listen(self):
        self.handle_reset()
        self.gui.show_animated_image(join(dirname(__file__), "ui",
                                          "listening.gif"),
                                     override_idle=True)

    def handle_think(self, message=None):
        self.gui.show_animated_image(join(dirname(__file__), "ui",
                                          "think.gif"),
                                     override_idle=True)

    def stop(self):
        self.idle()
