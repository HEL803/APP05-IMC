import flet as ft



def main(page: ft.Page):
    page.title="calculadora imc"
    page.bgcolor="yellow"
    
    txtpeso=ft.TextField(label="ingresa tu peso")
    txtaltura=ft.TextField(label="ingresa tu altura")
    lblimcv=ft.Text("tu imc es de:")
    
    ing=ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )    
    btncalcular=ft.ElevatedButton(text="calcular")
    btnlimpiar=ft.ElevatedButton(text="limpiar")    
    
    page.add(
        ft.Column(
            controls=[
                txtpeso,txtaltura,lblimcv
            ],aligment="CENTER"),
        ft.Row(
            controls=[
                ing
            ],aligment="CENTER"),
        ft.Row(
            controls=[
                btncalcular,btnlimpiar
            ],aligment="CENTER")
        )
        
            
        
            
    
    


ft.app(target=main,view=ft.AppView.WEB_BROWSER)
