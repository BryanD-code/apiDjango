from django.core.management.base import BaseCommand
from djangocrud.models import Suma, Alergias

class Command(BaseCommand):
    help = 'Carga los platos y asigna las alergias automáticamente en djangocrud'

    def handle(self, *args, **kwargs):
        self.stdout.write("Iniciando carga de datos en djangocrud...")

        # ---------------------------------------------------------
        # 1. CREAR LAS ALERGIAS BASE (Si no existen)
        # ---------------------------------------------------------
        # Esto es necesario para que los IDs del JSON (1, 2, 5...)
        # tengan una correspondencia real en la base de datos.
        alergias_base = {
            1: "Gluten", 2: "Crustáceos", 3: "Huevos", 4: "Soja", 5: "Lácteos",
            6: "Frutos cáscara", 7: "Apio", 8: "Pescado", 9: "Cacahuetes", 10: "Mostaza",
            11: "Sésamo", 12: "Sulfitos", 13: "Altramuces", 14: "Moluscos", 15: "Picante"
        }

        for id_aler, info in alergias_base.items():
            obj, created = Alergias.objects.get_or_create(
                id=id_aler, 
                defaults={
                    'Informacion': info, 
                    'ImagenAler': f"https://www.restaurantesuma.es/public/images/allergy_icons/{id_aler}.png"
                }
            )
            if created:
                self.stdout.write(f"- Alergia creada: {info} (ID: {id_aler})")

        # ---------------------------------------------------------
        # 2. JSON COMPLETO CON LOS 200 PLATOS Y SUS IDs
        # ---------------------------------------------------------
        datos_json = [
            {
                "tipo_id": "1",
                "Platos": "1.Ensalada de aguacate con langostinos",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b1e5c9530.png",
                "Precio": "9.90€",
                "alergias_ids": [2]
            },
            {
                "tipo_id": "1",
                "Platos": "3.Ensalada de wakame, algas japonesas",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120182445912324.jpg",
                "Precio": "7.80€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "1",
                "Platos": "4.Ensalada de la habas soja",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120182456998175.jpg",
                "Precio": "6.50€",
                "alergias_ids": [4]
            },
            {
                "tipo_id": "1",
                "Platos": "5.Ensalada chino",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20171208195725788194.jpg",
                "Precio": "8.80€",
                "alergias_ids": [3]
            },
            {
                "tipo_id": "1",
                "Platos": "6.Ensalada con Aliño de Tahini (Sésamo)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b1e5c9e18.png",
                "Precio": "9.30€",
                "alergias_ids": [3, 11]
            },
            {
                "tipo_id": "1",
                "Platos": "7.Rollitos de primavera (verduras y carne)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20230408150611237403.jpg",
                "Precio": "2.15€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "1",
                "Platos": "8.Rollitos de langostinos 4unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240702221341980855.jpg",
                "Precio": "6.80€",
                "alergias_ids": [1, 2]
            },
            {
                "tipo_id": "1",
                "Platos": "9.Rollitos vietnamitas (sólo verduras) 4unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120182522821752.jpg",
                "Precio": "4.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "1",
                "Platos": "10.Wan-Tun de queso con cangrejo  8unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120182530449627.jpg",
                "Precio": "6.90€",
                "alergias_ids": [1, 2, 5]
            },
            {
                "tipo_id": "1",
                "Platos": "11.Pan frito",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240702221744931184.jpg",
                "Precio": "2.15€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "1",
                "Platos": "11A.Pan de gambas",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b1e5ca653.png",
                "Precio": "2.95€",
                "alergias_ids": [2]
            },
            {
                "tipo_id": "1",
                "Platos": "12.Tempura de verduras",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240630133116354846.jpg",
                "Precio": "9.50€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "1",
                "Platos": "13.Tempura de langostinos (6 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240702222308416357.jpg",
                "Precio": "11.95€",
                "alergias_ids": [1, 2]
            },
            {
                "tipo_id": "1",
                "Platos": "13A.Langostinos rebozados con sesamo ( 12 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b1e5cac66.png",
                "Precio": "11.95€",
                "alergias_ids": [1, 2, 3, 11]
            },
            {
                "tipo_id": "1",
                "Platos": "131.Brochetas de Pollo con salsa Teriyaki (2  pincho)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240702222719122271.jpg",
                "Precio": "6.90€",
                "alergias_ids": [1, 4]
            },
            {
                "tipo_id": "1",
                "Platos": "133.Brochetas de Salmón con salsa Teriyaki (2 pinchos)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2b0550ec.png",
                "Precio": "9.10€",
                "alergias_ids": [1, 4, 8]
            },
            {
                "tipo_id": "1",
                "Platos": "134.Takoyaki  de pulpo con salsa Teriyaki (4 bolas)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2b05553f.png",
                "Precio": "6.90€",
                "alergias_ids": [1, 4, 14]
            },
            {
                "tipo_id": "2",
                "Platos": "15.Sopa de aleta tiburón",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120182628235835.jpg",
                "Precio": "4.90€",
                "alergias_ids": [3, 8]
            },
            {
                "tipo_id": "2",
                "Platos": "16.Sopa de agripicante",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b1e5cb434.png",
                "Precio": "4.90€",
                "alergias_ids": [1, 15]
            },
            {
                "tipo_id": "2",
                "Platos": "17.Sopa de miso",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120182643527193.jpg",
                "Precio": "4.90€",
                "alergias_ids": [4]
            },
            {
                "tipo_id": "2",
                "Platos": "18.Sopa de Ramen tallarines con pollo",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120182653151776.jpg",
                "Precio": "6.10€",
                "alergias_ids": [1, 3]
            },
            {
                "tipo_id": "2",
                "Platos": "19.Sopa de Wan-Tun",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120182702358870.jpg",
                "Precio": "5.60€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "3",
                "Platos": "20.Dim-sum cantónes al vapor 8unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b1e5cb9e7.png",
                "Precio": "9.20€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "3",
                "Platos": "21.Shia chiao (gambas y setas) 4unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120182753734290.jpg",
                "Precio": "5.90€",
                "alergias_ids": [1, 2]
            },
            {
                "tipo_id": "3",
                "Platos": "22.Shao mai (carne y setas) 4unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b1e5cc0a2.png",
                "Precio": "5.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "3",
                "Platos": "23.Siao long bao (carne y col china) 4unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b1e5cc575.png",
                "Precio": "5.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "3",
                "Platos": "23A.Samosa de pollo con curry (6 und)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2273f31c.png",
                "Precio": "5.90€",
                "alergias_ids": [1, 15]
            },
            {
                "tipo_id": "3",
                "Platos": "24.Gyoza de pollo a la plancha 6unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240915204620426575.png",
                "Precio": "6.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "4",
                "Platos": "25.Nigiri variadas 10 unidades",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2273fc2d.png",
                "Precio": "25.50€",
                "alergias_ids": [2, 8]
            },
            {
                "tipo_id": "4",
                "Platos": "26A.Nigiri Salmón 2unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120182913376635.jpg",
                "Precio": "4.80€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "4",
                "Platos": "26B.Nigiri Atún 2unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120182938375698.jpg",
                "Precio": "5.80€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "4",
                "Platos": "26C.Nigiri Pez mantequilla 2unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120182947794924.jpg",
                "Precio": "4.80€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "4",
                "Platos": "26D.Nigiri Anguila 2unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120183001571157.jpg",
                "Precio": "4.80€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "4",
                "Platos": "26F.Nigiri ventresca salmón flameado ( 2 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b227401a9.png",
                "Precio": "5.80€",
                "alergias_ids": [1, 8]
            },
            {
                "tipo_id": "4",
                "Platos": "26H.Nigiri Ebi 2unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120184251223131.jpg",
                "Precio": "4.80€",
                "alergias_ids": [2]
            },
            {
                "tipo_id": "4",
                "Platos": "26P.Nigiri de salmón flameado ( 2 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b22740cf6.png",
                "Precio": "5.30€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "4",
                "Platos": "26K.Nigiri Tobico 2unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120184354372439.jpg",
                "Precio": "4.80€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "4",
                "Platos": "26L.Nigiri de atún flameado ( 2 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b22740863.png",
                "Precio": "6.00€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "5",
                "Platos": "27.Sashimi variados 15 cortes",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b227410fc.png",
                "Precio": "29.50€",
                "alergias_ids": [2, 8]
            },
            {
                "tipo_id": "5",
                "Platos": "28.Sashimi salmón 6 cortes",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120184450518345.jpg",
                "Precio": "12.95€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "5",
                "Platos": "29.Sashimi atún 6 cortes",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120184456990637.jpg",
                "Precio": "15.90€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "5",
                "Platos": "30A.Sashimi  de salmón (3 Cortes)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b227417b9.png",
                "Precio": "6.20€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "5",
                "Platos": "30B.Sashimi Atún 3cortes",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120184509229107.jpg",
                "Precio": "7.20€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "5",
                "Platos": "30C.Sashimi Pez mantequilla 3cortes",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120184515213949.jpg",
                "Precio": "6.20€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "5",
                "Platos": "31.Tataki de atún semicrudo con aguacate",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b22741bfe.png",
                "Precio": "16.95€",
                "alergias_ids": [1, 8]
            },
            {
                "tipo_id": "5",
                "Platos": "32.Tataki de salmon semicrudo con aguacate",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b246e0b15.png",
                "Precio": "13.95€",
                "alergias_ids": [1, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "33.Rollo tango mango con atún (8 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b246e13a1.png",
                "Precio": "13.45€",
                "alergias_ids": [1, 5, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "35.Maki salmón 8unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120184609804607.jpg",
                "Precio": "7.00€",
                "alergias_ids": [1, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "36.Maki atún 8unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120184616377558.jpg",
                "Precio": "7.60€",
                "alergias_ids": [1, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "37.Rollo pez mantequilla flameando (8 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240518132017877011.jpg",
                "Precio": "11.50€",
                "alergias_ids": [1, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "38.Maki aguacate(8unida)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b246e1f59.png",
                "Precio": "6.40€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "6",
                "Platos": "39.Uramaki anguila ( 8unds)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b246e2405.png",
                "Precio": "13.45€",
                "alergias_ids": [1, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "40.Rollo de arcoiris (8 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20250318224940651132.jpg",
                "Precio": "13.45€",
                "alergias_ids": [1, 2]
            },
            {
                "tipo_id": "6",
                "Platos": "41.Maki mango (8 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b246e2d86.png",
                "Precio": "6.50€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "6",
                "Platos": "42.Maki cebolla frita 8unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120184734283877.jpg",
                "Precio": "9.95€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "6",
                "Platos": "43.Maki pepino  8unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b246e3147.png",
                "Precio": "6.40€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "6",
                "Platos": "44.California Sakura  Rollo  8unds",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20241228160834704682.jpg",
                "Precio": "12.95€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "6",
                "Platos": "45.California  de salmon con sésamo (8 und)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b24fb73d2.png",
                "Precio": "11.00€",
                "alergias_ids": [1, 5, 8, 11]
            },
            {
                "tipo_id": "6",
                "Platos": "46.Uramaki salmón con aguacate y queso ( 8unds)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b24fb7cef.png",
                "Precio": "11.50€",
                "alergias_ids": [1, 5, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "47.Uramaki de atun con aguacate y queso",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b24fb828a.png",
                "Precio": "13.45€",
                "alergias_ids": [1, 5, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "48.Uramaki de pollo crujiente (8 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b24fb88b8.png",
                "Precio": "11.00€",
                "alergias_ids": [1, 3]
            },
            {
                "tipo_id": "6",
                "Platos": "49.Uramaki aguacate con queso ( 8 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b24fb8da9.png",
                "Precio": "10.50€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "6",
                "Platos": "50.Uramaki  langostino frito ( 8 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b24fb92da.png",
                "Precio": "13.45€",
                "alergias_ids": [1, 2]
            },
            {
                "tipo_id": "6",
                "Platos": "50A.Uramaki Dragon rollo (8 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b24fb996e.png",
                "Precio": "13.45€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "6",
                "Platos": "51.Tempura sushi frita (8unds)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b24fb9e76.png",
                "Precio": "11.50€",
                "alergias_ids": [1, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "52.Cheese salmon (8 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20250427154715663989.jpg",
                "Precio": "11.00€",
                "alergias_ids": [1, 5, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "52A.Quemado salmón roll (8 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b26651ced.png",
                "Precio": "14.45€",
                "alergias_ids": [1, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "53.Spicy de salmon (picante）8 unidades",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b26652450.png",
                "Precio": "12.00€",
                "alergias_ids": [1, 8, 15]
            },
            {
                "tipo_id": "6",
                "Platos": "54.Spicy de atún (picante) (8 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2665292f.png",
                "Precio": "13.45€",
                "alergias_ids": [1, 8, 15]
            },
            {
                "tipo_id": "6",
                "Platos": "55.Tobico de salmon ( 8 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b26652f08.png",
                "Precio": "12.00€",
                "alergias_ids": [2, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "56A.Temaki Salmón",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120184843173935.jpg",
                "Precio": "5.30€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "6",
                "Platos": "56B.Temaki Atún",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120184850303090.jpg",
                "Precio": "5.80€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "6",
                "Platos": "56C.Temaki de pez mantequilla",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20250117203939331794.jpg",
                "Precio": "5.30€",
                "alergias_ids": [8]
            },
            {
                "tipo_id": "6",
                "Platos": "56D.Temaki de tempura langostino",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20250117204258512163.png",
                "Precio": "5.30€",
                "alergias_ids": [1, 2]
            },
            {
                "tipo_id": "6",
                "Platos": "57.Tartar de salmón",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b266533e9.png",
                "Precio": "11.90€",
                "alergias_ids": [1, 8]
            },
            {
                "tipo_id": "6",
                "Platos": "58.Tartar de atún",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b26653840.png",
                "Precio": "14.50€",
                "alergias_ids": [1, 8]
            },
            {
                "tipo_id": "7",
                "Platos": "60.Arroz frito tres delicias",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240702223301324249.jpg",
                "Precio": "5.90€",
                "alergias_ids": [3]
            },
            {
                "tipo_id": "7",
                "Platos": "61.Arroz blanco",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b275b5027.png",
                "Precio": "2.70€",
                "alergias_ids": []
            },
            {
                "tipo_id": "7",
                "Platos": "64.Arroz con gambas",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b275b558f.png",
                "Precio": "7.60€",
                "alergias_ids": [2]
            },
            {
                "tipo_id": "7",
                "Platos": "65.Arroz con verdura y salsa de soja",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120185041733368.jpg",
                "Precio": "7.70€",
                "alergias_ids": [1, 4]
            },
            {
                "tipo_id": "7",
                "Platos": "66.Arroz estilo pato laqueado",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240423151514319269.png",
                "Precio": "8.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "7",
                "Platos": "67.Arroz con curry Thai",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120185055162968.jpg",
                "Precio": "7.70€",
                "alergias_ids": [1, 15]
            },
            {
                "tipo_id": "7",
                "Platos": "69.Ku-bak de langostino",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240423151415810145.png",
                "Precio": "9.60€",
                "alergias_ids": [1, 2]
            },
            {
                "tipo_id": "7",
                "Platos": "70.Ku-bak de ternera",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b275b60dd.png",
                "Precio": "9.60€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "7",
                "Platos": "71.Hormigas que suben al arbol",
                "Imagenes": "https://www.restaurantesuma.es/public/images/no-imagen.jpg",
                "Precio": "10.00€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "7",
                "Platos": "72.Chow-main tallarines con gambas",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240620223728583687.jpg",
                "Precio": "8.50€",
                "alergias_ids": [1, 2]
            },
            {
                "tipo_id": "7",
                "Platos": "73.Chow-main tallarines con ternera",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b275b6656.png",
                "Precio": "8.50€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "7",
                "Platos": "74.Yaki Udon tallarines japonesas frito con gambas",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b275b6c03.png",
                "Precio": "9.40€",
                "alergias_ids": [1, 2]
            },
            {
                "tipo_id": "7",
                "Platos": "75.Yaki udon tallarines japoneses con ternera",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b275b7198.png",
                "Precio": "9.40€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "7",
                "Platos": "76.Tallarines teppanyaki",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2838c6f6.png",
                "Precio": "9.30€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "7",
                "Platos": "76A.Yakisoba con verdura",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2838d1f8.png",
                "Precio": "8.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "7",
                "Platos": "77.Pad thai tallarines de la casa",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240620224225516484.png",
                "Precio": "8.80€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "7",
                "Platos": "78.Fideo de arroz con verdura y langostino",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120185216275022.jpg",
                "Precio": "8.90€",
                "alergias_ids": [1, 2]
            },
            {
                "tipo_id": "7",
                "Platos": "79.Fifeos de arroz con verdura y ternera",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2838dd80.png",
                "Precio": "8.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "7",
                "Platos": "80.Fideo chino con pollo",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2838e5e8.png",
                "Precio": "8.60€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "8",
                "Platos": "81.Toufu salteada mapo (poco picante)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2838ec7e.png",
                "Precio": "8.80€",
                "alergias_ids": [1, 4, 15]
            },
            {
                "tipo_id": "8",
                "Platos": "82.Verduras  al wok",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2838f203.png",
                "Precio": "8.80€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "8",
                "Platos": "83.Bambu y seta al salteada",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2838f894.png",
                "Precio": "9.30€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "9",
                "Platos": "84.",
                "Imagenes": "https://www.restaurantesuma.es/public/images/no-imagen.jpg",
                "Precio": "0.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "9",
                "Platos": "85.Ternera al estilo mongolia",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b28d86c8a.png",
                "Precio": "11.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "9",
                "Platos": "86.Ternera con salsa de guindilla(picante)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240517135556152152.png",
                "Precio": "10.90€",
                "alergias_ids": [1, 15]
            },
            {
                "tipo_id": "9",
                "Platos": "87.Ternera teppanyaki",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b28d87caa.png",
                "Precio": "11.95€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "9",
                "Platos": "88.Ternera con bambú y seta",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120185402952063.jpg",
                "Precio": "10.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "9",
                "Platos": "89.Ternera con salsa de ostras",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b28d88214.png",
                "Precio": "10.90€",
                "alergias_ids": [1, 14]
            },
            {
                "tipo_id": "9",
                "Platos": "90.Ternera curry thai",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b28d88868.png",
                "Precio": "10.90€",
                "alergias_ids": [1, 15]
            },
            {
                "tipo_id": "9",
                "Platos": "92.Tira de buey caramelizados",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120185425127191.jpg",
                "Precio": "10.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "9",
                "Platos": "93.Tiras de buey crujiente con salsa agridulce",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b28d88e64.png",
                "Precio": "10.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "9",
                "Platos": "95.Cerdo agridulce",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b28d894b2.png",
                "Precio": "8.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "9",
                "Platos": "96.Cerdo crujiente con sal y pimienta",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b28d89ad3.png",
                "Precio": "8.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "10",
                "Platos": "97.Pollo empanado con patata",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b29618092.png",
                "Precio": "10.20€",
                "alergias_ids": [3]
            },
            {
                "tipo_id": "10",
                "Platos": "98.Bolita de pollo frita(6 unidad)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b29618997.png",
                "Precio": "9.60€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "10",
                "Platos": "99.Pollo tappanyaki",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b29618e72.png",
                "Precio": "11.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "10",
                "Platos": "100.Pollo al curry thai",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120185507935100.jpg",
                "Precio": "10.90€",
                "alergias_ids": [1, 15]
            },
            {
                "tipo_id": "10",
                "Platos": "101.Pollo kon-bao",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b296194e4.png",
                "Precio": "11.20€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "10",
                "Platos": "102.Turrón de pollo",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240517134505915371.jpg",
                "Precio": "10.90€",
                "alergias_ids": [3]
            },
            {
                "tipo_id": "10",
                "Platos": "103.Pollo al limón",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120185533857273.jpg",
                "Precio": "10.90€",
                "alergias_ids": [3]
            },
            {
                "tipo_id": "10",
                "Platos": "104.Pollo almendra con verduras",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b29619eaa.png",
                "Precio": "10.90€",
                "alergias_ids": [1, 6]
            },
            {
                "tipo_id": "10",
                "Platos": "105.Teppanyaki de pollo al estilo cantones",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2961a524.png",
                "Precio": "10.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "10",
                "Platos": "106.Pollo con salsa de guindilla(picante)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2961aa9c.png",
                "Precio": "10.90€",
                "alergias_ids": [1, 15]
            },
            {
                "tipo_id": "10",
                "Platos": "106A.Pollo escalfado con vinagreta china (con picante o sin picante)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20251126162007987744.jpg",
                "Precio": "10.90€",
                "alergias_ids": [1, 15]
            },
            {
                "tipo_id": "10",
                "Platos": "107.Pollo con salsa teriyaki japonesa",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2a542854.png",
                "Precio": "11.80€",
                "alergias_ids": [1, 4]
            },
            {
                "tipo_id": "10",
                "Platos": "108.Pollo caramelizado con soja",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120185551411836.jpg",
                "Precio": "10.90€",
                "alergias_ids": [1, 4]
            },
            {
                "tipo_id": "10",
                "Platos": "109.Tiras de pollo en salsa sate(picante)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2a5430ff.png",
                "Precio": "10.90€",
                "alergias_ids": [1, 9, 15]
            },
            {
                "tipo_id": "10",
                "Platos": "109A.Tira de pollo frito",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2a5437ac.png",
                "Precio": "10.90€",
                "alergias_ids": [3]
            },
            {
                "tipo_id": "10",
                "Platos": "110.Pato frito crujiente",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120185638441473.jpg",
                "Precio": "12.50€",
                "alergias_ids": []
            },
            {
                "tipo_id": "10",
                "Platos": "111.Pato crujiente con salsa naranja",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120185706276637.jpg",
                "Precio": "12.50€",
                "alergias_ids": []
            },
            {
                "tipo_id": "10",
                "Platos": "112.Pato pekines",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2a543c2c.png",
                "Precio": "16.50€",
                "alergias_ids": [3]
            },
            {
                "tipo_id": "10",
                "Platos": "113.Pato teppanyaki",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2a5440d3.png",
                "Precio": "12.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "10",
                "Platos": "113A.Pato con bambu y seta",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2a54479e.png",
                "Precio": "12.40€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "11",
                "Platos": "115.Langostino con  bambu y seta",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20230905214221314323.jpg",
                "Precio": "12.40€",
                "alergias_ids": [1, 2]
            },
            {
                "tipo_id": "11",
                "Platos": "116.Langostino curry al estilo thai",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20150120185736317011.jpg",
                "Precio": "12.90€",
                "alergias_ids": [1, 2, 15]
            },
            {
                "tipo_id": "11",
                "Platos": "117.Langostino con verdura al wok",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2a544c1d.png",
                "Precio": "11.40€",
                "alergias_ids": [1, 2]
            },
            {
                "tipo_id": "11",
                "Platos": "119.Langostinos con salsa de guindilla(picante)",
                "Imagenes": "https://www.restaurantesuma.es/public/images/no-imagen.jpg",
                "Precio": "12.40€",
                "alergias_ids": [1, 2, 15]
            },
            {
                "tipo_id": "11",
                "Platos": "120.Chipirones Teppanyaki",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516222228469432.jpg",
                "Precio": "12.90€",
                "alergias_ids": [1, 14]
            },
            {
                "tipo_id": "11",
                "Platos": "121.Chipirónes con salsa de ostra",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516222213123969.jpg",
                "Precio": "12.90€",
                "alergias_ids": [1, 14]
            },
            {
                "tipo_id": "11",
                "Platos": "122.Chipirones con salsa de guindilla(picante）",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516222303643486.jpg",
                "Precio": "12.90€",
                "alergias_ids": [1, 14, 15]
            },
            {
                "tipo_id": "12",
                "Platos": "Bandeja 1 (14P)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20160427123015300527.jpg",
                "Precio": "14.95€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "12",
                "Platos": "Bandeja 2 (22P)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20160427123148952701.jpg",
                "Precio": "26.95€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "12",
                "Platos": "Bandeja 3 (30P)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20160427123121408514.jpg",
                "Precio": "43.90€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "12",
                "Platos": "Bandeja 4 (36P)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20250509221200555503.jpg",
                "Precio": "53.00€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "12",
                "Platos": "BANDEJA 5 (16P)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20180923024804998885.jpg",
                "Precio": "29.00€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "12",
                "Platos": "BANDEJA 6 (38P)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240423150909227883.png",
                "Precio": "62.00€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "13",
                "Platos": "MENÚ SUMO ( 2 PERSONAS)",
                "Imagenes": "https://www.restaurantesuma.es/public/images/no-imagen.jpg",
                "Precio": "36.95€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "13",
                "Platos": "MENÚ BAMBÚ ( 3 PERSONAS)",
                "Imagenes": "https://www.restaurantesuma.es/public/images/no-imagen.jpg",
                "Precio": "54.95€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "13",
                "Platos": "MENÚ FUSIÓN (4 PERSONAS)",
                "Imagenes": "https://www.restaurantesuma.es/public/images/no-imagen.jpg",
                "Precio": "68.95€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "13",
                "Platos": "MENU ASIATICO ( para 6 personas)",
                "Imagenes": "https://www.restaurantesuma.es/public/images/no-imagen.jpg",
                "Precio": "125.45€",
                "Alergia": "https://www.restaurantesuma.es/public/images/allergy_icons/1.png",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "13",
                "Platos": "MENÚ TOKIO ( 2 PERSONAS)",
                "Imagenes": "https://www.restaurantesuma.es/public/images/no-imagen.jpg",
                "Precio": "49.95€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "14",
                "Platos": "VINO DE LA CASA, RIOJA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516225159400477.jpg",
                "Precio": "12.00€",
                "alergias_ids": [12]
            },
            {
                "tipo_id": "14",
                "Platos": "CUNE CRIANZA Y RIOJA½",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516225044182968.jpg",
                "Precio": "11.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "CUNE CRIANZA Y RIOJA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516225028169214.jpg",
                "Precio": "17.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "VIÑA ALCORTA CRIANZA, RIOJA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516224942146819.jpg",
                "Precio": "19.90€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "VIÑA MAYOR ROBLE, RIBERA DEL DUERO",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516223959489206.jpg",
                "Precio": "17.50€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "MARQUÉS DE CÁCERES CRIANZA, RIOJA½",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516223748406962.jpg",
                "Precio": "11.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "MARQUÉS DE CÁCERES CRIANZA, RIOJA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516223652549572.jpg",
                "Precio": "17.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "MUGA CRIANZA, RIOJA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516223605974698.jpg",
                "Precio": "37.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "RAMON BILBAO CRIANZA RIOJA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516222853736391.jpg",
                "Precio": "19.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "PROTO ROBLE",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516224535394050.jpg",
                "Precio": "17.80€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "PROTOS CRIANZA, RIBERA DEL DUERO",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516223511723175.jpg",
                "Precio": "24.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "PRUNO 2021 ( RIBERA DEL DUERO)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20250207131225538003.jpg",
                "Precio": "19.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "FINCA CONSTANCIA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516223228381321.jpg",
                "Precio": "16.50€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "PAGO DEL VICARIO 50-50 (TIERRA DE CATILLA )",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20250207130110252078.png",
                "Precio": "18.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "14",
                "Platos": "ALCARDET",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240518134002565996.png",
                "Precio": "13.95€",
                "alergias_ids": []
            },
            {
                "tipo_id": "15",
                "Platos": "Pinuaga Rose 2023",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240620225450772294.jpg",
                "Precio": "16.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "15",
                "Platos": "PEÑASCAL, VALLADOLID",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516225643598556.jpg",
                "Precio": "13.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "15",
                "Platos": "MATEU ROSE, PORTUGAL",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516225609423690.jpg",
                "Precio": "14.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "15",
                "Platos": "LAMBRUSCO, ITALIA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516225453760985.jpg",
                "Precio": "12.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "15",
                "Platos": "GRAN FEUDO, NAYARRA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516225341227768.jpg",
                "Precio": "12.50€",
                "alergias_ids": []
            },
            {
                "tipo_id": "16",
                "Platos": "BLANCO NIEVA MARTUE 2023 VERDEJO RUEDA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240529132238629579.png",
                "Precio": "14.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "16",
                "Platos": "PALACIO DE BORNOS FRIZZANTE VERDEJO (semidulce)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240529133012116268.jpg",
                "Precio": "16.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "16",
                "Platos": "QUINTA DE AVES MUSCAT VOLCANICO 2023 ( 100% MOSCATEL )",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240620224742226630.png",
                "Precio": "16.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "16",
                "Platos": "PACO Y LOLA ALBARINO",
                "Imagenes": "https://www.restaurantesuma.es/public/images/no-imagen.jpg",
                "Precio": "16.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "16",
                "Platos": "BARBADILLO",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240518134913270851.jpg",
                "Precio": "13.80€",
                "alergias_ids": []
            },
            {
                "tipo_id": "16",
                "Platos": "BLANCO DE LA CASA, RUEDA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516225910117860.jpg",
                "Precio": "12.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "16",
                "Platos": "CORPUS DEL MUNI  (SEMIDULCE)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516230217355405.jpg",
                "Precio": "16.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "16",
                "Platos": "MARTÍN CÓDAX ALBARIÑO, RÍAS BAIXAS",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516230347717787.jpg",
                "Precio": "25.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "16",
                "Platos": "DIAMANTE ( SEMIDULCE)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240908203900550614.jpg",
                "Precio": "15.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "17",
                "Platos": "JARRA½",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516231145817893.jpg",
                "Precio": "6.50€",
                "alergias_ids": []
            },
            {
                "tipo_id": "17",
                "Platos": "JARRA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516231135317393.jpg",
                "Precio": "9.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "18",
                "Platos": "ALCARDET BRUT 36MESES",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516231317827544.jpg",
                "Precio": "18.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "19",
                "Platos": "MAHOU",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516232105174153.jpg",
                "Precio": "2.90€",
                "alergias_ids": []
            },
            {
                "tipo_id": "19",
                "Platos": "MAHOU TOSTADA 0%",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516232036833124.jpg",
                "Precio": "2.90€",
                "alergias_ids": []
            },
            {
                "tipo_id": "19",
                "Platos": "CERVEZA JAPONESA KIRIN, SAPPORO, O ASAHÍ",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516232002705766.jpg",
                "Precio": "3.50€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "19",
                "Platos": "CERVEZA CHINA TSING-TAO",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516231856501430.jpg",
                "Precio": "3.50€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "19",
                "Platos": "CERVEZA TAILANDESA SINGA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516231804253056.jpg",
                "Precio": "3.50€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "20",
                "Platos": "AGUA MINERAL",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516231720943953.jpg",
                "Precio": "2.20€",
                "alergias_ids": []
            },
            {
                "tipo_id": "20",
                "Platos": "AGUA CON GAS SOLAR",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516231625812164.jpg",
                "Precio": "2.60€",
                "alergias_ids": []
            },
            {
                "tipo_id": "20",
                "Platos": "COCA COLA, FANTA LIMÓN Y NARANJA, SPRITE, TÓNICA, AQUARIUS, NESTEA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516231539987329.jpg",
                "Precio": "2.90€",
                "alergias_ids": []
            },
            {
                "tipo_id": "20",
                "Platos": "ZUMO DE FRUTA",
                "Imagenes": "https://www.restaurantesuma.es/public/images/no-imagen.jpg",
                "Precio": "2.25€",
                "alergias_ids": []
            },
            {
                "tipo_id": "20",
                "Platos": "ZUMO DE NARANJA NATURAL",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516231428287187.jpg",
                "Precio": "3.80€",
                "alergias_ids": []
            },
            {
                "tipo_id": "21",
                "Platos": "SAKE JARRA, CALIENTE O FRÍO",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516232329283593.jpg",
                "Precio": "8.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "21",
                "Platos": "SAKE JAPÓN SHOGUN (BOTELLA) FRÍO ( 180ML)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516232230901845.jpg",
                "Precio": "10.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "21",
                "Platos": "SAKE JAPÓN NAMA-CHOZO (300ML)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516232153581534.jpg",
                "Precio": "15.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "22",
                "Platos": "LICORES ORIENTALES, CHOYA, FLORES O  GAOLIAN",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516233937963409.jpg",
                "Precio": "3.50€",
                "alergias_ids": []
            },
            {
                "tipo_id": "22",
                "Platos": "LICORES DE  PACHARÁN, HIERBAS, ORUJO CREMA O  LIMONCHELO",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516233730305481.jpg",
                "Precio": "4.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "22",
                "Platos": "WHISKY , VODKA O  COÑA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516233503683915.jpg",
                "Precio": "4.50€",
                "alergias_ids": []
            },
            {
                "tipo_id": "22",
                "Platos": "COMBINADOS",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516233007147118.jpg",
                "Precio": "5.50€",
                "alergias_ids": []
            },
            {
                "tipo_id": "22",
                "Platos": "MARTINI Y SIMILARES",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516232727306988.jpg",
                "Precio": "4.50€",
                "alergias_ids": []
            },
            {
                "tipo_id": "22",
                "Platos": "AMARETTO, BAILEY´S, 0  FRANGELICO",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516232625400130.jpg",
                "Precio": "4.80€",
                "alergias_ids": []
            },
            {
                "tipo_id": "22",
                "Platos": "WHISKY ESPECIAL",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516233049922560.jpg",
                "Precio": "6.50€",
                "alergias_ids": []
            },
            {
                "tipo_id": "23",
                "Platos": "TÉ VERDE",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516234851502777.jpg",
                "Precio": "2.10€",
                "alergias_ids": []
            },
            {
                "tipo_id": "23",
                "Platos": "TÉ VERDE, ROJO , NEGRO,  MANZANILLA O MENTA POLEO",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516234734666432.jpg",
                "Precio": "2.10€",
                "alergias_ids": []
            },
            {
                "tipo_id": "23",
                "Platos": "TÉ ARROZ",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516234432495475.jpg",
                "Precio": "2.50€",
                "alergias_ids": []
            },
            {
                "tipo_id": "23",
                "Platos": "CAFÉ",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516235723483977.jpg",
                "Precio": "1.90€",
                "alergias_ids": []
            },
            {
                "tipo_id": "23",
                "Platos": "CAFÉ BOMBÓN, CAPPUCCINO",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516235650389320.jpg",
                "Precio": "4.20€",
                "alergias_ids": []
            },
            {
                "tipo_id": "23",
                "Platos": "CAFÉ IRLANDÉS",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516235518325082.jpg",
                "Precio": "4.90€",
                "alergias_ids": []
            },
            {
                "tipo_id": "23",
                "Platos": "CARAJILLO",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240516235440311403.jpg",
                "Precio": "3.40€",
                "alergias_ids": []
            },
            {
                "tipo_id": "24",
                "Platos": "(AUTÉNTICO YEN SEN NATURAL VAPORIZADO CON BAYA DE GOJI Y MIEL) (AFRODISIACO Y ANTIOXIDANTE)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240517000010632311.jpg",
                "Precio": "6.00€",
                "alergias_ids": []
            },
            {
                "tipo_id": "25",
                "Platos": "800C.Trufa té verde (6 piezas)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2b055ec3.png",
                "Precio": "4.55€",
                "alergias_ids": [3]
            },
            {
                "tipo_id": "25",
                "Platos": "833.Plátano frito ( 2 piezas)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2c582f07.png",
                "Precio": "3.55€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "25",
                "Platos": "831.Helado frito",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2c5823de.png",
                "Precio": "4.35€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "836.Bola helado",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2d4266cd.png",
                "Precio": "3.25€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "837.Helado doble",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20220709161324799555.jpg",
                "Precio": "4.65€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "839.Flan chino mandarín vanilla",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2d426f3a.png",
                "Precio": "2.25€",
                "alergias_ids": [1, 3, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "839A.Flan con nata",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2d427576.png",
                "Precio": "4.25€",
                "alergias_ids": [1, 3, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "839B.Flan con nata y nueces",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2d427a7c.png",
                "Precio": "5.05€",
                "alergias_ids": [1, 3, 5, 6]
            },
            {
                "tipo_id": "25",
                "Platos": "807.Maxibon",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20220709162431752905.png",
                "Precio": "3.00€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "827.Nuii almendrado",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2c581810.png",
                "Precio": "3.00€",
                "alergias_ids": [3]
            },
            {
                "tipo_id": "25",
                "Platos": "808.Fantasmikos pirulo",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2b85f48d.png",
                "Precio": "2.50€",
                "alergias_ids": [3]
            },
            {
                "tipo_id": "25",
                "Platos": "829.Bombones",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2c581e0f.png",
                "Precio": "4.50€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "832.Trufa chocolates ( 5 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2c5828a0.png",
                "Precio": "6.00€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "802.Brownie con nueces con helado de vanilla",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2b85e7f9.png",
                "Precio": "5.50€",
                "alergias_ids": [1, 5, 6]
            },
            {
                "tipo_id": "25",
                "Platos": "801.Tarta de chocolate",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2b056353.png",
                "Precio": "4.10€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "830.Tarta queso Gourmet",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240423151610468642.png",
                "Precio": "4.10€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "814.Tarta al whisky",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20240430103303977793.jpg",
                "Precio": "4.50€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "816.Mini carolina",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2b8607de.png",
                "Precio": "3.50€",
                "alergias_ids": [1]
            },
            {
                "tipo_id": "25",
                "Platos": "843.Bolita de sésamo (5 unidades)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2d428539.png",
                "Precio": "3.85€",
                "alergias_ids": [1, 11]
            },
            {
                "tipo_id": "25",
                "Platos": "835.Pancakes con helado",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2c58338a.png",
                "Precio": "5.90€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "813.Crema Quemada",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2b86024b.png",
                "Precio": "5.20€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "817.Coco helado",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2b860d98.png",
                "Precio": "6.60€",
                "alergias_ids": [5]
            },
            {
                "tipo_id": "25",
                "Platos": "809.La tentagioni caffe",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2b85fa55.png",
                "Precio": "5.00€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "810.La tentagioni panna e cioccolato",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2b85fe4a.png",
                "Precio": "5.00€",
                "alergias_ids": [5]
            },
            {
                "tipo_id": "25",
                "Platos": "818.Limón helado",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2c580be9.png",
                "Precio": "5.50€",
                "alergias_ids": [5]
            },
            {
                "tipo_id": "25",
                "Platos": "806.COPA OREO",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20250504204125298636.jpg",
                "Precio": "4.80€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "805.VASO HUEVO LACASITOS",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20241031131555596882.jpg",
                "Precio": "4.80€",
                "alergias_ids": [3, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "812.COPA MILKA",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/20241126163213695381.png",
                "Precio": "4.80€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "800.Mochi helado (2 bola)",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2b0559d6.png",
                "Precio": "4.55€",
                "alergias_ids": [1, 5]
            },
            {
                "tipo_id": "25",
                "Platos": "840.Mousse de chocolate o limon",
                "Imagenes": "https://www.restaurantesuma.es/public/uploadfile/6627b2d4280a9.png",
                "Precio": "3.65€",
                "alergias_ids": [5]
            }
        ]

        # 3. PROCESAR Y GUARDAR
        for item in datos_json:
            nombre = item["Platos"]
            precio = item["Precio"]
            imagen = item["Imagenes"]
            tipo_id = item["tipo_id"]
            # Obtenemos los IDs, si no tiene, usamos lista vacía
            ids_alergias = item.get("alergias_ids", [])

            # Buscamos si el plato ya existe o lo creamos nuevo
            plato, created = Suma.objects.get_or_create(
                Platos=nombre,
                defaults={
                    'Precio': precio,
                    'Imagenes': imagen,
                    'tipo_id': tipo_id
                }
            )

            # Si ya existía, actualizamos sus datos por si han cambiado
            if not created:
                plato.Precio = precio
                plato.Imagenes = imagen
                plato.tipo_id = tipo_id
                plato.save()

            # ASIGNAR ALERGIAS (Relación ManyToMany)
            # Primero limpiamos las que tuviera para evitar duplicados
            plato.alergias.clear() 
            
            # Añadimos las nuevas según el array de IDs
            for al_id in ids_alergias:
                if Alergias.objects.filter(id=al_id).exists():
                    plato.alergias.add(al_id)
            
            estado = "Creado" if created else "Actualizado"
            self.stdout.write(f"{estado}: {nombre} - IDs Alergias: {ids_alergias}")

        self.stdout.write(self.style.SUCCESS('¡Carga completada exitosamente!'))