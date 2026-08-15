<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useProducts } from '../store/useProducts'
import { formatPrice } from '../utils/currency'

const { state, refreshProducts } = useProducts()

const SUBTYPES_BY_TYPE = {
  clothing: [
    { value: 'tshirt', label: 'T-Shirts' },
    { value: 'jacket', label: 'Jacket' },
    { value: 'denim', label: 'Denim' }
  ],
  accessories: [
    { value: 'glasses', label: 'Glasses' },
    { value: 'hats', label: 'Hats' },
    { value: 'bags', label: 'Bags' }
  ]
}

const MIN_IMAGES = 3

function emptyForm() {
  return {
    name: '',
    category: 'man',
    type: 'clothing',
    subtype: 'tshirt',
    price: '',
    salePrice: '',
    tag: '',
    images: ['', '', ''],
    sizesText: ''
  }
}

const loading = ref(true)
const showForm = ref(false)
const editingId = ref(null)
const form = reactive(emptyForm())
const unavailableSizes = ref(new Set())
const error = ref('')
const saving = ref(false)

const subtypeOptions = computed(() => SUBTYPES_BY_TYPE[form.type])

const sizeChips = computed(() =>
  form.sizesText.split(',').map((s) => s.trim()).filter(Boolean)
)

function toggleSizeAvailability(size) {
  const next = new Set(unavailableSizes.value)
  if (next.has(size)) {
    next.delete(size)
  } else {
    next.add(size)
  }
  unavailableSizes.value = next
}

function addImageField() {
  form.images.push('')
}

function removeImageField(index) {
  if (form.images.length <= MIN_IMAGES) return
  form.images.splice(index, 1)
}

onMounted(async () => {
  await refreshProducts()
  loading.value = false
})

function getToken() {
  return localStorage.getItem('access_token') || sessionStorage.getItem('access_token')
}

function openAddForm() {
  editingId.value = null
  Object.assign(form, emptyForm())
  unavailableSizes.value = new Set()
  error.value = ''
  showForm.value = true
}

function openEditForm(product) {
  editingId.value = product.id
  Object.assign(form, {
    name: product.name,
    category: product.category,
    type: product.type,
    subtype: product.subtype,
    price: product.price,
    salePrice: product.salePrice || '',
    tag: product.tag || '',
    images: [...product.images],
    sizesText: product.sizes.map((s) => s.size).join(', ')
  })
  unavailableSizes.value = new Set(
    product.sizes.filter((s) => !s.available).map((s) => s.size)
  )
  error.value = ''
  showForm.value = true
}

function closeForm() {
  showForm.value = false
}

function onTypeChange() {
  form.subtype = SUBTYPES_BY_TYPE[form.type][0].value
}

async function submitForm() {
  error.value = ''
  saving.value = true

  const payload = {
    name: form.name,
    category: form.category,
    type: form.type,
    subtype: form.subtype,
    price: Number(form.price),
    salePrice: form.salePrice ? Number(form.salePrice) : null,
    tag: form.tag || null,
    images: form.images.map((url) => url.trim()).filter(Boolean),
    sizes: sizeChips.value.map((size) => ({
      size,
      available: !unavailableSizes.value.has(size)
    }))
  }

  const url = editingId.value
    ? `http://localhost:5000/products/${editingId.value}`
    : 'http://localhost:5000/products'
  const method = editingId.value ? 'PUT' : 'POST'

  try {
    const res = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${getToken()}`
      },
      body: JSON.stringify(payload)
    })
    const data = await res.json()

    if (!res.ok) {
      error.value = data.message || 'Something went wrong.'
      return
    }

    await refreshProducts()
    showForm.value = false
  } catch (err) {
    console.error(err)
    error.value = 'Cannot connect to server.'
  } finally {
    saving.value = false
  }
}

async function deleteProduct(product) {
  if (!confirm(`Delete "${product.name}"? This cannot be undone.`)) return

  try {
    const res = await fetch(`http://localhost:5000/products/${product.id}`, {
      method: 'DELETE',
      headers: { Authorization: `Bearer ${getToken()}` }
    })
    if (!res.ok) {
      const data = await res.json()
      alert(data.message || 'Could not delete product.')
      return
    }
    await refreshProducts()
  } catch (err) {
    console.error(err)
    alert('Cannot connect to server.')
  }
}
</script>

