import flet as ft


def main(page: ft.Page):

    page.title = "Plan de Ahorro"

    page.padding = 20

    titulo = ft.Text(value="Bienvenido al Sistema de Plan de Ahorro",
                     size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_300)

    page.theme_mode = ft.ThemeMode.LIGHT

    def actualizar_tema(e):
        if tema_switch.value:
            page.theme_mode = ft.ThemeMode.DARK
            titulo.color = ft.Colors.LIGHT_BLUE_200
            page.update()
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            titulo.color = ft.Colors.PINK_300
            page.update()

    tema_switch = ft.Switch(label="Modo Oscuro", on_change=actualizar_tema)

    page.add(titulo, tema_switch)


ft.app(main)
