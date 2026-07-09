
function img(seed, w = 700, h = 900) {
  return `https://picsum.photos/seed/${seed}/${w}/${h}`
}

export const products = [
  {
    id: 'm01',
    name: 'Boxy Wool Overcoat',
    category: 'man',
    price: 189,
    salePrice: null,
    tag: 'New',
    image: img('friso-m01-a'),
    imageAlt: img('friso-m01-b'),
    sizes: ['S', 'M', 'L', 'XL']
  },
  {
    id: 'm02',
    name: 'Heavyweight Crewneck',
    category: 'man',
    price: 68,
    salePrice: 48,
    tag: 'Sale',
    image: img('friso-m02-a'),
    imageAlt: img('friso-m02-b'),
    sizes: ['S', 'M', 'L', 'XL', 'XXL']
  },
  {
    id: 'm03',
    name: 'Tapered Chino Trouser',
    category: 'man',
    price: 92,
    salePrice: null,
    tag: null,
    image: img('friso-m03-a'),
    imageAlt: img('friso-m03-b'),
    sizes: ['28', '30', '32', '34', '36']
  },
  {
    id: 'm04',
    name: 'Structured Denim Jacket',
    category: 'man',
    price: 128,
    salePrice: 89,
    tag: 'Sale',
    image: img('friso-m04-a'),
    imageAlt: img('friso-m04-b'),
    sizes: ['S', 'M', 'L', 'XL']
  },
  {
    id: 'm05',
    name: 'Merino Half-Zip',
    category: 'man',
    price: 110,
    salePrice: null,
    tag: 'New',
    image: img('friso-m05-a'),
    imageAlt: img('friso-m05-b'),
    sizes: ['S', 'M', 'L', 'XL']
  },
  {
    id: 'm06',
    name: 'Relaxed Linen Shirt',
    category: 'man',
    price: 74,
    salePrice: null,
    tag: null,
    image: img('friso-m06-a'),
    imageAlt: img('friso-m06-b'),
    sizes: ['S', 'M', 'L']
  },
  {
    id: 'w01',
    name: 'Draped Satin Slip Dress',
    category: 'woman',
    price: 142,
    salePrice: null,
    tag: 'New',
    image: img('friso-w01-a'),
    imageAlt: img('friso-w01-b'),
    sizes: ['XS', 'S', 'M', 'L']
  },
  {
    id: 'w02',
    name: 'Cropped Tailored Blazer',
    category: 'woman',
    price: 156,
    salePrice: 109,
    tag: 'Sale',
    image: img('friso-w02-a'),
    imageAlt: img('friso-w02-b'),
    sizes: ['XS', 'S', 'M', 'L']
  },
  {
    id: 'w03',
    name: 'High-Rise Wide Denim',
    category: 'woman',
    price: 98,
    salePrice: null,
    tag: null,
    image: img('friso-w03-a'),
    imageAlt: img('friso-w03-b'),
    sizes: ['24', '26', '28', '30', '32']
  },
  {
    id: 'w04',
    name: 'Ribbed Knit Bodysuit',
    category: 'woman',
    price: 54,
    salePrice: 38,
    tag: 'Sale',
    image: img('friso-w04-a'),
    imageAlt: img('friso-w04-b'),
    sizes: ['XS', 'S', 'M', 'L']
  },
  {
    id: 'w05',
    name: 'Oversized Camel Coat',
    category: 'woman',
    price: 210,
    salePrice: null,
    tag: 'New',
    image: img('friso-w05-a'),
    imageAlt: img('friso-w05-b'),
    sizes: ['XS', 'S', 'M', 'L']
  },
  {
    id: 'w06',
    name: 'Pleated Midi Skirt',
    category: 'woman',
    price: 82,
    salePrice: null,
    tag: null,
    image: img('friso-w06-a'),
    imageAlt: img('friso-w06-b'),
    sizes: ['XS', 'S', 'M', 'L']
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
