import flet as ft
import time


def main(page: ft.Page):

    page.title = "Plan de Ahorro"

    page.padding = 20

    page.scroll = "adaptive"

    titulo = ft.Text(value="Bienvenido al Sistema de Plan de Ahorro",
                     size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_300)

    subtitulo = ft.Text(value="Calculo De Ahorro Final:", size=20,
                        weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_300)

    page.theme_mode = ft.ThemeMode.LIGHT

    txt_preview = ft.Text(value="Ingresa los datos completos",
                          size=14, weight=ft.FontWeight.BOLD)

    contador_meses = ft.Text(value=0)

    def actualizar_tema(e):
        if tema_switch.value:
            page.theme_mode = ft.ThemeMode.DARK
            titulo.color = ft.Colors.LIGHT_BLUE_200
            subtitulo.color = ft.Colors.PINK_300
            page.update()
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            titulo.color = ft.Colors.PINK_300
            subtitulo.color = ft.Colors.BLUE_300
            page.update()

    def actualizar_preview(e):
        txt_preview.value = f"""
        Nombre: {nombre_input.value.title()}
        Edad: {edad_dropdown.value}
        Objetivo: {objetivo_radio.value}"""
        page.update()

    def actualizar_objetivo(e):
        costo_input.label = f"Costo de {objetivo_radio.value}:"
        page.update()

    def calculo_ahorro(e):
        meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo",
                 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre",
                 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
        ahorro_mensual = int(salario_input.value) - int(gastos_input.value)
        ahorro_total = ahorro_mensual
        costo = int(costo_input.value)
        mes = int(time.strftime("%m"))
        while (ahorro_total <= costo):
            page.add(
                ft.Text(value=f"{meses.get(mes, 'Error')} -- ${ahorro_total}"))
            ahorro_total += ahorro_mensual
            mes += 1
            contador_meses.value = int(contador_meses.value)+1
            if mes > 12:
                mes = 1
            page.update()
        page.add(
            ft.Text(value=f"{objetivo_radio.value} alcanzado en {int(contador_meses.value)//12} Años con {int(contador_meses.value) % 12} Meses",
                    size=16, weight=ft.FontWeight.BOLD))

    nombre_input = ft.TextField(
        label="Nombre:", border_radius=8, on_change=actualizar_preview)

    edad_dropdown = ft.Dropdown(
        label="Edad",
        options=[ft.dropdown.Option(str(edad)) for edad in range(18, 101)],
        on_change=actualizar_preview
    )

    objetivo_radio = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Auto", label="Auto"),
            ft.Radio(value="Viaje", label="Viaje"),
            ft.Radio(value="Casa", label="Casa"),
            ft.Radio(value="Celular", label="Celular")
        ])
    )

    objetivo_radio.on_change = actualizar_preview
    objetivo_radio.on_change = actualizar_objetivo

    salario_input = ft.TextField(
        label="Salario Mensual:", border_radius=8, on_change=actualizar_preview, expand=True)

    gastos_input = ft.TextField(
        label="Gastos Mensuales:", border_radius=8, expand=True)

    costo_input = ft.TextField(
        label=f"Costo de Ninguno", border_radius=8, expand=True)

    fila_inputs = ft.Row(
        [salario_input, gastos_input, costo_input],
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER
    )

    tema_switch = ft.Switch(label="Modo Oscuro", on_change=actualizar_tema)

    calcular_boton = ft.IconButton(
        icon=ft.Icons.DONE_OUTLINE, on_click=calculo_ahorro)

    contenido = ft.Container(
        content=ft.Column(
            [
                titulo,
                tema_switch,
                nombre_input,
                edad_dropdown,
                objetivo_radio,
                fila_inputs,
                txt_preview,
                calcular_boton,
                subtitulo
            ],
            scroll="auto"
        ),
        expand=False
    )

    page.add(contenido)
    page.update()


ft.app(main)
