import { reactive, computed } from 'vue'

// A tiny hand-rolled store (no Pinia dependency needed).
// Everything lives in one reactive object so any component
// can import `state` and get live updates.

const state = reactive({
  cart: [], // { id, name, price, size, qty, image }
  user: null, // { name, email }
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

const cartCount = computed(() =>
  state.cart.reduce((sum, item) => sum + item.qty, 0)
)

const cartTotal = computed(() =>
  state.cart.reduce((sum, item) => sum + item.qty * item.price, 0)
)

function login(email, name) {
  const fallback = email.split('@')[0]
  const displayName = name?.trim()
    ? name.trim()
    : fallback.charAt(0).toUpperCase() + fallback.slice(1)
  state.user = { name: displayName, email }
  state.isLoginOpen = false
}

function logout() {
  state.user = null
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
    cartCount,
    cartTotal,
    login,
    logout,
    toggleCart,
    toggleSearch,
    toggleLogin
  }
}
