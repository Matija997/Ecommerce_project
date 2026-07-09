<script setup>
import { useStore } from '../store/useStore'

const { state, cartTotal, removeFromCart, updateQty, toggleCart } = useStore()
</script>

<template>
  <transition name="fade">
    <div v-if="state.isCartOpen" class="drawer">
      <div class="drawer__scrim" @click="toggleCart(false)"></div>

      <aside class="drawer__panel" role="dialog" aria-modal="true" aria-label="Shopping bag">
        <div class="drawer__head">
          <h3>Your Bag ({{ state.cart.reduce((n, i) => n + i.qty, 0) }})</h3>
          <button class="drawer__close" aria-label="Close bag" @click="toggleCart(false)">✕</button>
        </div>

        <div v-if="state.cart.length === 0" class="drawer__empty">
          <p>Your bag is empty.</p>
          <button class="btn btn-outline" @click="toggleCart(false)">Continue shopping</button>
        </div>

        <div v-else class="drawer__items">
          <div v-for="item in state.cart" :key="item.id + item.size" class="drawer__item">
            <img :src="item.image" :alt="item.name" />
            <div class="drawer__item-info">
              <p class="drawer__item-name">{{ item.name }}</p>
              <p class="drawer__item-size">Size {{ item.size }}</p>

              <div class="drawer__item-row">
                <div class="drawer__qty">
                  <button @click="updateQty(item.id, item.size, item.qty - 1)">−</button>
                  <span>{{ item.qty }}</span>
                  <button @click="updateQty(item.id, item.size, item.qty + 1)">+</button>
                </div>
                <span class="drawer__item-price">${{ item.qty * item.price }}</span>
              </div>
            </div>
            <button class="drawer__remove" aria-label="Remove item" @click="removeFromCart(item.id, item.size)">
              ✕
            </button>
          </div>
        </div>

        <div v-if="state.cart.length > 0" class="drawer__foot">
          <div class="drawer__total">
            <span>Subtotal</span>
            <span>${{ cartTotal }}</span>
          </div>
          <button class="btn" style="width: 100%;">Checkout</button>
        </div>
      </aside>
    </div>
  </transition>
</template>

<style scoped>
.drawer {
  position: fixed;
  inset: 0;
  z-index: 65;
  display: flex;
  justify-content: flex-end;
}

.drawer__scrim {
  position: absolute;
  inset: 0;
  background: rgba(17, 17, 17, 0.5);
}

.drawer__panel {
  position: relative;
  width: 100%;
  max-width: 400px;
  height: 100%;
  background: var(--paper);
  display: flex;
  flex-direction: column;
}

.drawer__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 24px 18px;
  border-bottom: 1px solid var(--line);
}

.drawer__head h3 {
  font-size: 1.1rem;
}

.drawer__close {
  background: none;
  border: none;
  font-size: 1rem;
  padding: 6px;
}

.drawer__empty {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  color: var(--taupe);
}

.drawer__items {
  flex: 1;
  overflow-y: auto;
  padding: 16px 24px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.drawer__item {
  display: flex;
  gap: 14px;
  position: relative;
}

.drawer__item img {
  width: 76px;
  height: 96px;
  object-fit: cover;
  flex-shrink: 0;
}

.drawer__item-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.drawer__item-name {
  font-weight: 600;
  font-size: 0.9rem;
  padding-right: 20px;
}

.drawer__item-size {
  font-size: 0.78rem;
  color: var(--taupe);
}

.drawer__item-row {
  margin-top: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.drawer__qty {
  display: flex;
  align-items: center;
  gap: 10px;
  border: 1px solid var(--line);
  padding: 4px 10px;
}

.drawer__qty button {
  background: none;
  border: none;
  font-size: 0.9rem;
  width: 16px;
}

.drawer__item-price {
  font-weight: 600;
  font-size: 0.88rem;
}

.drawer__remove {
  position: absolute;
  top: 0;
  right: 0;
  background: none;
  border: none;
  color: var(--taupe);
  font-size: 0.8rem;
  padding: 4px;
}

.drawer__foot {
  border-top: 1px solid var(--line);
  padding: 20px 24px 28px;
}

.drawer__total {
  display: flex;
  justify-content: space-between;
  font-weight: 600;
  margin-bottom: 14px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
