<script setup>
import { ref, computed, watch } from 'vue'
import { useStore } from '../store/useStore'
import { formatPrice } from '../utils/currency'

const { state, cartTotal, clearCart, toggleLogin } = useStore()

const firstName = ref('')
const lastName = ref('')
const email = ref(state.user?.email || '')
const phone = ref('')
const address = ref('')
const city = ref('')

const paymentMethod = ref('card')
const cardName = ref('')
const cardNumber = ref('')
const cardExpiry = ref('')
const cardCvc = ref('')

const placed = ref(false)
const orderNumber = ref('')
const continuingAsGuest = ref(false)
const placing = ref(false)
const placeError = ref('')

const showGuestPrompt = computed(() => !state.user && !continuingAsGuest.value)

const shippingFee = computed(() => (cartTotal.value >= 12000 || cartTotal.value === 0 ? 0 : 490))
const orderTotal = computed(() => cartTotal.value + shippingFee.value)

function getToken() {
  return localStorage.getItem('access_token') || sessionStorage.getItem('access_token')
}

async function loadProfile() {
  const token = getToken()
  if (!token) return

  try {
    const res = await fetch('http://localhost:5000/profile', {
      headers: { Authorization: `Bearer ${token}` }
    })
    if (!res.ok) return
    const data = await res.json()

    firstName.value = data.first_name || ''
    lastName.value = data.last_name || ''
    email.value = data.email || ''
    phone.value = data.phone || ''
    address.value = data.address || ''
    city.value = data.city || ''
  } catch (err) {
    console.error(err)
  }
}

watch(
  () => state.user,
  (user) => {
    if (user) {
      continuingAsGuest.value = false
      loadProfile()
    }
  },
  { immediate: true }
)

function continueAsGuest() {
  continuingAsGuest.value = true
}

async function placeOrder() {
  placeError.value = ''
  placing.value = true

  try {
    const res = await fetch('http://localhost:5000/orders', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        first_name: firstName.value,
        last_name: lastName.value,
        email: email.value,
        phone: phone.value,
        address: address.value,
        city: city.value,
        payment_method: paymentMethod.value,
        items: state.cart.map((item) => ({
          product_id: item.id,
          name: item.name,
          image: item.image,
          size: item.size,
          qty: item.qty,
          price: item.price
        })),
        subtotal: cartTotal.value,
        shipping_fee: shippingFee.value,
        total: orderTotal.value
      })
    })

    const data = await res.json()

    if (!res.ok) {
      placeError.value = data.message || 'Could not place order.'
      return
    }

    orderNumber.value = data.order_number
    placed.value = true
    clearCart()
  } catch (err) {
    console.error(err)
    placeError.value = 'Cannot connect to server.'
  } finally {
    placing.value = false
  }
}
</script>

