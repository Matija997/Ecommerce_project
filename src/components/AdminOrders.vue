<script setup>
import { ref, onMounted } from 'vue'
import { useOrders } from '../store/useOrders'
import { formatPrice } from '../utils/currency'

const { state, refreshOrders } = useOrders()

const loading = ref(true)
const error = ref('')
const expandedId = ref(null)

onMounted(async () => {
  try {
    await refreshOrders()
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

function toggleExpand(order) {
  expandedId.value = expandedId.value === order.id ? null : order.id
}
</script>

<template>
  <div class="admin">
    <div class="admin__head">
      <p v-if="!loading" class="admin__count">{{ state.orders.length }} orders</p>
    </div>

    <p v-if="loading" class="admin__loading">Loading orders…</p>
    <p v-if="error" class="admin__error">{{ error }}</p>

    <template v-else-if="!loading">
      <div class="admin__table-wrap">
        <div class="admin__table">
          <div class="admin__row admin__row--head">
            <span>Order #</span>
            <span>Customer</span>
            <span>Payment</span>
            <span>Total</span>
            <span>Placed</span>
            <span>Items</span>
          </div>

          <template v-for="order in state.orders" :key="order.id">
            <div class="admin__row">
              <span class="admin__order-num">{{ order.order_number }}</span>
              <span>
                {{ order.first_name }} {{ order.last_name }}
                <span class="admin__muted admin__block">{{ order.email }}</span>
              </span>
              <span class="admin__muted">{{ order.payment_method === 'card' ? 'Card' : 'Cash on Delivery' }}</span>
              <span>{{ formatPrice(order.total) }}</span>
              <span class="admin__muted">{{ formatDate(order.created_at) }}</span>
              <button class="admin__link" @click="toggleExpand(order)">
                {{ expandedId === order.id ? 'Hide' : `View (${order.items.length})` }}
              </button>
            </div>

            <div v-if="expandedId === order.id" class="admin__order-details">
              <div class="admin__order-address">
                <span class="admin__contact-label">Ship to</span>
                <p>{{ order.address }}, {{ order.city }} · {{ order.phone }}</p>
              </div>

              <div v-for="(item, i) in order.items" :key="i" class="admin__order-item">
                <img :src="item.image" :alt="item.name" class="admin__thumb" />
                <span>{{ item.name }}</span>
                <span class="admin__muted">Size {{ item.size }}</span>
                <span class="admin__muted">Qty {{ item.qty }}</span>
                <span>{{ formatPrice(item.qty * item.price) }}</span>
              </div>

              <div class="admin__order-totals">
                <span>Subtotal {{ formatPrice(order.subtotal) }}</span>
                <span>Shipping {{ order.shipping_fee === 0 ? 'Free' : formatPrice(order.shipping_fee) }}</span>
                <span class="admin__order-total">Total {{ formatPrice(order.total) }}</span>
              </div>
            </div>
          </template>
        </div>
      </div>

      <p v-if="state.orders.length === 0" class="admin__empty">No orders yet.</p>
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

.admin__table-wrap {
  overflow-x: auto;
  border: 1px solid var(--line);
}

.admin__table {
  min-width: 760px;
}

.admin__row {
  display: grid;
  grid-template-columns: 1.1fr 1.6fr 1fr 1fr 1.3fr 120px;
  align-items: center;
  gap: 16px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--line);
  font-size: 0.85rem;
}

.admin__row--head {
  background: var(--stone);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  color: var(--taupe);
  border-bottom: 1px solid var(--line);
}

.admin__order-num {
  font-weight: 600;
}

.admin__muted {
  color: var(--taupe);
}

.admin__block {
  display: block;
  font-size: 0.78rem;
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
  justify-self: start;
}

.admin__order-details {
  padding: 16px 20px 20px;
  background: var(--stone);
  border-bottom: 1px solid var(--line);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.admin__order-address {
  font-size: 0.85rem;
  margin-bottom: 4px;
}

.admin__contact-label {
  display: block;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  color: var(--taupe);
  margin-bottom: 4px;
}

.admin__order-item {
  display: grid;
  grid-template-columns: 44px 2fr 1fr 1fr 1fr;
  align-items: center;
  gap: 12px;
  font-size: 0.85rem;
}

.admin__thumb {
  width: 36px;
  height: 46px;
  object-fit: cover;
  background: var(--paper);
}

.admin__order-totals {
  display: flex;
  gap: 20px;
  padding-top: 10px;
  margin-top: 4px;
  border-top: 1px solid var(--line);
  font-size: 0.85rem;
  color: var(--taupe);
}

.admin__order-total {
  color: var(--ink);
  font-weight: 700;
}

.admin__error {
  color: var(--accent);
  font-size: 0.82rem;
  margin-bottom: 16px;
}
</style>
