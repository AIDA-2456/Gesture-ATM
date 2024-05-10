from config import cfg


class DetectClick():

    def __init__(self, circleCenters):
        self.circleCenters = circleCenters


    def detectClick(self, fingertip):
        curPg = cfg["currentpage"]
        buttons = cfg["pages"][curPg]["buttons"]
        radius = cfg["btnparams"]["R"]

        # Check if finger print point resides in any of the eight circles of buttons.
        for i, button in enumerate(buttons):
            if button and button.strip():
                center_x = self.circleCenters[i][0]
                center_y = self.circleCenters[i][1]
                if ((fingertip[0] - center_x)**2 + (fingertip[1] - center_y)**2) < radius**2:
                    return i
