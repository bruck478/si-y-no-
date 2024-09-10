import flet as ft


def main(page: ft.Page):
    page.title="¿Me perdonas?"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER 
    page.bgcolor="black"
    
    lbli=ft.Text("¿Me perdonas?",
                style=ft.TextStyle(size=40, weight="bold"))
    
    Ingi=ft.Image(src="triste.png",width=200, height=200)
    
    btnSi=ft.ElevatedButton("Si",
                            color="green",
                            width=100,
                            height=50)
    
    btrNo=ft.ElevatedButton("No"    ,   
                            color="red",
                            width=100,
                            height=50)

page.add(
    ft.Column{}
)

ft.app(main)
