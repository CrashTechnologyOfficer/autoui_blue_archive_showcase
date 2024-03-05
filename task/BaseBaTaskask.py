from autoui.task.FindFeatureTask import FindFeatureTask
from scene.MainScene import MainScene


class BaseBaTask(FindFeatureTask):

    def go_back(self):
        self.send_key("KEYCODE_BACK")
        self.sleep(1)

    def go_home(self):
        return self.wait_scene(MainScene,
                               time_out=20,
                               pre_action=lambda: (self.sleep(1), self.send_key("KEYCODE_BACK"), self.sleep(1)))