<template>
  <div class="admin">
    <div class="admin__head">
      <p v-if="!loading" class="admin__count">{{ state.products.length }} products</p>
      <button class="btn" @click="openAddForm">Add Product</button>
    </div>

    <p v-if="loading" class="admin__loading">Loading products…</p>

    <template v-else>
      <div class="admin__table-wrap">
        <div class="admin__table">
          <div class="admin__row admin__row--head">
            <span>Image</span>
            <span>Name</span>
            <span>Category</span>
            <span>Subtype</span>
            <span>Price</span>
            <span>Actions</span>
          </div>

          <div v-for="product in state.products" :key="product.id" class="admin__row">
            <img :src="product.images[0]" :alt="product.name" class="admin__thumb" />
            <span>{{ product.name }}</span>
            <span class="admin__muted">{{ product.category }} / {{ product.type }}</span>
            <span class="admin__muted">{{ product.subtype }}</span>
            <span>
              <template v-if="product.salePrice">
                <span class="admin__was">{{ formatPrice(product.price) }}</span>
                {{ formatPrice(product.salePrice) }}
              </template>
              <template v-else>{{ formatPrice(product.price) }}</template>
            </span>
            <div class="admin__actions">
              <button class="admin__link" @click="openEditForm(product)">Edit</button>
              <button class="admin__link admin__link--danger" @click="deleteProduct(product)">
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>

      <p v-if="state.products.length === 0" class="admin__empty">No products yet.</p>
    </template>

    <div v-if="showForm" class="admin__modal">
      <div class="admin__modal-scrim" @click="closeForm"></div>
      <div class="admin__modal-panel">
        <button class="admin__modal-close" aria-label="Close" @click="closeForm">✕</button>
        <h3 class="admin__modal-title">{{ editingId ? 'Edit Product' : 'Add Product' }}</h3>

        <form class="admin__form" @submit.prevent="submitForm">
          <label class="admin__label">
            Name
            <input v-model="form.name" type="text" required />
          </label>

          <div class="admin__form-row">
            <label class="admin__label">
              Category
              <select v-model="form.category">
                <option value="man">Man</option>
                <option value="woman">Woman</option>
              </select>
            </label>

            <label class="admin__label">
              Type
              <select v-model="form.type" @change="onTypeChange">
                <option value="clothing">Clothing</option>
                <option value="accessories">Accessories</option>
              </select>
            </label>

            <label class="admin__label">
              Subtype
              <select v-model="form.subtype">
                <option v-for="opt in subtypeOptions" :key="opt.value" :value="opt.value">
                  {{ opt.label }}
                </option>
              </select>
            </label>
          </div>

          <div class="admin__form-row">
            <label class="admin__label">
              Price (RSD)
              <input v-model.number="form.price" type="number" min="1" required />
            </label>
            <label class="admin__label">
              Sale Price (RSD)
              <input v-model.number="form.salePrice" type="number" min="1" placeholder="Optional" />
            </label>
            <label class="admin__label">
              Tag
              <select v-model="form.tag">
                <option value="">None</option>
                <option value="New">New</option>
                <option value="Sale">Sale</option>
              </select>
            </label>
          </div>

          <div class="admin__images">
            <span class="admin__label-text">Images (at least {{ MIN_IMAGES }}, or leave all blank for placeholders)</span>
            <div v-for="(image, index) in form.images" :key="index" class="admin__image-row">
              <input v-model="form.images[index]" type="text" :placeholder="`Image ${index + 1} URL`" />
              <button
                v-if="form.images.length > MIN_IMAGES"
                type="button"
                class="admin__link admin__link--danger"
                @click="removeImageField(index)"
              >
                Remove
              </button>
            </div>
            <button type="button" class="admin__link" @click="addImageField">+ Add another image</button>
          </div>

          <label class="admin__label">
            Sizes
            <input v-model="form.sizesText" type="text" placeholder="S, M, L, XL" required />
          </label>
          <div v-if="sizeChips.length" class="admin__size-chips">
            <button
              v-for="size in sizeChips"
              :key="size"
              type="button"
              class="admin__size-chip"
              :class="{ 'admin__size-chip--unavailable': unavailableSizes.has(size) }"
              @click="toggleSizeAvailability(size)"
            >
              {{ size }}
            </button>
          </div>
          <p v-if="sizeChips.length" class="admin__hint">
            Click a size to mark it unavailable — it still shows on the product page, just can't be selected.
          </p>

          <p v-if="error" class="admin__error">{{ error }}</p>

          <button type="submit" class="btn" style="width: 100%;" :disabled="saving">
            {{ saving ? 'Saving…' : editingId ? 'Save Changes' : 'Add Product' }}
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
  min-width: 720px;
}

.admin__row {
  display: grid;
  grid-template-columns: 64px 2fr 1.3fr 1fr 1.4fr 120px;
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

.admin__thumb {
  width: 44px;
  height: 56px;
  object-fit: cover;
  background: var(--stone);
}

.admin__muted {
  color: var(--taupe);
  text-transform: capitalize;
}

.admin__was {
  color: var(--taupe);
  text-decoration: line-through;
  margin-right: 6px;
  font-size: 0.8em;
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
}

.admin__link--danger {
  color: var(--accent);
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
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.admin__images {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.admin__label-text {
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  color: var(--taupe);
}

.admin__image-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.admin__image-row input {
  font-family: var(--font-body);
  font-size: 0.9rem;
  color: var(--ink);
  border: 1px solid var(--line);
  background: var(--white);
  padding: 10px 12px;
  width: 100%;
  min-width: 0;
}

.admin__image-row input:focus {
  outline: none;
  border-color: var(--ink);
}

.admin__image-row .admin__link {
  flex-shrink: 0;
}

.admin__size-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: -6px;
}

.admin__size-chip {
  border: 1px solid var(--line);
  background: transparent;
  padding: 8px 14px;
  font-size: 0.8rem;
  font-weight: 600;
  transition: border-color 0.15s ease, background 0.15s ease;
}

.admin__size-chip--unavailable {
  color: var(--taupe);
  text-decoration: line-through;
  border-style: dashed;
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

.admin__error {
  color: var(--accent);
  font-size: 0.82rem;
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
