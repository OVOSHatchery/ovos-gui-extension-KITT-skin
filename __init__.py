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
        self.add_event('enclosure.mouth.talk', self.handle_speak_start)
        self.add_event('recognizer_loop:audio_output_end',
                       self.handle_reset)

        # listen
        self.add_event('recognizer_loop:record_begin', self.handle_listen)
        self.add_event('enclosure.mouth.listen', self.handle_listen)
        self.add_event('recognizer_loop:record_end', self.handle_reset)

        # clear gui
        self.add_event("mycroft.skill.handler.complete",
                       self.idle)
        self.add_event('enclosure.mouth.reset',
                       self.handle_reset)

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

    @resting_screen_handler("KITT")
    def idle(self, message=None):
        # TODO blacklist mark2 skill since it conflicts
        self.gui.show_animated_image(join(dirname(__file__),
                                          "ui", "idle.gif"),
                                     override_idle=True)

    def handle_speak_start(self, message=None):
        self.gui.show_animated_image(join(dirname(__file__),
                                          "ui", "speak.gif"),
                                     override_idle=True)

    def handle_reset(self, message=None):
        self.gui.clear()

    def handle_listen(self):
        self.gui.show_animated_image(join(dirname(__file__),
                                          "ui", "listening.gif"),
                                     override_idle=True)

    def handle_think(self, message=None):
        self.gui.show_animated_image(join(dirname(__file__),
                                          "ui", "think.gif"),
                                     override_idle=True)

    def stop(self):
        self.handle_reset()


def create_skill():
    return KittSkinSkill()

