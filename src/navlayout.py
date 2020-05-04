from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.lang.builder import Builder


Builder.load_string("""

<NavigationDrawerLogo@Image>:
    size_hint: None, None
    width: self.parent.width
    height: self.parent.width / self.image_ratio
    source: "res/book.jpg"

<NavLayout>:
    id: nav_drawer

    BoxLayout:
        orientation: "vertical"

        NavigationDrawerLogo:

        MDList:
            OneLineListItem:
                text: "Главное меню"
                on_release:
                    nav_drawer.set_state("close")
                    app.open_textslist()

            OneLineListItem:
                text: "Настройки"
                on_release:
                    nav_drawer.set_state("close")
                    app.open_settings()

        # just for keep all at the top
        BoxLayout:

""", filename="navlayout.kv")


class NavLayout(MDNavigationDrawer):
	pass