<template>
  <div class="checkout container">
    <div v-if="placed" class="checkout__confirm">
      <span class="eyebrow">Order placed</span>
      <h1 class="checkout__confirm-title">Thank you, {{ firstName || 'there' }}.</h1>
      <p class="checkout__confirm-sub">
        Your order <strong>{{ orderNumber }}</strong> has been placed. A confirmation
        would normally be sent to <strong>{{ email }}</strong>.
      </p>
      <router-link to="/" class="btn">Continue Shopping</router-link>
    </div>

    <div v-else-if="state.cart.length === 0" class="checkout__empty">
      <span class="eyebrow">Checkout</span>
      <h1 class="checkout__confirm-title">Your bag is empty.</h1>
      <p class="checkout__confirm-sub">Add something to your bag before checking out.</p>
      <router-link to="/" class="btn">Back to Shop</router-link>
    </div>

    <template v-else>
      <div class="checkout__head">
        <span class="eyebrow">Checkout</span>
        <h1 class="checkout__title">Checkout</h1>
      </div>

      <div v-if="showGuestPrompt" class="checkout__guest">
        <p>Sign in for faster checkout — we'll fill in your details for you.</p>
        <div class="checkout__guest-actions">
          <button type="button" class="btn" @click="toggleLogin(true)">Sign In / Sign Up</button>
          <button type="button" class="btn btn-outline" @click="continueAsGuest">
            Continue Without Account
          </button>
        </div>
      </div>

      <div class="checkout__layout">
        <form class="checkout__form" @submit.prevent="placeOrder">
          <section class="checkout__section">
            <h2 class="checkout__section-title">Contact</h2>
            <label class="checkout__label">
              Email
              <input v-model="email" type="email" placeholder="you@email.com" required />
            </label>
          </section>

          <section class="checkout__section">
            <h2 class="checkout__section-title">Shipping address</h2>
            <div class="checkout__row">
              <label class="checkout__label">
                First Name
                <input v-model="firstName" type="text" placeholder="John" required />
              </label>
              <label class="checkout__label">
                Last Name
                <input v-model="lastName" type="text" placeholder="Doe" required />
              </label>
            </div>
            <label class="checkout__label">
              Address
              <input v-model="address" type="text" placeholder="Street 12" required />
            </label>
            <div class="checkout__row">
              <label class="checkout__label">
                City
                <input v-model="city" type="text" placeholder="Belgrade" required />
              </label>
              <label class="checkout__label">
                Phone
                <input v-model="phone" type="text" placeholder="+381601234567" required />
              </label>
            </div>
          </section>

          <section class="checkout__section">
            <h2 class="checkout__section-title">Payment</h2>

            <div class="checkout__payment-methods">
              <button
                type="button"
                class="checkout__payment-method"
                :class="{ 'checkout__payment-method--active': paymentMethod === 'card' }"
                @click="paymentMethod = 'card'"
              >
                Pay with Card
              </button>
              <button
                type="button"
                class="checkout__payment-method"
                :class="{ 'checkout__payment-method--active': paymentMethod === 'cash' }"
                @click="paymentMethod = 'cash'"
              >
                Cash on Delivery
              </button>
            </div>

            <template v-if="paymentMethod === 'card'">
              <p class="checkout__demo-note">Demo checkout — no real payment is processed.</p>
              <label class="checkout__label">
                Name on Card
                <input v-model="cardName" type="text" placeholder="John Doe" required />
              </label>
              <label class="checkout__label">
                Card Number
                <input
                  v-model="cardNumber"
                  type="text"
                  inputmode="numeric"
                  placeholder="4242 4242 4242 4242"
                  maxlength="19"
                  required
                />
              </label>
              <div class="checkout__row">
                <label class="checkout__label">
                  Expiry
                  <input v-model="cardExpiry" type="text" placeholder="MM/YY" maxlength="5" required />
                </label>
                <label class="checkout__label">
                  CVC
                  <input v-model="cardCvc" type="text" inputmode="numeric" placeholder="123" maxlength="4" required />
                </label>
              </div>
            </template>

            <p v-else class="checkout__demo-note">
              Pay in cash when your order arrives.
            </p>
          </section>

          <p v-if="placeError" class="checkout__error">{{ placeError }}</p>

          <button type="submit" class="btn" style="width: 100%;" :disabled="placing">
            {{ placing ? 'Placing Order…' : `Place Order — ${formatPrice(orderTotal)}` }}
          </button>
        </form>

        <aside class="checkout__summary">
          <h2 class="checkout__section-title">Order summary</h2>

          <div class="checkout__items">
            <div v-for="item in state.cart" :key="item.id + item.size" class="checkout__item">
              <img :src="item.image" :alt="item.name" />
              <div class="checkout__item-info">
                <p class="checkout__item-name">{{ item.name }}</p>
                <p class="checkout__item-meta">Size {{ item.size }} · Qty {{ item.qty }}</p>
              </div>
              <span class="checkout__item-price">{{ formatPrice(item.qty * item.price) }}</span>
            </div>
          </div>

          <div class="checkout__totals">
            <div class="checkout__totals-row">
              <span>Subtotal</span>
              <span>{{ formatPrice(cartTotal) }}</span>
            </div>
            <div class="checkout__totals-row">
              <span>Shipping</span>
              <span>{{ shippingFee === 0 ? 'Free' : formatPrice(shippingFee) }}</span>
            </div>
            <div class="checkout__totals-row checkout__totals-row--total">
              <span>Total</span>
              <span>{{ formatPrice(orderTotal) }}</span>
            </div>
          </div>
        </aside>
      </div>
    </template>
  </div>
