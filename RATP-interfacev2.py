"""RATP-interfacev2.py: Makes a web interface for RATP_Watch. This is the file you want to run."""

__author__      = "Adrien Le Falher"

from threading import Timer
import RATP_Watch
import remi.gui as gui
from remi import start, App



refresh_rate = 30

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):

        container = gui.VBox(width = 480, height = 320, layout_orientation=gui.Widget.LAYOUT_VERTICAL)

        # ---------- LIGNE 12 ----------------
        container_ligne1 = gui.Widget(width='100%', layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, margin='0px', style={'display': 'flex', 'overflow': 'visible'}, )
        info_ligne1 = gui.Widget(width='80%', layout_orientation=gui.Widget.LAYOUT_VERTICAL, margin='12px',
                                      style={'display': 'block', 'overflow': 'visible'})
        self.logo = gui.Image('https://www.ratp.fr/sites/default/files/network/metro/ligne12.svg', width="100px", height="50px", margin="10px")

        next_bus, last_bus, updated = RATP_Watch.get_12_convention()

        self.nextbus12 = gui.Label(next_bus)
        self.lastbus12 = gui.Label(last_bus)

        container.append(container_ligne1)


        container_ligne1.append(self.logo)


        container_ligne1.append(info_ligne1)
        info_ligne1.append(self.nextbus12)
        info_ligne1.append(self.lastbus12)

        # ------------------- BUS 95 ---------------


        container_ligne3 = gui.Widget(width='100%', layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, margin='0px',
                                      style={'display': 'flex', 'overflow': 'visible'}, )
        info_ligne3 = gui.Widget(width='80%', layout_orientation=gui.Widget.LAYOUT_VERTICAL, margin='12px',
                                 style={'display': 'block', 'overflow': 'visible'})
        self.logo = gui.Image('https://www.ratp.fr/sites/default/files/network/bus/ligne95.svg', width="100px",
                              height="60px", margin="10px")

        next_bus, last_bus, updated = RATP_Watch.get_95_morillons()

        self.nextbus95 = gui.Label(next_bus)
        self.lastbus95 = gui.Label(last_bus)

        container.append(container_ligne3)

        container_ligne3.append(self.logo)

        container_ligne3.append(info_ligne3)
        info_ligne3.append(self.nextbus95)
        info_ligne3.append(self.lastbus95)

        # ------------------------- BUS 89 --------------
        "https://www.ratp.fr/sites/default/files/network/bus/ligne89.svg"

        container_ligne4 = gui.Widget(width='100%', layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, margin='0px',
                                      style={'display': 'flex', 'overflow': 'visible'}, )
        info_ligne4 = gui.Widget(width='80%', layout_orientation=gui.Widget.LAYOUT_VERTICAL, margin='12px',
                                 style={'display': 'block', 'overflow': 'visible'})
        self.logo = gui.Image('https://www.ratp.fr/sites/default/files/network/bus/ligne89.svg', width="100px",
                              height="60px", margin="10px")

        next_bus, last_bus, updated = RATP_Watch.get_89_brancion_vouille()

        self.nextbus89 = gui.Label(next_bus)
        self.lastbus89 = gui.Label(last_bus)

        container.append(container_ligne4)

        container_ligne4.append(self.logo)

        container_ligne4.append(info_ligne4)
        info_ligne4.append(self.nextbus89)
        info_ligne4.append(self.lastbus89)

        # ---------- BUS 62 -------------
        "https://www.ratp.fr/sites/default/files/network/bus/ligne62.svg"

        container_ligne2 = gui.Widget(width='100%', layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, margin='0px',
                                      style={'display': 'flex', 'overflow': 'visible'}, )
        info_ligne2 = gui.Widget(width='80%', layout_orientation=gui.Widget.LAYOUT_VERTICAL, margin='12px',
                                 style={'display': 'block', 'overflow': 'visible'})
        self.logo = gui.Image('https://www.ratp.fr/sites/default/files/network/bus/ligne62.svg', width="100px",
                              height="60px", margin="10px")

        next_bus, last_bus, updated = RATP_Watch.get_62_brancion_vouille()

        self.nextbus62 = gui.Label(next_bus)
        self.lastbus62 = gui.Label(last_bus)

        container.append(container_ligne2)

        container_ligne2.append(self.logo)

        container_ligne2.append(info_ligne2)
        info_ligne2.append(self.nextbus62)
        info_ligne2.append(self.lastbus62)


        # -------- VELIB --------------

        container_ligne5 = gui.Widget(width='100%', layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, margin='0px',
                                      style={'display': 'flex', 'overflow': 'visible'}, )
        info_ligne5 = gui.Widget(width='80%', layout_orientation=gui.Widget.LAYOUT_VERTICAL, margin='12px',
                                 style={'display': 'block', 'overflow': 'visible'})
        self.logo = gui.Image('http://www.orchestredeparis.com/assets/img/content/practical/howto/velib.svg', width="100px",
                              height="60px", margin="10px")

        bike, ebike = RATP_Watch.get_velib()

        velo = str(bike) + ' ' + "vélo disponible"
        electrique = str(ebike) + " " + "ebike disponible"

        self.nextbus_velib = gui.Label(velo, margin="0px")
        self.lastbus_velib = gui.Label(electrique, margin="00px")

        container.append(container_ligne5)

        container_ligne5.append(self.logo)

        container_ligne5.append(info_ligne5)
        info_ligne5.append(self.nextbus_velib)
        info_ligne5.append(self.lastbus_velib)


        self.update12()
        self.update62()
        self.update89()
        self.update95()
        self.update_velib()

        return container



    def update12(self):
        global refresh_rate
        next_bus, last_bus, updated = RATP_Watch.get_12_convention()
        self.nextbus12.set_text(next_bus)
        self.lastbus12.set_text(last_bus)
        Timer(refresh_rate, self.update12).start()
    def update95(self):
        global refresh_rate
        next_bus, last_bus, updated = RATP_Watch.get_95_morillons()
        self.nextbus95.set_text(next_bus)
        self.lastbus95.set_text(last_bus)
        Timer(refresh_rate, self.update95).start()

    def update62(self):
        global refresh_rate
        next_bus, last_bus, updated = RATP_Watch.get_62_brancion_vouille()
        self.nextbus62.set_text(next_bus)
        self.lastbus62.set_text(last_bus)
        Timer(refresh_rate, self.update62).start()
    def update89(self):
        global refresh_rate
        next_bus, last_bus, updated = RATP_Watch.get_89_brancion_vouille()
        self.nextbus89.set_text(next_bus)
        self.lastbus89.set_text(last_bus)
        Timer(refresh_rate, self.update89).start()
    def update_velib(self):
        global refresh_rate
        next_bus, last_bus = RATP_Watch.get_velib()
        self.nextbus_velib.set_text(next_bus)
        self.lastbus_velib.set_text(last_bus)
        Timer(refresh_rate, self.update_velib).start()




# starts the webserver
start(MyApp)
