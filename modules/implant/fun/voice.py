import core.job
import core.implant
import uuid

class VoiceJob(core.job.Job):
    def done(self):
        self.display()

    def display(self):
        self.results = "Completed!"
        self.shell.print_plain(self.data)

class VoiceImplant(core.implant.Implant):

    NAME = "Voice"
    DESCRIPTION = "Makes the computer speak a message."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/fun/voice"

    def load(self):
        self.options.register("MESSAGE", "You are hacked!", "Message to speak.")

    def job(self):
        return VoiceJob

    def run(self):

        payloads = {}
        #payloads["vbs"] = self.load_script("data/implant/fun/voice.vbs", self.options)
        payloads["js"] = self.loader.load_script("data/implant/fun/voice.js", self.options)

        self.dispatch(payloads, self.job)
