from django.shortcuts import render

# Create your views here.
def listagem_produtos(request):
    produtos_de_vendedores = [{        
        'vendedor': {'nome': 'Jhon Doe'},
        'produtos': [
            {'nome': 'Uva', 'preco': 1},
            {'nome': 'Melancia', 'preco': 10},
            {'nome': 'Banana', 'preco': 14}
        ]
    },
    {
        'vendedor': {'nome': 'Marta Doe'},
        'produtos': [ {'nome': 'Maça', 'preco': 5},

        ]
    }]
        
    context = {'produtos_de_vendedores': produtos_de_vendedores}
    
    
    return render(request, 'templates/listagem_produtos.html', context)
