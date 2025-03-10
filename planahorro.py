import flet as ft


def main(page: ft.Page):

    page.title = "Plan de Ahorro"

    page.padding = 20

    titulo = ft.Text(value="Bienvenido al Sistema de Plan de Ahorro",
                     size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_300)

    page.theme_mode = ft.ThemeMode.LIGHT

    txt_preview = ft.Text(value="Ingresa los datos completos",
                          size=14, weight=ft.FontWeight.BOLD)

    def actualizar_preview(e):
        txt_preview.value = f"""
        Nombre: {nombre_input.value.title()}
        Edad: {edad_dropdown.value}"""
        page.update()

    def actualizar_tema(e):
        if tema_switch.value:
            page.theme_mode = ft.ThemeMode.DARK
            titulo.color = ft.Colors.LIGHT_BLUE_200
            page.update()
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            titulo.color = ft.Colors.PINK_300
            page.update()

    nombre_input = ft.TextField(
        label="Nombre:", border_radius=8, on_change=actualizar_preview)

    edad_dropdown = ft.Dropdown(
        label="Edad",
        options=[ft.dropdown.Option(str(edad)) for edad in range(18, 101)],
        on_change=actualizar_preview
    )

    tema_switch = ft.Switch(label="Modo Oscuro", on_change=actualizar_tema)

    page.add(titulo, tema_switch, nombre_input, edad_dropdown, txt_preview)


ft.app(main)
