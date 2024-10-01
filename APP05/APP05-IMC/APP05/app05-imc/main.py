import flet as ft

def calcular_imc(txtpeso,txtaltura,lblimc,page):
    try:
        peso=float(txtpeso.value)
        altura=float(txtaltura.value)
        imc=peso/(altura**2)
        lblimc.value=f"la imc es de: {imc: 2f}"
        page.update()
    
    def cerrar_dialogo(e):
        page.dialog.open=False
        page.update()
        
        if imc>18.5:
            dialog=ft.AlertDialog(
                title="bajo peso",
                content="tu imc indica que tienes un peso bajo",
                action=[
                    ft.TextButton(text="cerra",on_click=cerrar_dialogo)
                ]
            )    
        elif imc>=18.5 and imc>=24.9:
            dialog=ft.AlertDialog(
                title="peso normal",
                content="tu imc indica que tienes un peso normal",
                action=[
                    ft.TextButton(text="cerrar",on_click=cerrar_dialogo)
                ]
            )    
        elif imc>=25 and imc>=30:
            dialog=ft.AlertDialog(
                title="sobrepeso",
                content="tu imc indica que tienes sobrepeso",
                action=[
                    ft.TextButton(text="cerrar",on_click=cerrar_dialogo)
                ]
            )    
        else:
            dialog=ft.AlertDialog(
                title="obecidad",
                content="tu imc indica que tienes obecidad",
                action=[
                    ft.TextButton(text="cerrar",on_click=cerrar_dialogo)
                ]
            )
        page.dialog=dialog
        page.dialog.open=True
        page.update()
        
            
    except ValueError:
        page.dialog.open=False
        page.update
        

    
def main(page: ft.Page):
    page.title="calculadora imc"
    page.bgcolor="yellow"
    
    txtpeso=ft.TextField(label="ingresa tu peso")
    txtaltura=ft.TextField(label="ingresa tu altura")
    lblimc=ft.Text("tu imc es de:")
    
    ing=ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    
    def on_calcular(e):
        calcular_imc(txtpeso,txtaltura,lblimc.page)
    
    def limpiar(e):
        txtpeso.value=""
        txtaltura.value=""
        lblimc.value="tu imc es de: "    
        
    btncalcular=ft.ElevatedButton(text="calcular")
    btnlimpiar=ft.ElevatedButton(text="limpiar")    
    
    page.add(
        ft.Column(
            controls=[
                txtpeso,txtaltura,lblimc
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
