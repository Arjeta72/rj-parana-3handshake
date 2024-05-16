from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
import sys

class TwoPanelLayoutApp(MDApp):
    def build(self):
        Window.size = (900,500)
        screen_manager = ScreenManager()
        screen = Screen()
        screen.add_widget(self._create_split_layout_panel())
        screen_manager.add_widget(screen)
        return screen_manager
   
    def _create_split_layout_panel(self):
        split_layout_panel = GridLayout(cols=2)
        split_layout_panel.add_widget(self._create_navigation_bar_panel())
        split_layout_panel.add_widget(self._create_content_panel())

        return split_layout_panel
    
    
    def _create_navigation_bar_panel(self):
        navigation_bar_panel = GridLayout(cols=1, spacing=20)
        navigation_bar_panel.size_hint_x = None
        navigation_bar_panel.width = 300

        navigation_bar_panel_title = MDLabel(text="NavBar",size_hint=(1, 0.1), theme_text_color = 'Secondary',
                                             font_style="H6")
        navigation_bar_panel_content = MDLabel(text="Nav Bar Buttons",size_hint=(1, 0.9), theme_text_color = 'Secondary',
                                             font_size="15sp", markup=True)
        navigation_bar_panel.add_widget(navigation_bar_panel_title)
        navigation_bar_panel.add_widget(navigation_bar_panel_content)
        return navigation_bar_panel
    

    def _create_content_panel(self):
        content_panel = GridLayout(cols=1, spacing=20)
        content_panel.size_hint_x = None
        content_panel.width = 600

        content_panel_title = MDLabel(text="Content panel",size_hint=(1, 0.1), theme_text_color = 'Secondary',
                                             font_style="H6")
        content_panel_content = MDLabel(text="Content Space",size_hint=(1, 0.9), theme_text_color = 'Secondary',
                                             font_size="15sp", markup=True)
        content_panel.add_widget(content_panel_title)
        content_panel.add_widget(content_panel_content)
        return content_panel

TwoPanelLayoutApp().run()
