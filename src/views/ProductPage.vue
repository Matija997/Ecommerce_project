<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useStore } from '../store/useStore'
import { useProducts } from '../store/useProducts'
import { formatPrice } from '../utils/currency'

const route = useRoute()
const { addToCart } = useStore()
const { getById } = useProducts()

const selectedSize = ref(null)
const activeImageIndex = ref(0)

const product = computed(() => getById(route.params.id))

watch(
  () => route.params.id,
  () => {
    selectedSize.value = null
    activeImageIndex.value = 0
  }
)

function addSelectedToCart() {
  if (!selectedSize.value) return
  addToCart(product.value, selectedSize.value)
}
</script>

<template>
  <div v-if="product" class="product container">
    <div class="product__gallery">
      <div class="product__media">
        <img :src="product.images[activeImageIndex]" :alt="product.name" />
      </div>
      <div class="product__thumbs">
        <button
          v-for="(image, index) in product.images"
          :key="index"
          class="product__thumb"
          :class="{ 'product__thumb--active': activeImageIndex === index }"
          @click="activeImageIndex = index"
        >
          <img :src="image" :alt="`${product.name} view ${index + 1}`" />
        </button>
      </div>
    </div>

    <div class="product__info">
      <span v-if="product.tag" class="eyebrow">{{ product.tag }}</span>
      <h1 class="product__name">{{ product.name }}</h1>

      <div class="product__price">
        <span v-if="product.salePrice" class="product__price--was">{{ formatPrice(product.price) }}</span>
        <span :class="{ 'product__price--sale': product.salePrice }">
          {{ formatPrice(product.salePrice || product.price) }}
        </span>
      </div>

      <div class="product__sizes">
        <span class="product__sizes-label">Size</span>
        <div class="product__size-grid">
          <button
            v-for="size in product.sizes"
            :key="size.size"
            class="product__size"
            :class="{
              'product__size--active': selectedSize === size.size,
              'product__size--unavailable': !size.available
            }"
            :disabled="!size.available"
            @click="selectedSize = size.size"
          >
            {{ size.size }}
          </button>
        </div>
      </div>

      <button class="btn" style="width: 100%;" :disabled="!selectedSize" @click="addSelectedToCart">
        {{ selectedSize ? 'Add to Bag' : 'Select a size' }}
      </button>

      <p class="product__note">Free shipping over 12.000 RSD · Easy 30-day returns</p>
    </div>
  </div>

  <div v-else class="notfound container">
    <span class="eyebrow">Error 404</span>
    <h1 class="notfound__title">This product walked off the rack.</h1>
    <router-link to="/" class="btn">Back to Home</router-link>
  </div>
</template>

<style scoped>
.product {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 56px;
  padding: 48px 32px 100px;
}

.product__media {
  aspect-ratio: 3 / 4;
  overflow: hidden;
  background: var(--stone);
}

.product__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product__thumbs {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 12px;
}

.product__thumb {
  width: 64px;
  aspect-ratio: 3 / 4;
  padding: 0;
  border: 1px solid var(--line);
  overflow: hidden;
  opacity: 0.7;
  transition: opacity 0.15s ease, border-color 0.15s ease;
}

.product__thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product__thumb--active {
  opacity: 1;
  border-color: var(--ink);
}

.product__info {
  display: flex;
  flex-direction: column;
  padding-top: 8px;
}

.product__name {
  font-size: clamp(1.8rem, 3.5vw, 2.6rem);
  margin: 10px 0 18px;
}

.product__price {
  display: flex;
  gap: 12px;
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 32px;
}

.product__price--was {
  color: var(--taupe);
  text-decoration: line-through;
  font-weight: 400;
}

.product__price--sale {
  color: var(--accent);
}

.product__sizes {
  margin-bottom: 28px;
}

.product__sizes-label {
  display: block;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  color: var(--taupe);
  margin-bottom: 10px;
}

.product__size-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.product__size {
  min-width: 48px;
  background: transparent;
  border: 1px solid var(--line);
  padding: 10px 12px;
  font-size: 0.82rem;
  font-weight: 600;
  transition: border-color 0.15s ease, background 0.15s ease;
}

.product__size:hover {
  border-color: var(--ink);
}

.product__size--active {
  border-color: var(--ink);
  background: var(--ink);
  color: var(--paper);
}

.product__size--unavailable {
  color: var(--taupe);
  text-decoration: line-through;
  cursor: not-allowed;
}

.product__size--unavailable:hover {
  border-color: var(--line);
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.product__note {
  margin-top: 16px;
  font-size: 0.78rem;
  color: var(--taupe);
  text-align: center;
}

.notfound {
  min-height: 50vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 16px;
  padding: 100px 32px;
}

.notfound__title {
  font-size: clamp(1.8rem, 4vw, 2.6rem);
  max-width: 18ch;
}

@media (max-width: 780px) {
  .product {
    grid-template-columns: 1fr;
    gap: 28px;
    padding: 32px 18px 60px;
  }
}
</style>
