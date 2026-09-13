import { reactive } from 'vue'

const API = 'http://localhost:5000'

const state = reactive({
  messages: [],
  loaded: false
})

function getToken() {
  return localStorage.getItem('access_token') || sessionStorage.getItem('access_token')
}

async function refreshMessages() {
  const res = await fetch(`${API}/admin/messages`, {
    headers: { Authorization: `Bearer ${getToken()}` }
  })
  state.messages = await res.json()
  state.loaded = true
}

async function deleteMessage(messageId) {
  const res = await fetch(`${API}/admin/messages/${messageId}`, {
    method: 'DELETE',
    headers: { Authorization: `Bearer ${getToken()}` }
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.message || 'Could not delete message.')

  state.messages = state.messages.filter((m) => m.id !== messageId)
}

export function useMessages() {
  return {
    state,
    refreshMessages,
    deleteMessage
  }
}
