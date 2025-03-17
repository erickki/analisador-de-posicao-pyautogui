import flet as ft
import pyautogui
import time

FONTE = "JetBrains Mono"
NEGRITO = ft.FontWeight.BOLD

def tela_geral(page: ft.Page):

    page.title = "Analisador."
    page.bgcolor = "#1a1a1a"
    page.window.width= 300
    page.window.height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.alignment = ft.alignment.center
    page.padding = 0
    page.window.center()
    

    def cursor_posicao_loop():
        while True:
            cursor_posicao = pyautogui.position()
            cursor_posicao_x = f"Posição X: {cursor_posicao.x} (horizontal)"
            cursor_posicao_y = f"Posição Y: {cursor_posicao.y} (vertical)"
            posicao_cursor_x.content.value = cursor_posicao_x
            posicao_cursor_y.content.value = cursor_posicao_y
            page.update()
            time.sleep(0.1)

    texto = ft.Container(
        content=ft.Text(
            value="Posição do cursor:", text_align=ft.TextAlign.CENTER, font_family=FONTE, size=18, weight=NEGRITO,
            color="#dedede"
        )
    )

    posicao_cursor_x = ft.Container(
        content=ft.Text(
            value="", text_align=ft.TextAlign.CENTER, font_family=FONTE, size=14, weight=NEGRITO, color="#dedede"
        )
    )

    posicao_cursor_y = ft.Container(
        content=ft.Text(
            value="", text_align=ft.TextAlign.CENTER, font_family=FONTE, size=14, weight=NEGRITO, color="#dedede"
        )
    )

    fundo_geral = ft.Container(
        content=ft.Column(
            [
                texto, posicao_cursor_x, posicao_cursor_y
            ],alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    page.add(fundo_geral)
    cursor_posicao_loop()

ft.app(target=tela_geral)