from flet import *
from livre import Livre

def main(page:Page):
    page.title="gestion des livres"
    page.window.width=450
    page.window.left=750
    page.scroll="auto"

# creer des livres pour manipulation des donners 
    l1=Livre("harry putter","imagination","oui")
    l2=Livre("no3man","imagination","non")
    l3=Livre("jon sina","imagination","non")
    l4=Livre("spider man","imagination","oui")
    l5=Livre("my life","imagination","oui")
    l6=Livre("dev","imagination","non")
    l7=Livre("harry putter","imagination","non")
    l8=Livre("alten","imagination","oui")

    list_of_livre=[l1,l2,l3,l4,l5,l6,l7,l8]

    def voirlivre(e):
        print(l1.titre)
    filter_input=TextField("looking foor book ?")
    btn_search=ElevatedButton("search",on_click=voirlivre)

    header_container=Container(
        content=Row(
            controls=[
                filter_input,
                btn_search
            ]
        )
    )

    livre_containers=[]
    for livre in list_of_livre:
        livre_container=Container(
        content=Column(
            controls=[
                Text(f" Titre : {livre.titre}"),#doit etre recupere de la classe
                #button peux ouvrir une autre page pour voir la description ou un extrait du livre 
                ElevatedButton("description",on_click=...),
                Text(f" disponibilite : {livre.is_disponible}")#doit etre recupere de la classe
            ]
        ),
        bgcolor=colors.AMBER_300,
        width=250,
        padding=20,
        border_radius=10,
        alignment=alignment.center
       )
        livre_containers.append(livre_container)
    
    galery_book=Container(
        content=
            #ici on va mettre les livres
            Column(
                controls=[*livre_containers],
                )
        )
        

    page.add(
        header_container,
        galery_book
    )
    page.update()

app(main)