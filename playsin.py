import threading
import pyaudio
import struct
import numpy as np
import wx

def play(Hz=440, fs=8000, sec=1):
    data = [int(15000*np.sin(2*np.pi*x*Hz/fs)) for x in range(sec*fs)]
    data = struct.pack("h"*len(data), *data)
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1, rate=int(fs), output=True)
    chunk = 1024
    sp = 0
    buffer = data[sp:sp+chunk]
    while sp < len(data):
        stream.write(buffer)
        sp = sp+chunk
        buffer = data[sp:sp+chunk]
    stream.close()
    audio.terminate()

def loop():
    global loopFlag
    while loopFlag:
        play(slider1.GetValue(), slider2.GetValue(), 2)

def ButtonBind(event):
    global loopFlag
    if event.GetId() == 100:
        threading.Thread(target=play, args=(slider1.GetValue(), slider2.GetValue(), slider3.GetValue())).start()
    elif event.GetId() == 101:
        loopFlag = loopb.GetValue()
        threading.Thread(target=loop).start()
    

if __name__=='__main__':
    loopFlag = False
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, 'HSPP', size=(600, 300), style=wx.MINIMIZE_BOX | wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)

    panel = wx.Panel(frame, wx.ID_ANY)
    slidertext1 = wx.StaticText(panel, label='Hz')
    slider1 = wx.Slider(panel, style=wx.SL_HORIZONTAL|wx.SL_LABELS)
    slider1.SetMin(100)
    slider1.SetMax(50000)
    slider1.SetValue(100)
    slidertext2 = wx.StaticText(panel, label='fs')
    slider2 = wx.Slider(panel, style=wx.SL_HORIZONTAL|wx.SL_LABELS)
    slider2.SetMin(2000)
    slider2.SetMax(50000)
    slider2.SetValue(2000)
    slidertext3 = wx.StaticText(panel, label='sec')
    slider3 = wx.Slider(panel, style=wx.SL_HORIZONTAL|wx.SL_LABELS)
    slider3.SetMin(0)
    slider3.SetMax(60)
    slider3.SetValue(0)
    start = wx.Button(panel, id=100, label='start')
    loopb = wx.ToggleButton(panel, id=101, label='loop')
    layout = wx.BoxSizer(wx.VERTICAL)
    layout.Add(slidertext1, flag=wx.GROW)
    layout.Add(slider1, flag=wx.GROW)
    layout.Add(slidertext2, flag=wx.GROW)
    layout.Add(slider2, flag=wx.GROW)
    layout.Add(slidertext3, flag=wx.GROW)
    layout.Add(slider3, flag=wx.GROW)
    layout.Add(start, flag=wx.GROW)
    layout.Add(loopb, flag=wx.GROW)
    panel.SetSizer(layout)

    panel.Bind(wx.EVT_BUTTON, ButtonBind)
    panel.Bind(wx.EVT_TOGGLEBUTTON, ButtonBind)
    frame.Show()
    app.MainLoop()