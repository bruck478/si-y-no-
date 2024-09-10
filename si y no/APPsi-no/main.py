import flet as ft


def main(page: ft.Page):
    page.title="¿Me perdonas?"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER 
    page.bgcolor="blue"
    
    lbll=ft.Text("¿Me perdonas?"
                style=ft.TextThemeStyle(size=40, weight="blod"))
    
    Ingl=ft.Image(src="triste.png",width=200, height=200)
    
    btnSi=ft.ElevatedButton("Si",
                            color="green",
                            width=100,
                            height=50)
    
    btnNo=ft.ElevatedButton("No"    ,   
                            color="red",
                            width=100,
                            height=50)

    page.add(
        ft.Column(
            [
                lbli,
                Ingi,
                ft.Row([btnSi,btnNo])
            ]
        )
    )

ft.app(main)
