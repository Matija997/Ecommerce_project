import { reactive, computed } from 'vue'

// A tiny hand-rolled store (no Pinia dependency needed).
// Everything lives in one reactive object so any component
// can import `state` and get live updates.

// "Stay logged in" -> localStorage (survives browser restarts).
// Otherwise -> sessionStorage (cleared when the tab/browser closes).
const storedUser = localStorage.getItem('user') || sessionStorage.getItem('user')
const storedToken = localStorage.getItem('access_token') || sessionStorage.getItem('access_token')

const state = reactive({
  cart: [], // { id, name, price, size, qty, image }
  user: storedUser && storedToken ? JSON.parse(storedUser) : null, // { id, name, email, role }
  isCartOpen: false,
  isSearchOpen: false,
  isLoginOpen: false,
  searchQuery: ''
})

function addToCart(product, size) {
  const existing = state.cart.find(
    (item) => item.id === product.id && item.size === size
  )
  if (existing) {
    existing.qty += 1
  } else {
    state.cart.push({
      id: product.id,
      name: product.name,
      price: product.price,
      image: product.image,
      size,
      qty: 1
    })
  }
  state.isCartOpen = true
}

function removeFromCart(id, size) {
  const idx = state.cart.findIndex((i) => i.id === id && i.size === size)
  if (idx > -1) state.cart.splice(idx, 1)
}

function updateQty(id, size, qty) {
  const item = state.cart.find((i) => i.id === id && i.size === size)
  if (item) item.qty = Math.max(1, qty)
}

function clearCart() {
  state.cart = []
}

const cartCount = computed(() =>
  state.cart.reduce((sum, item) => sum + item.qty, 0)
)

const cartTotal = computed(() =>
  state.cart.reduce((sum, item) => sum + item.qty * item.price, 0)
)

function login(user, token, remember = false) {
  state.user = user
  state.isLoginOpen = false

  const store = remember ? localStorage : sessionStorage
  const other = remember ? sessionStorage : localStorage
  other.removeItem('user')
  other.removeItem('access_token')

  store.setItem('user', JSON.stringify(user))
  if (token) store.setItem('access_token', token)
}

function logout() {
  state.user = null
  localStorage.removeItem('user')
  localStorage.removeItem('access_token')
  sessionStorage.removeItem('user')
  sessionStorage.removeItem('access_token')
}

function toggleCart(force) {
  state.isCartOpen = force !== undefined ? force : !state.isCartOpen
}

function toggleSearch(force) {
  state.isSearchOpen = force !== undefined ? force : !state.isSearchOpen
  if (!state.isSearchOpen) state.searchQuery = ''
}

function toggleLogin(force) {
  state.isLoginOpen = force !== undefined ? force : !state.isLoginOpen
}

export function useStore() {
  return {
    state,
    addToCart,
    removeFromCart,
    updateQty,
    clearCart,
    cartCount,
    cartTotal,
    login,
    logout,
    toggleCart,
    toggleSearch,
    toggleLogin
  }
}