</template>

<style scoped>
.checkout {
  padding: 48px 32px 100px;
}

.checkout__head {
  margin-bottom: 32px;
}

.checkout__title {
  font-size: clamp(2rem, 4vw, 2.8rem);
  margin-top: 8px;
}

.checkout__guest {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
  background: var(--stone);
  padding: 20px 24px;
  margin-bottom: 32px;
}

.checkout__guest p {
  font-size: 0.9rem;
  color: var(--ink-soft);
}

.checkout__guest-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.checkout__payment-methods {
  display: flex;
  gap: 10px;
  margin-bottom: 4px;
}

.checkout__payment-method {
  flex: 1;
  border: 1px solid var(--line);
  background: transparent;
  padding: 12px;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  transition: border-color 0.15s ease, background 0.15s ease;
}

.checkout__payment-method--active {
  border-color: var(--ink);
  background: var(--ink);
  color: var(--paper);
}

.checkout__layout {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 56px;
  align-items: start;
}

.checkout__form {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.checkout__section {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.checkout__section-title {
  font-size: 1.05rem;
  font-weight: 600;
  font-family: var(--font-body);
}

.checkout__demo-note {
  font-size: 0.78rem;
  color: var(--taupe);
  margin-top: -8px;
}

.checkout__error {
  color: var(--accent);
  font-size: 0.85rem;
}

.checkout__row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.checkout__label {
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  color: var(--taupe);
}

.checkout__label input {
  font-family: var(--font-body);
  font-size: 0.95rem;
  font-weight: 400;
  text-transform: none;
  letter-spacing: normal;
  color: var(--ink);
  border: 1px solid var(--line);
  background: var(--white);
  padding: 12px 14px;
  width: 100%;
  min-width: 0;
}

.checkout__label input:focus {
  outline: none;
  border-color: var(--ink);
}

.checkout__summary {
  background: var(--stone);
  padding: 28px;
  position: sticky;
  top: calc(var(--header-h) + 24px);
}

.checkout__items {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin: 20px 0;
  max-height: 340px;
  overflow-y: auto;
}

.checkout__item {
  display: flex;
  align-items: center;
  gap: 12px;
}

.checkout__item img {
  width: 56px;
  height: 70px;
  object-fit: cover;
  flex-shrink: 0;
}

.checkout__item-info {
  flex: 1;
  min-width: 0;
}

.checkout__item-name {
  font-size: 0.85rem;
  font-weight: 600;
}

.checkout__item-meta {
  font-size: 0.75rem;
  color: var(--taupe);
  margin-top: 2px;
}

.checkout__item-price {
  font-size: 0.82rem;
  font-weight: 600;
  white-space: nowrap;
}

.checkout__totals {
  border-top: 1px solid var(--line);
  padding-top: 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.checkout__totals-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.88rem;
  color: var(--taupe);
}

.checkout__totals-row--total {
  color: var(--ink);
  font-weight: 700;
  font-size: 1rem;
  padding-top: 6px;
  border-top: 1px solid var(--line);
}

.checkout__confirm,
.checkout__empty {
  min-height: 50vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 14px;
  padding: 60px 0;
}

.checkout__confirm-title {
  font-size: clamp(1.8rem, 4vw, 2.6rem);
  max-width: 20ch;
}

.checkout__confirm-sub {
  color: var(--taupe);
  max-width: 46ch;
  margin-bottom: 8px;
}

@media (max-width: 860px) {
  .checkout {
    padding: 32px 18px 60px;
  }

  .checkout__layout {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  .checkout__row {
    grid-template-columns: 1fr;
  }

  .checkout__summary {
    position: static;
    order: -1;
  }

  .checkout__guest {
    flex-direction: column;
    align-items: flex-start;
  }

  .checkout__payment-methods {
    flex-direction: column;
  }
}
</style>
