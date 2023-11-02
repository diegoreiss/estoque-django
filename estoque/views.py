from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_POST


from .models import Products, Categories

# Create your views here.

QUANTIDADE_POR_PAGINA = 1

@require_GET
def index(request):
    numero_da_pagina = request.GET.get("page")

    if not numero_da_pagina:
        numero_da_pagina = 1
    
    produtos = Products.objects.filter(in_stock=True, qtd__gt=1)

    if "fora-stock" in request.GET:
        print("tem")
        produtos = Products.objects.filter(in_stock=False, qtd__gt=1)
    
    paginator_produtos = Paginator(produtos, QUANTIDADE_POR_PAGINA)
    elided = list(paginator_produtos.get_elided_page_range(number=numero_da_pagina, on_each_side=3, on_ends=1))
    pagina = paginator_produtos.get_page(numero_da_pagina)

    categorias = Categories.objects.all()
    
    context = {
        "pagina_atual": int(numero_da_pagina),
        "pagina_anterior": pagina.previous_page_number() if pagina.has_previous() else None,
        "proxima_pagina": pagina.next_page_number() if pagina.has_next() else None,
        "total_paginas": str(paginator_produtos.num_pages),
        "pagina_elided": elided,
        "dados_pagina": pagina,
        "ellipsis": str(paginator_produtos.ELLIPSIS),
        "categorias": categorias,
    }

    return render(request, "estoque/index.html", context)


def product_detail(request, id):
    product = Products.objects.get(id=id)
    context = {
        "product": product
    }

    return render(request, 'estoque/product_detail.html', context)


@require_POST
def add_product(request):
    req = request.POST
    print(req)

    name = req.get("name")
    category = req.get("category")
    price = req.get("price")
    description = req.get("description")
    quantity = req.get("quantity")
    discount = req.get("discount")

    Products.objects.create()

    return redirect('home')


def delete_product(request, id):
    Products.objects.get(id=id).delete()

    return redirect('home')


def sell_product(request, id):
    produto = Products.objects.get(id=id)

    if produto.qtd == 0:
        return index(request)

    produto.qtd -= 1
    produto.save()

    return product_detail(request, id)

