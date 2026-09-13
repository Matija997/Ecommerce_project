<script setup>
import { ref, onMounted } from 'vue'
import { useMessages } from '../store/useMessages'

const { state, refreshMessages, deleteMessage } = useMessages()

const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    await refreshMessages()
  } catch (err) {
    console.error(err)
    error.value = 'Cannot connect to server.'
  } finally {
    loading.value = false
  }
})

function formatDate(iso) {
  return new Date(iso).toLocaleString('en-GB', {
    day: '2-digit',
    month: 'short',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

async function onDelete(message) {
  if (!confirm(`Delete the message from "${message.name}"? This cannot be undone.`)) return

  error.value = ''
  try {
    await deleteMessage(message.id)
  } catch (err) {
    error.value = err.message
  }
}
</script>

<template>
  <div class="admin">
    <div class="admin__head">
      <p v-if="!loading" class="admin__count">{{ state.messages.length }} messages</p>
    </div>

    <p v-if="loading" class="admin__loading">Loading messages…</p>
    <p v-if="error" class="admin__error">{{ error }}</p>

    <template v-else-if="!loading">
      <div class="admin__list">
        <div v-for="message in state.messages" :key="message.id" class="admin__message">
          <div class="admin__message-head">
            <div>
              <p class="admin__message-name">{{ message.name }}</p>
              <a class="admin__message-email" :href="`mailto:${message.email}`">{{ message.email }}</a>
            </div>
            <div class="admin__message-meta">
              <span class="admin__muted">{{ formatDate(message.created_at) }}</span>
              <button class="admin__link admin__link--danger" @click="onDelete(message)">Delete</button>
            </div>
          </div>
          <p class="admin__message-body">{{ message.message }}</p>
        </div>
      </div>

      <p v-if="state.messages.length === 0" class="admin__empty">No messages yet.</p>
    </template>
  </div>
</template>

<style scoped>
.admin__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
}

.admin__count {
  color: var(--taupe);
  font-size: 0.85rem;
}

.admin__loading,
.admin__empty {
  color: var(--taupe);
  padding: 40px 0;
  text-align: center;
}

.admin__list {
  display: flex;
  flex-direction: column;
  gap: 1px;
  background: var(--line);
  border: 1px solid var(--line);
}

.admin__message {
  background: var(--paper);
  padding: 18px 20px;
}

.admin__message-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 10px;
}

.admin__message-name {
  font-weight: 600;
  font-size: 0.92rem;
}

.admin__message-email {
  color: var(--taupe);
  font-size: 0.82rem;
}

.admin__message-meta {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-shrink: 0;
}

.admin__message-body {
  font-size: 0.9rem;
  line-height: 1.5;
  color: var(--ink);
  white-space: pre-wrap;
}

.admin__muted {
  color: var(--taupe);
  font-size: 0.78rem;
  white-space: nowrap;
}

.admin__link {
  background: none;
  border: none;
  padding: 0;
  font-size: 0.8rem;
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 2px;
  color: var(--ink);
  cursor: pointer;
}

.admin__link--danger {
  color: var(--accent);
}

.admin__error {
  color: var(--accent);
  font-size: 0.82rem;
  margin-bottom: 16px;
}

@media (max-width: 640px) {
  .admin__message-head {
    flex-direction: column;
    gap: 8px;
  }
}
</style>
