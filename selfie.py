# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 18:20:39 2023

@author: 91954
"""
from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class selfie_app(App):
    def makeApp(self):
        
        self.obj_camera = Camera()
        self.obj_camera.resolution=(800,800)
        obj_button=Button(text="click here")
        obj_button.size_hint=(.6,.3)
        obj_button.pos_hint={'x':.35,'y':.35}
        obj_button.bind(on_press=self.selfie_take())
        obj_layout=BoxLayout()
        obj_layout.addWidget(self.obj_camera)
        obj_layout.addWidget(self.obj_button)
        return obj_layout
    def selfie_take(self,*args):
        print("selfie has been taken successfully")
        self.obj_camera.export_to_png('p.png')
        
if __name__ == '__main__':
    selfie_app().run()        