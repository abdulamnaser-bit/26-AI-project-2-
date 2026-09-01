import sys
import math
import random
import psutil
import numpy as np

from datetime import datetime

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
)

from PyQt6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QFont,
)

from PyQt6.QtCore import (
    Qt,
    QTimer,
    QRect,
)



class FridayUI(QWidget):

    def __init__(self):

        super().__init__()

        self.rotation_speed = 2

        self.core_red = 15
        self.core_green = 53
        self.core_blue = 82

        self.glow_alpha = 30

        self.angle = 0
        self.radius = 100
        self.grow = True

        self.wave_offset = 0

        self.mic_level = 0

        self.init_ui()

        QTimer.singleShot(
            100,
            self.center_boot_label
        )

        self.core_color = QColor("#072B44")
        self.glow_color = QColor("#0A4A6E")

        self.update_state(
            "Sleeping..."
        )

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate_core)
        self.timer.start(40)

        self.rotation_timer = QTimer()
        self.rotation_timer.timeout.connect(
            self.rotate_ring
        )
        self.rotation_timer.start(30)

        self.wave_timer = QTimer()
        self.wave_timer.timeout.connect(
            self.animate_wave
        )
        self.wave_timer.start(30)

        self.scanner_angle = 0

        self.clock_timer = QTimer()

        self.clock_timer.timeout.connect(
            self.update_clock
        )

        self.clock_timer.start(1000)

        self.stats_timer = QTimer()

        self.stats_timer.timeout.connect(
            self.update_system_stats
        )

        self.stats_timer.start(1000)

        self.boot_messages = [
            "INITIALIZING...",
            "LOADING MEMORY...",
            "CONNECTING MODULES...",
            "FRIDAY ONLINE"
        ]

        self.boot_index = 0

        self.boot_timer = QTimer()

        self.boot_timer.timeout.connect(
            self.boot_sequence
        )

        self.boot_timer.start(1500)


    def init_ui(self):

        self.boot_label = QLabel(self)

        self.boot_label.resize(
            2400,
            500
        )

        self.boot_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.boot_label.setStyleSheet(
            "color:#00D4FF;"
        )

        self.boot_label.setFont(
            QFont(
                "Orbitron",
                18
            )
        )

        self.time_label = QLabel(self)

        self.time_label.setGeometry(
            40,
            40,
            250,
            50
        )

        self.time_label.setStyleSheet(
            "color:#00D4FF;"
        )

        self.time_label.setFont(
            QFont(
                "Orbitron",
                18
            )
        )

        self.state = "sleeping..."

        self.inner_angle = 360

        self.setWindowTitle("FRIDAY")

        self.setGeometry(
            300,
            100,
            1200,
            850
        )

        self.setStyleSheet(
            "background-color:#050505;"
        )

        self.status_label = QLabel(
            "Sleeping...",
            self
        )

        self.status_label.setGeometry(
            930,
            200,
            220,
            40
        )

        self.status_label.setStyleSheet("""
            color:#00D4FF;
            font-family: Orbitron;
            font-size:14px;
            font-weight:bold;
        """)

        

        self.status_label.setFont(
            QFont(
                "Orbitron",
                16
            )
        )

        self.cpu_label = QLabel(self)

        self.cpu_label.setGeometry(
            40,
            100,
            250,
            40
        )

        self.cpu_label.setStyleSheet(
            "color:#00D4FF;"
        )

        self.cpu_label.setFont(
            QFont(
                "Orbitron",
                12
            )
        )

        self.ram_label = QLabel(self)

        self.ram_label.setGeometry(
            40,
            140,
            250,
            40
        )

        self.ram_label.setStyleSheet(
            "color:#00D4FF;"
        )

        self.ram_label.setFont(
            QFont(
                "Orbitron",
                12
            )
        )

        self.system_label = QLabel(self)

        self.system_label.setGeometry(
            930,
            40,
            220,
            160
        )

        self.system_label.setStyleSheet(
            """
            color:#00D4FF;
            """
        )

        self.system_label.setFont(
            QFont(
                "Orbitron",
                10
            )
        )

        self.wave_values = [
            10,20,30,15,40,25,35,
            20,45,15,30,20
        ]

        self.update_clock()

        self.update_system_stats()

        self.command_label = QLabel(self)

        self.command_label.setGeometry(
            300,
            650,
            600,
            140
        )

        self.command_label.setWordWrap(True)

        self.command_label.setStyleSheet(
            """
            color:#00D4FF;
            """
        )

        self.command_label.setFont(
            QFont(
                "Orbitron",
                10
            )
        )

        self.update_system_panel()


    def update_state(self, state):

        state = state.strip()
          
        self.state = state

        self.status_label.setText(state)

        if state == "Sleeping...":

            self.status_label.setStyleSheet(
                "color:#00A8FF;"
            )

        elif state == "Listening...":

            self.status_label.setStyleSheet(
                "color:#00FFFF;"
            )

        elif state == "Thinking...":

            self.status_label.setStyleSheet(
                "color:#66CCFF;"
            )

        elif state == "Speaking...":

            self.status_label.setStyleSheet(
                "color:#66E7FF;"
            )

        print("STATE =", state)

        if "Sleeping..." in state:

            self.core_color = QColor("#072B44")
            self.glow_color = QColor("#0A4A6E")

        elif "Listening..." in state:

            self.core_color = QColor("#062930")
            self.glow_color = QColor("#31545A")

        elif "Thinking..." in state:

            self.core_color = QColor("#1E90FF")
            self.glow_color = QColor("#66CCFF")

        elif "Speaking..." in state:

            self.core_color = QColor("#215F74")
            self.glow_color = QColor("#226064")

        if "Speaking..." in state:

            self.rotation_speed = 8

        elif "Thinking..." in state:

            self.rotation_speed = 4

        else:

            self.rotation_speed = 2

        if "Sleeping..." in state:

            self.rotation_speed = 2

            self.core_red = 15
            self.core_green = 53
            self.core_blue = 82

            self.glow_alpha = 30

        elif "Listening..." in state:

            self.rotation_speed = 8

            self.core_red = 0
            self.core_green = 212
            self.core_blue = 255

            self.glow_alpha = 80

        elif "Thinking..." in state:

            self.rotation_speed = 12

            self.core_red = 0
            self.core_green = 180
            self.core_blue = 255

            self.glow_alpha = 120

        elif "Speaking..." in state:

            self.rotation_speed = 6

            self.core_red = 0
            self.core_green = 255
            self.core_blue = 255

            self.glow_alpha = 100

        self.update()

        self.update_system_panel()


    def animate_core(self):

        limit = 100

        if self.state == "Speaking...":
            limit = 115

        elif self.state == "Thinking...":
            limit = 105

        if self.grow:

            self.radius += 1

            if self.radius >= limit:
                self.grow = False

        else:

            self.radius -= 1

            if self.radius <= 90:
                self.grow = True

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        center_x = self.width() // 2
        center_y = self.height() // 2

        # ==================================
        # OUTER STATIC RING
        # ==================================

        pen = QPen(
            QColor("#0A4A6B"),
            2
        )

        painter.setPen(pen)

        painter.drawEllipse(
            center_x - 160,
            center_y - 160,
            320,
            320
        )

        if self.state == "Speaking...":

            glow_pen = QPen(
                QColor("#66CCFF")
            )

            glow_pen.setWidth(10)

            painter.setPen(glow_pen)

            painter.drawEllipse(
                center_x - 150,
                center_y - 150,
                300,
                300
            )

        # ==================================
        # OUTER GLOW ARC
        # ==================================

        glow_pen = QPen(
            QColor(0, 191, 255, 40),
            16
        )

        painter.setPen(glow_pen)

        painter.drawArc(
            center_x - 160,
            center_y - 160,
            320,
            320,
            self.angle * 16,
            120 * 16
        )

        # ==================================
        # OUTER ARC
        # ==================================

        arc_pen = QPen(
            QColor("#00BFFF"),
            6
        )

        painter.setPen(arc_pen)

        painter.drawArc(
            center_x - 160,
            center_y - 160,
            320,
            320,
            self.angle * 16,
            120 * 16
        )

        # ==================================
        # SECOND ROTATING RING
        # ==================================

        second_pen = QPen(
            QColor("#66E0FF"),
            3
        )

        painter.setPen(second_pen)

        painter.drawArc(
            center_x - 130,
            center_y - 130,
            260,
            260,
            -self.angle * 16,
            80 * 16
        )

        # ==================================
        # INNER STATIC RING
        # ==================================

        inner_pen = QPen(
            QColor("#00D4FF"),
            2
        )

        painter.setPen(inner_pen)

        painter.drawEllipse(
            center_x - 115,
            center_y - 115,
            230,
            230
        )

        inner_pen = QPen(
            QColor("#7FE8FF")
        )

        inner_pen.setWidth(4)

        painter.setPen(inner_pen)

        painter.drawArc(
            center_x - 125,
            center_y - 125,
            250,
            250,
            self.inner_angle * 16,
            70 * 16
        )

        # Glow Layer 1

        painter.setPen(Qt.PenStyle.NoPen)

        painter.setBrush(
            QColor(
                self.core_red,
                self.core_green,
                self.core_blue,
                25
            )
        )

        painter.drawEllipse(
            center_x - self.radius - 35,
            center_y - self.radius - 35,
            (self.radius + 35) * 2,
            (self.radius + 35) * 2
        )

        # Glow Layer 2
        
        painter.setBrush(
            QColor(
                self.core_red,
                self.core_green,
                self.core_blue,
                50
            )
        )
        
        painter.drawEllipse(
            center_x - self.radius - 20,
            center_y - self.radius - 20,
            (self.radius + 20) * 2,
            (self.radius + 20) * 2
        )

        # Glow Halo

        painter.setBrush(
            QColor(
                self.core_red,
                self.core_green,
                self.core_blue,
                self.glow_alpha
            )
        )

        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(
            center_x - 125,
            center_y - 125,
            250,
            250
        )

        painter.setBrush(
            Qt.BrushStyle.NoBrush
        )
 
        # ==================================
        # CORE
        # ==================================

        
        painter.setBrush(
            self.core_color
        )

        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(
            center_x - self.radius,
            center_y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

        glow_pen = QPen(
            self.glow_color
        )

        glow_pen.setWidth(10)

        painter.setPen(glow_pen)

        painter.drawEllipse(
            center_x - self.radius - 8,
            center_y - self.radius - 8,
            (self.radius * 2) + 16,
            (self.radius * 2) + 16
        )

        # ==================================
        # TEXT
        # ==================================

        painter.setPen(
            QColor("#EAFBFF")
        )

        font = QFont(
                    "Orbitron",
                24
            )
        
        font.setLetterSpacing(
            QFont.SpacingType.AbsoluteSpacing,
            8
        )

        painter.setFont(font)

        text_rect = QRect(
        center_x - 120,
        center_y - 25,
        240,
        50
        )

        painter.drawText(
            text_rect,
            Qt.AlignmentFlag.AlignCenter,
            "FRIDAY"
        )

        # ==================================
        # VOICE WAVE
        # ==================================

        bar_width = 15
        spacing = 12

        start_x = center_x - 68
        base_y = center_y + 240

        wave_pen = QPen(
            QColor("#00D4FF")
        )

        wave_pen.setWidth(4)

        painter.setPen(wave_pen)

        for i, h in enumerate(self.wave_values):

            x = start_x + i * spacing

            painter.drawLine(
                x,
                base_y - h,
                x,
                base_y + h
            )
        

    def animate_wave(self):

        if self.state == "Sleeping...":

            minimum = 2
            maximum = 5

        elif self.state == "Listening...":

            minimum = 8
            maximum = 18

        elif self.state == "Thinking...":

            minimum = 20
            maximum = 50

        elif self.state == "Speaking...":

            minimum = 15
            maximum = 35

        else:

            minimum = 5
            maximum = 15

        self.wave_values = [
            random.randint(minimum, maximum)
            for _ in range(12)
        ]

        self.update()

    def update_clock(self):

        now = datetime.now()

        self.time_label.setText(
            now.strftime("%H:%M:%S")
        )

    def update_system_panel(self):

        self.system_label.setText(

            f"STATUS\n"
            f"{self.state}\n\n"

            f"VOICE\n"
            f"ONLINE\n\n"

            f"MEMORY\n"
            f"CONNECTED"

        )

    def update_system_stats(self):

        cpu = psutil.cpu_percent()

        ram = psutil.virtual_memory().percent

        self.cpu_label.setText(
            f"CPU : {cpu}%"
        )

        self.ram_label.setText(
            f"RAM : {ram}%"
        )

    def update_command_history(
        self,
        boss_text,
        friday_text
    ):

        self.command_label.setText(

            f"Boss:\n{boss_text}\n\n"
            f"Friday:\n{friday_text}"

        )

    def center_boot_label(self):

        self.boot_label.move(
            self.width() // 2 - self.boot_label.width() // 2,
            self.height() // 2 - self.boot_label.height() // 2
        )

    def boot_sequence(self):

        if self.boot_index < len(
            self.boot_messages
        ):

            self.boot_label.setText(
                self.boot_messages[
                    self.boot_index
                ]
            )

            self.boot_index += 1

        else:

            self.boot_timer.stop()

            self.boot_label.hide()

    def update_mic_level(self, audio_data):

        volume = np.abs(audio_data).mean()

        self.mic_level = min(
            int(volume / 100),
            100
        )
    

    def rotate_ring(self):

        self.angle += self.rotation_speed

        if self.angle >= 360:
            self.angle = 0

        self.inner_angle -= 3

        if self.inner_angle <= 0:
            self.inner_angle = 360

        self.scanner_angle += 4

        if self.scanner_angle >= 360:
            self.scanner_angle = 0

        self.update()

    def closeEvent(self, event):

        QApplication.quit()

        event.accept()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = FridayUI()

    window.show()

    sys.exit(app.exec())