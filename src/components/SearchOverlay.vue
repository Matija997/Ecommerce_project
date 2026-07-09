<script setup>
import { computed, nextTick, watch, ref } from 'vue'
import { useStore } from '../store/useStore'
import { searchProducts } from '../data/products'

const { state, toggleSearch, addToCart } = useStore()
const inputRef = ref(null)

const results = computed(() => searchProducts(state.searchQuery))

watch(
  () => state.isSearchOpen,
  async (open) => {
    if (open) {
      await nextTick()
      inputRef.value?.focus()
    }
  }
)

function quickAdd(product) {
  addToCart(product, product.sizes[0])
}
</script>

<template>
  <transition name="fade">
    <div v-if="state.isSearchOpen" class="overlay" @keydown.esc="toggleSearch(false)">
      <div class="overlay__scrim" @click="toggleSearch(false)"></div>

      <div class="overlay__panel">
        <div class="container overlay__top">
          <div class="overlay__input-wrap">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6">
              <circle cx="11" cy="11" r="7" />
              <line x1="21" y1="21" x2="16.2" y2="16.2" />
            </svg>
            <input
              ref="inputRef"
              v-model="state.searchQuery"
              type="text"
              placeholder="Search for jackets, denim, dresses…"
              class="overlay__input"
            />
          </div>
          <button class="overlay__close" aria-label="Close search" @click="toggleSearch(false)">
            ✕
          </button>
        </div>

        <div class="container overlay__results">
          <p v-if="!state.searchQuery" class="overlay__hint">
            Try “coat”, “denim”, or “man”.
          </p>
          <p v-else-if="results.length === 0" class="overlay__hint">
            No results for “{{ state.searchQuery }}”.
          </p>

          <div v-else class="overlay__grid">
            <button
              v-for="product in results"
              :key="product.id"
              class="overlay__result"
              @click="quickAdd(product)"
            >
              <img :src="product.image" :alt="product.name" />
              <span class="overlay__result-name">{{ product.name }}</span>
              <span class="overlay__result-price">
                ${{ product.salePrice || product.price }}
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<style scoped>
.overlay {
  position: fixed;
  inset: 0;
  z-index: 60;
  display: flex;
}

.overlay__scrim {
  position: absolute;
  inset: 0;
  background: rgba(17, 17, 17, 0.5);
}

.overlay__panel {
  position: relative;
  background: var(--paper);
  width: 100%;
  max-height: 84vh;
  overflow-y: auto;
  padding-bottom: 40px;
}

.overlay__top {
  display: flex;
  align-items: center;
  gap: 16px;
  padding-top: 32px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--line);
}

.overlay__input-wrap {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--taupe);
}

.overlay__input {
  flex: 1;
  border: none;
  background: transparent;
  font-family: var(--font-display);
  font-size: 1.6rem;
  color: var(--ink);
  outline: none;
}

.overlay__close {
  background: none;
  border: none;
  font-size: 1.2rem;
  padding: 8px;
}

.overlay__results {
  padding-top: 28px;
}

.overlay__hint {
  color: var(--taupe);
  font-size: 0.9rem;
}

.overlay__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 20px;
}

.overlay__result {
  text-align: left;
  background: none;
  border: none;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.overlay__result img {
  aspect-ratio: 3 / 4;
  object-fit: cover;
  width: 100%;
}

.overlay__result-name {
  font-size: 0.82rem;
  font-weight: 600;
}

.overlay__result-price {
  font-size: 0.8rem;
  color: var(--taupe);
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
