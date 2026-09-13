<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useUsers } from '../store/useUsers'
import { useStore } from '../store/useStore'

const { state, refreshUsers, createUser, updateUserRole, deleteUser } = useUsers()
const { state: authState } = useStore()

const loading = ref(true)
const error = ref('')
const savingId = ref(null)

const showForm = ref(false)
const saving = ref(false)
const formError = ref('')

function emptyForm() {
  return {
    first_name: '',
    last_name: '',
    email: '',
    password: '',
    phone: '',
    address: '',
    city: '',
    role: 'user'
  }
}

const form = reactive(emptyForm())

onMounted(async () => {
  try {
    await refreshUsers()
  } catch (err) {
    console.error(err)
    error.value = 'Cannot connect to server.'
  } finally {
    loading.value = false
  }
})

async function onRoleChange(user, event) {
  const role = event.target.value
  const previous = user.role
  savingId.value = user.id
  error.value = ''

  try {
    await updateUserRole(user.id, role)
  } catch (err) {
    error.value = err.message
    event.target.value = previous
  } finally {
    savingId.value = null
  }
}

async function onDelete(user) {
  if (!confirm(`Delete "${user.first_name} ${user.last_name}"? This cannot be undone.`)) return

  error.value = ''
  try {
    await deleteUser(user.id)
  } catch (err) {
    error.value = err.message
  }
}

function openAddForm() {
  Object.assign(form, emptyForm())
  formError.value = ''
  showForm.value = true
}

function closeForm() {
  showForm.value = false
}

async function submitForm() {
  formError.value = ''
  saving.value = true

  try {
    await createUser(form)
    showForm.value = false
  } catch (err) {
    formError.value = err.message
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <div class="admin">
    <div class="admin__head">
      <p v-if="!loading" class="admin__count">{{ state.users.length }} users</p>
      <button class="btn" @click="openAddForm">Add User</button>
    </div>

    <p v-if="loading" class="admin__loading">Loading users…</p>
    <p v-if="error" class="admin__error">{{ error }}</p>

    <template v-else-if="!loading">
      <div class="admin__table-wrap">
        <div class="admin__table">
          <div class="admin__row admin__row--head">
            <span>Name</span>
            <span>Email</span>
            <span>City</span>
            <span>Role</span>
            <span>Actions</span>
          </div>

          <div v-for="user in state.users" :key="user.id" class="admin__row">
            <span>{{ user.first_name }} {{ user.last_name }}</span>
            <span class="admin__muted">{{ user.email }}</span>
            <span class="admin__muted">{{ user.city || '—' }}</span>
            <span>
              <select
                class="admin__role-select"
                :value="user.role"
                :disabled="savingId === user.id"
                @change="onRoleChange(user, $event)"
              >
                <option value="user">User</option>
                <option value="editor">Editor</option>
                <option value="admin">Admin</option>
              </select>
            </span>
            <div class="admin__actions">
              <button
                class="admin__link admin__link--danger"
                :disabled="user.id === authState.user?.id"
                :title="user.id === authState.user?.id ? 'You cannot delete your own account' : ''"
                @click="onDelete(user)"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>

      <p v-if="state.users.length === 0" class="admin__empty">No registered users yet.</p>
    </template>

    <div v-if="showForm" class="admin__modal">
      <div class="admin__modal-scrim" @click="closeForm"></div>
      <div class="admin__modal-panel">
        <button class="admin__modal-close" aria-label="Close" @click="closeForm">✕</button>
        <h3 class="admin__modal-title">Add User</h3>

        <form class="admin__form" @submit.prevent="submitForm">
          <div class="admin__form-row">
            <label class="admin__label">
              First Name
              <input v-model="form.first_name" type="text" required />
            </label>
            <label class="admin__label">
              Last Name
              <input v-model="form.last_name" type="text" required />
            </label>
          </div>

          <label class="admin__label">
            Email
            <input v-model="form.email" type="email" required />
          </label>

          <label class="admin__label">
            Password
            <input v-model="form.password" type="password" required />
          </label>
          <p class="admin__hint">At least 8 characters, with an uppercase letter, a lowercase letter, and a number.</p>

          <div class="admin__form-row">
            <label class="admin__label">
              Phone
              <input v-model="form.phone" type="text" placeholder="+381601234567" required />
            </label>
            <label class="admin__label">
              City
              <input v-model="form.city" type="text" required />
            </label>
          </div>

          <label class="admin__label">
            Address
            <input v-model="form.address" type="text" required />
          </label>

          <label class="admin__label">
            Role
            <select v-model="form.role">
              <option value="user">User</option>
              <option value="editor">Editor</option>
              <option value="admin">Admin</option>
            </select>
          </label>

          <p v-if="formError" class="admin__error">{{ formError }}</p>

          <button type="submit" class="btn" style="width: 100%;" :disabled="saving">
            {{ saving ? 'Creating…' : 'Add User' }}
          </button>
        </form>
      </div>
    </div>
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

.admin__table-wrap {
  overflow-x: auto;
  border: 1px solid var(--line);
}

.admin__table {
  min-width: 640px;
}

.admin__row {
  display: grid;
  grid-template-columns: 1.4fr 1.8fr 1fr 140px 100px;
  align-items: center;
  gap: 16px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--line);
  font-size: 0.85rem;
}

.admin__row:last-child {
  border-bottom: none;
}

.admin__row--head {
  background: var(--stone);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  color: var(--taupe);
}

.admin__muted {
  color: var(--taupe);
}

.admin__role-select {
  font-family: var(--font-body);
  font-size: 0.85rem;
  color: var(--ink);
  border: 1px solid var(--line);
  background: var(--white);
  padding: 6px 8px;
  width: 100%;
}

.admin__role-select:focus {
  outline: none;
  border-color: var(--ink);
}

.admin__actions {
  display: flex;
  gap: 12px;
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

.admin__link:disabled {
  color: var(--taupe);
  text-decoration: none;
  cursor: not-allowed;
}

.admin__error {
  color: var(--accent);
  font-size: 0.82rem;
  margin-bottom: 16px;
}

.admin__modal {
  position: fixed;
  inset: 0;
  z-index: 80;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.admin__modal-scrim {
  position: absolute;
  inset: 0;
  background: rgba(17, 17, 17, 0.5);
}

.admin__modal-panel {
  position: relative;
  background: var(--paper);
  width: 100%;
  max-width: 560px;
  max-height: 90vh;
  overflow-y: auto;
  padding: 40px 32px;
}

.admin__modal-close {
  position: absolute;
  top: 14px;
  right: 14px;
  background: none;
  border: none;
  font-size: 1rem;
  padding: 8px;
}

.admin__modal-title {
  font-size: 1.4rem;
  margin-bottom: 24px;
}

.admin__form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.admin__form-row {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.admin__hint {
  font-size: 0.76rem;
  color: var(--taupe);
  margin-top: -8px;
}

.admin__label {
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  color: var(--taupe);
}

.admin__label input,
.admin__label select {
  font-family: var(--font-body);
  font-size: 0.9rem;
  font-weight: 400;
  text-transform: none;
  letter-spacing: normal;
  color: var(--ink);
  border: 1px solid var(--line);
  background: var(--white);
  padding: 10px 12px;
  width: 100%;
  min-width: 0;
}

.admin__label input:focus,
.admin__label select:focus {
  outline: none;
  border-color: var(--ink);
}

@media (max-width: 640px) {
  .admin__head {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }

  .admin__form-row {
    grid-template-columns: 1fr;
  }
}
</style>
