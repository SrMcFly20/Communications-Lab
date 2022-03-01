#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Multiplexado
# Author: Peña_Hernandez
# Copyright: Peña_Hernandez
# GNU Radio version: 3.8.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from ModuladorPAM import ModuladorPAM  # grc-generated hier_block
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class Multiplexado(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Multiplexado")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Multiplexado")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Multiplexado")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.w = w = 25
        self.samp_rate = samp_rate = 100000
        self.fs = fs = 1000
        self.Delay_3 = Delay_3 = 75
        self.Delay_2 = Delay_2 = 50
        self.Delay_1 = Delay_1 = 25

        ##################################################
        # Blocks
        ##################################################
        self._w_range = Range(0, 50, 1, 25, 200)
        self._w_win = RangeWidget(self._w_range, self.set_w, 'Ancho de Pulso', "counter_slider", int)
        self.top_layout.addWidget(self._w_win)
        self._fs_range = Range(0, 50000, 1000, 1000, 200)
        self._fs_win = RangeWidget(self._fs_range, self.set_fs, 'Frecuencia de Senal Cuadrada', "counter_slider", int)
        self.top_layout.addWidget(self._fs_win)
        self._Delay_3_range = Range(0, 100, 1, 75, 200)
        self._Delay_3_win = RangeWidget(self._Delay_3_range, self.set_Delay_3, 'Delay_3', "counter_slider", float)
        self.top_layout.addWidget(self._Delay_3_win)
        self._Delay_2_range = Range(0, 100, 1, 50, 200)
        self._Delay_2_win = RangeWidget(self._Delay_2_range, self.set_Delay_2, 'Delay_2', "counter_slider", float)
        self.top_layout.addWidget(self._Delay_2_win)
        self._Delay_1_range = Range(0, 100, 1, 25, 200)
        self._Delay_1_win = RangeWidget(self._Delay_1_range, self.set_Delay_1, 'Delay_1', "counter_slider", float)
        self.top_layout.addWidget(self._Delay_1_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Add all signals', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            4 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(4):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, Delay_3)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, Delay_2)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Delay_1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_0_2 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fs/10, 1, 0, 0)
        self.analog_sig_source_x_0_0_1 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, fs/10, 1, 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, fs/10, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fs/10, 1, 0, 0)
        self.ModuladorPAM_1_2 = ModuladorPAM(
            fs=fs,
            samp_rate=samp_rate,
            w=w,
        )
        self.ModuladorPAM_1_1 = ModuladorPAM(
            fs=fs,
            samp_rate=samp_rate,
            w=w,
        )
        self.ModuladorPAM_1_0 = ModuladorPAM(
            fs=fs,
            samp_rate=samp_rate,
            w=w,
        )
        self.ModuladorPAM_1 = ModuladorPAM(
            fs=fs,
            samp_rate=samp_rate,
            w=w,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ModuladorPAM_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.ModuladorPAM_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.ModuladorPAM_1_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.ModuladorPAM_1_1, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.ModuladorPAM_1_2, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.ModuladorPAM_1, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.ModuladorPAM_1_0, 0))
        self.connect((self.analog_sig_source_x_0_0_1, 0), (self.ModuladorPAM_1_1, 0))
        self.connect((self.analog_sig_source_x_0_0_2, 0), (self.ModuladorPAM_1_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_delay_0_1, 0), (self.qtgui_time_sink_x_0, 3))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Multiplexado")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_w(self):
        return self.w

    def set_w(self, w):
        self.w = w
        self.ModuladorPAM_1.set_w(self.w)
        self.ModuladorPAM_1_0.set_w(self.w)
        self.ModuladorPAM_1_1.set_w(self.w)
        self.ModuladorPAM_1_2.set_w(self.w)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.ModuladorPAM_1.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_1_0.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_1_1.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_1_2.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_2.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.ModuladorPAM_1.set_fs(self.fs)
        self.ModuladorPAM_1_0.set_fs(self.fs)
        self.ModuladorPAM_1_1.set_fs(self.fs)
        self.ModuladorPAM_1_2.set_fs(self.fs)
        self.analog_sig_source_x_0_0.set_frequency(self.fs/10)
        self.analog_sig_source_x_0_0_0.set_frequency(self.fs/10)
        self.analog_sig_source_x_0_0_1.set_frequency(self.fs/10)
        self.analog_sig_source_x_0_0_2.set_frequency(self.fs/10)

    def get_Delay_3(self):
        return self.Delay_3

    def set_Delay_3(self, Delay_3):
        self.Delay_3 = Delay_3
        self.blocks_delay_0_1.set_dly(self.Delay_3)

    def get_Delay_2(self):
        return self.Delay_2

    def set_Delay_2(self, Delay_2):
        self.Delay_2 = Delay_2
        self.blocks_delay_0_0.set_dly(self.Delay_2)

    def get_Delay_1(self):
        return self.Delay_1

    def set_Delay_1(self, Delay_1):
        self.Delay_1 = Delay_1
        self.blocks_delay_0.set_dly(self.Delay_1)





def main(top_block_cls=Multiplexado, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
