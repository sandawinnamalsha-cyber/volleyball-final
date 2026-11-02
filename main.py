import flet as ft

def main(page: ft.Page):
    page.title = "Volleyball Score"
    page.bgcolor = "black"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    a = ft.Text("0", size=100, color="white", weight="bold")
    b = ft.Text("0", size=100, color="white", weight="bold")
    sa = 0
    sb = 0

    def add_a(e):
        nonlocal sa
        sa+=1
        a.value=str(sa)
        page.update()
    def sub_a(e):
        nonlocal sa
        if sa>0: sa-=1
        a.value=str(sa)
        page.update()
    def add_b(e):
        nonlocal sb
        sb+=1
        b.value=str(sb)
        page.update()
    def sub_b(e):
        nonlocal sb
        if sb>0: sb-=1
        b.value=str(sb)
        page.update()
    def reset(e):
        nonlocal sa,sb
        sa=0; sb=0
        a.value="0"; b.value="0"
        page.update()

    page.add(
        ft.Column([
            ft.Text("VOLLEYBALL SCOREBOARD", color="white", size=28, weight="bold"),
            ft.Row([
                ft.Column([ft.Text("TEAM A", color="white", size=20), a, ft.Row([ft.ElevatedButton("-", on_click=sub_a), ft.ElevatedButton("+", on_click=add_a)])], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Text(":", color="white", size=60),
                ft.Column([ft.Text("TEAM B", color="white", size=20), b, ft.Row([ft.ElevatedButton("-", on_click=sub_b), ft.ElevatedButton("+", on_click=add_b)])], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.ElevatedButton("RESET", on_click=reset, bgcolor="red", color="white")
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
