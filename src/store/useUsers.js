import { reactive } from 'vue'

const API = 'http://localhost:5000'

const state = reactive({
  users: [],
  loaded: false
})

function getToken() {
  return localStorage.getItem('access_token') || sessionStorage.getItem('access_token')
}

async function refreshUsers() {
  const res = await fetch(`${API}/admin/users`, {
    headers: { Authorization: `Bearer ${getToken()}` }
  })
  state.users = await res.json()
  state.loaded = true
}

async function createUser(payload) {
  const res = await fetch(`${API}/admin/users`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${getToken()}`
    },
    body: JSON.stringify(payload)
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.message || 'Could not create user.')

  state.users.push(data)
  return data
}

async function updateUserRole(userId, role) {
  const res = await fetch(`${API}/admin/users/${userId}/role`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${getToken()}`
    },
    body: JSON.stringify({ role })
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.message || 'Could not update role.')

  const idx = state.users.findIndex((u) => u.id === userId)
  if (idx > -1) state.users[idx] = data

  return data
}

async function deleteUser(userId) {
  const res = await fetch(`${API}/admin/users/${userId}`, {
    method: 'DELETE',
    headers: { Authorization: `Bearer ${getToken()}` }
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.message || 'Could not delete user.')

  state.users = state.users.filter((u) => u.id !== userId)
}

export function useUsers() {
  return {
    state,
    refreshUsers,
    createUser,
    updateUserRole,
    deleteUser
  }
}
