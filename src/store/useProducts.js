import { reactive } from 'vue'

const API = 'http://localhost:5000'

const state = reactive({
  products: [],
  loaded: false
})

async function fetchProducts() {
  if (state.loaded) return
  await refreshProducts()
}

async function refreshProducts() {
  const res = await fetch(`${API}/products`)
  state.products = await res.json()
  state.loaded = true
}

function getById(id) {
  return state.products.find((p) => String(p.id) === String(id))
}

function getByCategory(category) {
  return state.products.filter((p) => p.category === category)
}

function getOnSale() {
  return state.products.filter((p) => p.salePrice)
}

function searchProducts(query) {
  const q = query.trim().toLowerCase()
  if (!q) return []
  return state.products.filter(
    (p) =>
      p.name.toLowerCase().includes(q) || p.category.toLowerCase().includes(q)
  )
}

export function useProducts() {
  return {
    state,
    fetchProducts,
    refreshProducts,
    getById,
    getByCategory,
    getOnSale,
    searchProducts
  }
}
