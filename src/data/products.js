import tshirtImg from '../assets/t-shirt.png'
import nikeTshirtImg from '../assets/NikeT-shirt.jpg'
import capImg from '../assets/cap.png'
import bagImg from '../assets/bag.png'

function img(seed, w = 700, h = 900) {
  return `https://picsum.photos/seed/${seed}/${w}/${h}`
}

export const products = [
  // ---- Man / Clothing ----
  {
    id: 'm01',
    name: 'Boxy Wool Overcoat',
    category: 'man',
    type: 'clothing',
    subtype: 'jacket',
    price: 22110,
    salePrice: null,
    tag: 'New',
    image: img('friso-m01-a'),
    imageAlt: img('friso-m01-b'),
    sizes: ['S', 'M', 'L', 'XL']
  },
  {
    id: 'm02',
    name: 'Logo Graphic Tee',
    category: 'man',
    type: 'clothing',
    subtype: 'tshirt',
    price: 5990,
    salePrice: null,
    tag: 'New',
    image: tshirtImg,
    imageAlt: tshirtImg,
    sizes: ['S', 'M', 'L', 'XL', 'XXL']
  },
  {
    id: 'm03',
    name: 'Cobalt Sport Tee',
    category: 'man',
    type: 'clothing',
    subtype: 'tshirt',
    price: 4990,
    salePrice: 3490,
    tag: 'Sale',
    image: nikeTshirtImg,
    imageAlt: nikeTshirtImg,
    sizes: ['S', 'M', 'L', 'XL']
  },
  {
    id: 'm04',
    name: 'Denim Trucker Jacket',
    category: 'man',
    type: 'clothing',
    subtype: 'denim',
    price: 14980,
    salePrice: 10410,
    tag: 'Sale',
    image: img('friso-m04-a'),
    imageAlt: img('friso-m04-b'),
    sizes: ['S', 'M', 'L', 'XL']
  },
  {
    id: 'm05',
    name: 'Straight Fit Jeans',
    category: 'man',
    type: 'clothing',
    subtype: 'denim',
    price: 9990,
    salePrice: null,
    tag: null,
    image: img('friso-m05-denim-a'),
    imageAlt: img('friso-m05-denim-b'),
    sizes: ['28', '30', '32', '34', '36']
  },
  {
    id: 'm06',
    name: 'Utility Field Jacket',
    category: 'man',
    type: 'clothing',
    subtype: 'jacket',
    price: 13990,
    salePrice: null,
    tag: null,
    image: img('friso-m06-jacket-a'),
    imageAlt: img('friso-m06-jacket-b'),
    sizes: ['S', 'M', 'L', 'XL']
  },

  // ---- Man / Accessories ----
  {
    id: 'm07',
    name: 'Two-Tone Baseball Cap',
    category: 'man',
    type: 'accessories',
    subtype: 'hats',
    price: 3490,
    salePrice: null,
    tag: null,
    image: capImg,
    imageAlt: capImg,
    sizes: ['One Size']
  },
  {
    id: 'm08',
    name: 'Canvas Crossbody Bag',
    category: 'man',
    type: 'accessories',
    subtype: 'bags',
    price: 7990,
    salePrice: null,
    tag: null,
    image: bagImg,
    imageAlt: bagImg,
    sizes: ['One Size']
  },
  {
    id: 'm09',
    name: 'Aviator Sunglasses',
    category: 'man',
    type: 'accessories',
    subtype: 'glasses',
    price: 6990,
    salePrice: null,
    tag: 'New',
    image: img('friso-m09-glasses-a'),
    imageAlt: img('friso-m09-glasses-b'),
    sizes: ['One Size']
  },

  // ---- Woman / Clothing ----
  {
    id: 'w01',
    name: 'Boxy Cropped Tee',
    category: 'woman',
    type: 'clothing',
    subtype: 'tshirt',
    price: 5490,
    salePrice: null,
    tag: 'New',
    image: img('friso-w01-tee-a'),
    imageAlt: img('friso-w01-tee-b'),
    sizes: ['XS', 'S', 'M', 'L']
  },
  {
    id: 'w02',
    name: 'Ribbed Longline Tee',
    category: 'woman',
    type: 'clothing',
    subtype: 'tshirt',
    price: 6320,
    salePrice: 4450,
    tag: 'Sale',
    image: img('friso-w04-a'),
    imageAlt: img('friso-w04-b'),
    sizes: ['XS', 'S', 'M', 'L']
  },
  {
    id: 'w03',
    name: 'Cropped Tailored Blazer',
    category: 'woman',
    type: 'clothing',
    subtype: 'jacket',
    price: 18250,
    salePrice: 12750,
    tag: 'Sale',
    image: img('friso-w02-a'),
    imageAlt: img('friso-w02-b'),
    sizes: ['XS', 'S', 'M', 'L']
  },
  {
    id: 'w04',
    name: 'Oversized Camel Coat',
    category: 'woman',
    type: 'clothing',
    subtype: 'jacket',
    price: 24570,
    salePrice: null,
    tag: 'New',
    image: img('friso-w05-a'),
    imageAlt: img('friso-w05-b'),
    sizes: ['XS', 'S', 'M', 'L']
  },
  {
    id: 'w05',
    name: 'High-Rise Wide Denim',
    category: 'woman',
    type: 'clothing',
    subtype: 'denim',
    price: 11470,
    salePrice: null,
    tag: null,
    image: img('friso-w03-a'),
    imageAlt: img('friso-w03-b'),
    sizes: ['24', '26', '28', '30', '32']
  },
  {
    id: 'w06',
    name: 'Oversized Denim Jacket',
    category: 'woman',
    type: 'clothing',
    subtype: 'denim',
    price: 15990,
    salePrice: null,
    tag: 'New',
    image: img('friso-w06-denim-a'),
    imageAlt: img('friso-w06-denim-b'),
    sizes: ['XS', 'S', 'M', 'L']
  },

  // ---- Woman / Accessories ----
  {
    id: 'w07',
    name: 'Structured Tote Bag',
    category: 'woman',
    type: 'accessories',
    subtype: 'bags',
    price: 10990,
    salePrice: null,
    tag: null,
    image: bagImg,
    imageAlt: bagImg,
    sizes: ['One Size']
  },
  {
    id: 'w08',
    name: 'Classic Ball Cap',
    category: 'woman',
    type: 'accessories',
    subtype: 'hats',
    price: 4990,
    salePrice: null,
    tag: null,
    image: capImg,
    imageAlt: capImg,
    sizes: ['One Size']
  },
  {
    id: 'w09',
    name: 'Cat-Eye Sunglasses',
    category: 'woman',
    type: 'accessories',
    subtype: 'glasses',
    price: 7490,
    salePrice: null,
    tag: null,
    image: img('friso-w09-glasses-a'),
    imageAlt: img('friso-w09-glasses-b'),
    sizes: ['One Size']
  }
]

export function getByCategory(category) {
  return products.filter((p) => p.category === category)
}

export function getOnSale() {
  return products.filter((p) => p.salePrice)
}

export function searchProducts(query) {
  const q = query.trim().toLowerCase()
  if (!q) return []
  return products.filter(
    (p) =>
      p.name.toLowerCase().includes(q) || p.category.toLowerCase().includes(q)
  )
}
