from app import db
from app.models import Category, MenuItem

MENU_DATA = {
    "Entrées 前菜": [
        ("Foie Gras & Char Siu Terrine", "French foie gras layered with Cantonese char siu, brioche toast, plum gastrique", 18.00, True),
        ("Scallop Congee Velouté", "Silky rice velouté, seared Hokkaido scallop, truffle oil, crispy shallots", 16.00, True),
        ("Peking Duck Rillettes", "Slow-confit duck, hoisin cream, cucumber, sesame tuile", 15.00, False),
        ("Wonton Consommé", "Crystal-clear French consommé, prawn & ginger wontons, chervil", 12.00, False),
    ],
    "Plats Principaux 主菜": [
        ("Five-Spice Duck Confit", "French confit technique, five-spice rub, cherry-Shaoxing jus, dauphinoise potato", 46.00, True),
        ("Lobster Mapo Tofu", "Butter-poached lobster, silken tofu, Sichuan doubanjiang beurre blanc", 54.00, True),
        ("Wagyu Beef Tenderloin", "Black pepper & oyster sauce glaze, pommes purée, wok-charred broccolini", 62.00, True),
        ("Steamed Sea Bass en Papillote", "Ginger, scallion, soy beurre blanc, julienne vegetables, jasmine rice", 38.00, False),
        ("Mushroom & Black Truffle Fried Rice", "Arborio-style wok rice, black truffle, shiitake, parmesan foam", 32.00, False),
    ],
    "Desserts 甜点": [
        ("Jasmine Crème Brûlée", "Jasmine tea–infused custard, caramelised sugar, sesame praline", 13.00, True),
        ("Red Bean Mille-Feuille", "Flaky puff pastry, sweetened red bean, jasmine Chantilly cream", 14.00, True),
        ("Matcha Fondant", "Warm matcha chocolate cake, vanilla bean gelato, gold leaf", 15.00, False),
        ("Lychee Panna Cotta", "Coconut panna cotta, lychee coulis, rose water jelly", 11.00, False),
    ],
    "Boissons 饮品": [
        ("Shaoxing Sour", "Aged Shaoxing wine, lemon, honey, egg white foam", 14.00, False),
        ("Lychee Champagne Royale", "Moët & Chandon, lychee liqueur, rose petal", 18.00, False),
        ("Pu-erh Old Fashioned", "Bourbon infused with aged Pu-erh tea, orange bitters", 15.00, False),
        ("Chrysanthemum Spritz", "Chrysanthemum tea, elderflower, sparkling water", 8.00, False),
    ],
}

IMAGES = {
    "Foie Gras & Char Siu Terrine": "https://images.unsplash.com/photo-1608897013039-887f21d8c804?w=600",
    "Scallop Congee Velouté": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=600",
    "Peking Duck Rillettes": "https://images.unsplash.com/photo-1544025162-d76694265947?w=600",
    "Wonton Consommé": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600",
    "Five-Spice Duck Confit": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600",
    "Lobster Mapo Tofu": "https://images.unsplash.com/photo-1563379926898-05f4575a45d8?w=600",
    "Wagyu Beef Tenderloin": "https://images.unsplash.com/photo-1558030006-450675393462?w=600",
    "Steamed Sea Bass en Papillote": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=600",
    "Mushroom & Black Truffle Fried Rice": "https://images.unsplash.com/photo-1476124369491-e7addf5db371?w=600",
    "Jasmine Crème Brûlée": "https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc?w=600",
    "Red Bean Mille-Feuille": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=600",
    "Matcha Fondant": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=600",
    "Lychee Panna Cotta": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600",
    "Shaoxing Sour": "https://images.unsplash.com/photo-1551538827-9c037cb4f32a?w=600",
    "Lychee Champagne Royale": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600",
    "Pu-erh Old Fashioned": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=600",
    "Chrysanthemum Spritz": "https://images.unsplash.com/photo-1548839140-29a749e1cf4d?w=600",
}


def seed_db():
    if Category.query.first():
        return  # already seeded, skip
    for cat_name, items in MENU_DATA.items():
        cat = Category(name=cat_name)
        db.session.add(cat)
        db.session.flush()
        for name, desc, price, featured in items:
            db.session.add(MenuItem(
                name=name,
                description=desc,
                price=price,
                featured=featured,
                image_url=IMAGES.get(name, ""),
                category_id=cat.id,
            ))
    db.session.commit()
    print("Database seeded with French-Chinese fusion menu.")
