from django.http import HttpResponse
from django.shortcuts import render

def vista_carta(request): #mi primera vista
    con_sed = {
        "Café" : {
            "Espresso" : {
                "tamaños" : {
                    "20 ml" : "$2.000",
                    "40 ml" : "$2.200"
                },
                "descripción" : ""
            },
            "Americano" : {
                "tamaños" : {
                    "200 ml" : "$2.300",
                    "300 ml" : "-"
                },
                "descripción" : "Espresso doble + agua"
            },
            "Macchiato" : {
                "tamaños" : {
                    "20 ml" : "$2.300",
                    "40 ml" : "$2.500",
                },
                "descripción" : "Espresso + un toque de espuma"
            },
            "Flat white" : {
                "tamaños": {
                    "150 ml" : "$2.700",
                },
                "descripción": "Espresso doble + poca leche texturizada"
            },
            "Cappuccino" : {
                "tamaños": {
                    "200 ml" : "$3.000",
                },
                "descripción" : "Espresso + leche texturizada + espuma, en partes iguales"
            },
            "Latte" : {
                "tamaños": {
                    "300 ml" : "$3.200"
                },
                "descripción": "Espresso + mucha leche texturizada"
            },
            "Mocaccino" : {
                "tamaños" : {
                    "200 ml" : "$3.500",
                },
                "descripción": "Capuccino + cacao"
            },
            "Affogatto" : "No disponible",
            "Café filtrado" : {
                "tamaños" : {
                    "300 ml" : "$3.500"
                },
                "descripción" : "Café molino a mano, preparado en método V60"
            }
        },
        "Otros bebestibles" : {
            "Té en hojas" : {
                "tamaño" : {
                    "200 ml" : "$2.500",
                    "tetera (2 tazas)" : "$4.800"
                },
                "variedades" : {
                    "Rukeri negro" : {
                        "descripción" : "Té negro en hebras. Un exquisito clásico"
                    },
                    "Earl Grey" : {
                        "descripción" : "Té negro en hebras y esencia natural de bergamota. Un té negro con un toque cítrico"
                    },
                    "Masala Chai" : {
                        "descripción" : "Té negro en hebras, canela, cardamomo, clavo de olor, pimienta y jengibre. Un té negro con sensación picante"
                    },
                    "Summer Peach" : {
                        "descripción" : "Té negro en hebras, papaya, damasco, durazno, hojas de mora y pétalos de caléndula"
                    },
                    "Brisa Tropical" : {
                        "descripción": "Té verde, papaya y esencia natural de maracuyá. Un blend de té verde muy fresco"
                    },
                    "Golden Tea" : {
                        "descripción" : "Infusión de jengibre, cúrcuma, canela, hierba luisa, cardamomo y nuez moscada. Una exquisita opción si no quieres cafeína en tu taza"
                    }
                }
            },
            "Chai Latte": {
                "tamaño" : {
                    "200 ml" : "$2.800",
                },
                "descripción" : "Masala Chai + leche texturizada"
            },
            "Dirty Chai" : {
                "tamaño" : {
                    "200 ml" : "$3.100"
                },
                "descripción" : "Masala chai + Espresso + leche texturizada"
            },
            "Matcha Latte" : {
                "tamaño" : {
                    "200 ml" : "$3.200"
                },
                "descripción" : "Té verde pulverizado de origen + leche texturizada"
            },
            "Chocolate caliente 50" + '%' + "cacao" : {
                "tamaño" : {
                    "200 ml" : "$3.500"
                },
                "descripción" : "Delicioso chocolate caliente 50" + '%' + "cacao con la textura perfecta: como una barra de chocolate en tu taza"
            },
            "Chocolate caliente 65" + '%' + "cacao" : {
                "tamaño" : {
                    "200 ml" : "$3.800"
                },
                "descripción" : "Si prefieres el chocolate más amargo, esta es tu mejor opción: tiene la misma textura que nuestro chocolate más dulce, pero con mayor cantidad de cacao. Además, si lo pides con not milk es una exquisita opción vegana"
            },
            "Jugo natural": {
                "tamaño" : {
                    "300 ml" : "$3.600" 
                },
                "descripción" : "Jugo de frutas naturales. Escoge el sabor que prefieras: piña, frutilla, arándano, mango o chirimoya"
            },
            "Bebida en lata" : {
                "tamaño" : {
                    "350 ml" : "1.400"
                }
            },
            "Agua mineral sin gas" : {
                "tamaño" : {
                    "500 ml" : "1.400"
                }
            }
        }
    }
    con_hambre = {
        "Antojos salados" : {
            "Sándwich 'El Gringo'" : {
                "precio" : "$7.200",
                "descripción": "Tocino ahumado, tortilla de huevo y queso mantecoso"
            },
            "Sándwich 'El Ibérico'": {
                "precio" : "$7.500",
                "descripción" : "Jamón Serrano, tomate en rodajas, queso mantecoso y rúcula fresca"
            },
            "Sándwich 'El Italiano'" : {
                "precio" : "$6.500",
                "descripción" : "Jamón artesanal, salame ahumado, queso mantecoso y aceitunas negras laminadas"
            },
            "Sándwich Aliado" : {
                "precio" : "$4.300",
                "descripción" : "Jamón artesanal y queso mantecoso"
            },
            "Sándwich Palta" : {
                "precio" : "$5.300",
                "descripción" : "Elige entre: Palta y jamón artesanal o Palta y queso mantecoso"
            },
            "Sándwich del Huerto" : {
                "precio" : "$5.000",
                "descripción" : "Palta, tomate en rodajas y mix de semillas"
            }
        },
        "Antojos Dulces" : {
            "Galletón" : {
                "precio" : "$1.200",
                "descripción" : "Crujiente galleta con trocitos de chocolate de leche"
            },
            "Brownie de chocolate" : {
                "precio" : "$1.500",
                "descripción" : "Delicioso brownie relleno con chips de choocolate belga"
            },
            "Rollito de canela": {
                "precio" : "$1.700",
                "descripción" : "Espiral danesa rellena de canela y pasta de azúcar morena"
            },
            "Danés" : {
                "precio" : "$1.800",
                "descripción" : "Bollo relleno de crema y un toque de almendras"
            },
            "Muffin de arándano" : {
                "precio" : "$1.800",
                "descripción" : "Bizcocho de vainilla con crumble y trozos de arándano"
            },
            "Donut rellena" : {
                "precio" : "$2.000",
                "descripción" : "Pan dulce frito con un toque de limón, cubierta en azúcar y rellena de chocolate-avellana o crema bavaria (similar a la pastelera)"
            },
            "Hojaldre de manzana" : {
                "precio" : "$2.500",
                "descripción" : "Masa de hoja, rellena con manzana cocida, pasas y canela. Nuestra exquisita opción vegana dulce"
            },
            "Torta de triple chocolate" : {
                "precio" : "$4.000",
                "descripción" : "Bizcocho de chocolate, relleno y decorado con ganache de chocolate "
            }
        }
    }
    return render(request, 'plantilla_menu.html', {'Con_sed': con_sed, 'Con_hambre': con_hambre})

def vista_sobre_nosotros(request): #mi primera vista
    return HttpResponse("Estos somos")

def vista_contacto(request): #mi primera vista
    return HttpResponse("Conversemoss")