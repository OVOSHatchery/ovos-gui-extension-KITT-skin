from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.core import resting_screen_handler
from os.path import join, dirname


class KittSkinSkill(MycroftSkill):
    def initialize(self):
        self.register_gui_handlers()

    def register_gui_handlers(self):
        self.add_event('enclosure.mouth.think', self.handle_think)

        # speak animation
        self.add_event('recognizer_loop:audio_output_start',
                       self.handle_speak_start)
        self.add_event('recognizer_loop:audio_output_end',
                       self.handle_speak_end)

        # clear gui
        self.add_event("mycroft.skill.handler.complete",
                       self.idle)
        self.add_event('enclosure.mouth.reset',
                       self.handle_reset)

        # TODO: Register handlers for standard (Mark 1) events
        # self.bus.on('enclosure.eyes.on', self.on)
        # self.bus.on('enclosure.eyes.off', self.off)
        # self.bus.on('enclosure.eyes.blink', self.blink)
        # self.bus.on('enclosure.eyes.narrow', self.narrow)
        # self.bus.on('enclosure.eyes.look', self.look)
        # self.bus.on('enclosure.eyes.color', self.color)
        # self.bus.on('enclosure.eyes.level', self.brightness)
        # self.bus.on('enclosure.eyes.volume', self.volume)
        # self.bus.on('enclosure.eyes.spin', self.spin)
        # self.bus.on('enclosure.eyes.timedspin', self.timed_spin)
        # self.bus.on('enclosure.eyes.reset', self.reset)
        # self.bus.on('enclosure.eyes.setpixel', self.set_pixel)
        # self.bus.on('enclosure.eyes.fill', self.fill)

        # self.bus.on('enclosure.mouth.talk', self.talk)
        # self.bus.on('enclosure.mouth.listen', self.listen)
        # self.bus.on('enclosure.mouth.smile', self.smile)
        # self.bus.on('enclosure.mouth.viseme', self.viseme)

        # self.bus.on('recognizer_loop:record_begin', self.mouth.listen)
        # self.bus.on('recognizer_loop:record_end', self.mouth.reset)
        pass

    @resting_screen_handler("KITT")
    def idle(self, message=None):
        self.handle_think()

    def handle_speak_start(self, message=None):
        self.gui.show_animated_image(join(dirname(__file__),
                                          "ui", "speak.gif"),
                                     override_idle=True)

    def handle_speak_end(self, message=None):
        self.idle()

    def handle_reset(self, message=None):
        self.gui.clear()

    def handle_think(self, message=None):
        self.gui.show_animated_image(join(dirname(__file__),
                                          "ui", "think.gif"),
                                     override_idle=True)

    def stop(self):
        self.handle_reset()


def create_skill():
    return KittSkinSkill()

