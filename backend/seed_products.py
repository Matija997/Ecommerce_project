import json
from app import app
from extensions import db
from models.product import Product

FRONTEND = 'http://localhost:5173'


def picsum(seed, w=700, h=900):
    return f'https://picsum.photos/seed/{seed}/{w}/{h}'


def picsum_gallery(base_seed, count=3):
    return [picsum(f'{base_seed}-{n}') for n in range(1, count + 1)]


def sizes_for(labels):
    return [{'size': label, 'available': True} for label in labels]


PRODUCTS = [
    # ---- Man / Clothing ----
    dict(name='Boxy Wool Overcoat', category='man', type='clothing', subtype='jacket',
         price=22110, sale_price=None, tag='New',
         images=picsum_gallery('friso-m01'),
         sizes=sizes_for(['S', 'M', 'L', 'XL'])),
    dict(name='Logo Graphic Tee', category='man', type='clothing', subtype='tshirt',
         price=5990, sale_price=None, tag='New',
         images=[f'{FRONTEND}/products/t-shirt.png'] * 3,
         sizes=sizes_for(['S', 'M', 'L', 'XL', 'XXL'])),
    dict(name='Cobalt Sport Tee', category='man', type='clothing', subtype='tshirt',
         price=4990, sale_price=3490, tag='Sale',
         images=[f'{FRONTEND}/products/nike-tshirt.jpg'] * 3,
         sizes=sizes_for(['S', 'M', 'L', 'XL'])),
    dict(name='Denim Trucker Jacket', category='man', type='clothing', subtype='denim',
         price=14980, sale_price=10410, tag='Sale',
         images=picsum_gallery('friso-m04'),
         sizes=sizes_for(['S', 'M', 'L', 'XL'])),
    dict(name='Straight Fit Jeans', category='man', type='clothing', subtype='denim',
         price=9990, sale_price=None, tag=None,
         images=picsum_gallery('friso-m05-denim'),
         sizes=sizes_for(['28', '30', '32', '34', '36'])),
    dict(name='Utility Field Jacket', category='man', type='clothing', subtype='jacket',
         price=13990, sale_price=None, tag=None,
         images=picsum_gallery('friso-m06-jacket'),
         sizes=sizes_for(['S', 'M', 'L', 'XL'])),

    # ---- Man / Accessories ----
    dict(name='Two-Tone Baseball Cap', category='man', type='accessories', subtype='hats',
         price=3490, sale_price=None, tag=None,
         images=[f'{FRONTEND}/products/cap.png'] * 3,
         sizes=sizes_for(['One Size'])),
    dict(name='Canvas Crossbody Bag', category='man', type='accessories', subtype='bags',
         price=7990, sale_price=None, tag=None,
         images=[f'{FRONTEND}/products/bag.png'] * 3,
         sizes=sizes_for(['One Size'])),
    dict(name='Aviator Sunglasses', category='man', type='accessories', subtype='glasses',
         price=6990, sale_price=None, tag='New',
         images=picsum_gallery('friso-m09-glasses'),
         sizes=sizes_for(['One Size'])),

    # ---- Woman / Clothing ----
    dict(name='Boxy Cropped Tee', category='woman', type='clothing', subtype='tshirt',
         price=5490, sale_price=None, tag='New',
         images=picsum_gallery('friso-w01-tee'),
         sizes=sizes_for(['XS', 'S', 'M', 'L'])),
    dict(name='Ribbed Longline Tee', category='woman', type='clothing', subtype='tshirt',
         price=6320, sale_price=4450, tag='Sale',
         images=picsum_gallery('friso-w04'),
         sizes=sizes_for(['XS', 'S', 'M', 'L'])),
    dict(name='Cropped Tailored Blazer', category='woman', type='clothing', subtype='jacket',
         price=18250, sale_price=12750, tag='Sale',
         images=picsum_gallery('friso-w02'),
         sizes=sizes_for(['XS', 'S', 'M', 'L'])),
    dict(name='Oversized Camel Coat', category='woman', type='clothing', subtype='jacket',
         price=24570, sale_price=None, tag='New',
         images=picsum_gallery('friso-w05'),
         sizes=sizes_for(['XS', 'S', 'M', 'L'])),
    dict(name='High-Rise Wide Denim', category='woman', type='clothing', subtype='denim',
         price=11470, sale_price=None, tag=None,
         images=picsum_gallery('friso-w03'),
         sizes=sizes_for(['24', '26', '28', '30', '32'])),
    dict(name='Oversized Denim Jacket', category='woman', type='clothing', subtype='denim',
         price=15990, sale_price=None, tag='New',
         images=picsum_gallery('friso-w06-denim'),
         sizes=sizes_for(['XS', 'S', 'M', 'L'])),

    # ---- Woman / Accessories ----
    dict(name='Structured Tote Bag', category='woman', type='accessories', subtype='bags',
         price=10990, sale_price=None, tag=None,
         images=[f'{FRONTEND}/products/bag.png'] * 3,
         sizes=sizes_for(['One Size'])),
    dict(name='Classic Ball Cap', category='woman', type='accessories', subtype='hats',
         price=4990, sale_price=None, tag=None,
         images=[f'{FRONTEND}/products/cap.png'] * 3,
         sizes=sizes_for(['One Size'])),
    dict(name='Cat-Eye Sunglasses', category='woman', type='accessories', subtype='glasses',
         price=7490, sale_price=None, tag=None,
         images=picsum_gallery('friso-w09-glasses'),
         sizes=sizes_for(['One Size'])),
]

with app.app_context():
    # Drop only the products table (schema changed) — leaves users untouched.
    Product.__table__.drop(db.engine, checkfirst=True)
    db.create_all()

    for data in PRODUCTS:
        db.session.add(Product(
            name=data['name'],
            category=data['category'],
            type=data['type'],
            subtype=data['subtype'],
            price=data['price'],
            sale_price=data['sale_price'],
            tag=data['tag'],
            images=json.dumps(data['images']),
            sizes=json.dumps(data['sizes'])
        ))
    db.session.commit()
    print(f'Seeded {len(PRODUCTS)} products.')
