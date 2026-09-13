import { reactive } from 'vue'

const API = 'http://localhost:5000'

const state = reactive({
  orders: [],
  loaded: false
})

function getToken() {
  return localStorage.getItem('access_token') || sessionStorage.getItem('access_token')
}

async function refreshOrders() {
  const res = await fetch(`${API}/admin/orders`, {
    headers: { Authorization: `Bearer ${getToken()}` }
  })
  state.orders = await res.json()
  state.loaded = true
}

export function useOrders() {
  return {
    state,
    refreshOrders
  }
}
