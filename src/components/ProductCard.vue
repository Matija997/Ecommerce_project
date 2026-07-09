<script setup>
import { ref } from 'vue'
import { useStore } from '../store/useStore'

const props = defineProps({
  product: { type: Object, required: true }
})

const { addToCart } = useStore()

const showSizes = ref(false)

function pick(size) {
  addToCart(props.product, size)
  showSizes.value = false
}
</script>

<template>
  <article class="card">
    <div class="card__media">
      <img :src="product.image" :alt="product.name" class="card__img card__img--front" loading="lazy" />
      <img :src="product.imageAlt" :alt="`${product.name} alternate view`" class="card__img card__img--back" loading="lazy" />

      <span v-if="product.tag" class="card__tag" :class="{ 'card__tag--sale': product.tag === 'Sale' }">
        {{ product.tag }}
      </span>

      <button class="card__add" @click="showSizes = !showSizes">
        {{ showSizes ? 'Close' : 'Quick add' }}
      </button>

      <div v-if="showSizes" class="card__sizes">
        <button
          v-for="size in product.sizes"
          :key="size"
          class="card__size"
          @click="pick(size)"
        >
          {{ size }}
        </button>
      </div>
    </div>

    <div class="card__info">
      <h4 class="card__name">{{ product.name }}</h4>
      <div class="card__price">
        <span v-if="product.salePrice" class="card__price--was">${{ product.price }}</span>
        <span :class="{ 'card__price--sale': product.salePrice }">
          ${{ product.salePrice || product.price }}
        </span>
      </div>
    </div>
  </article>
</template>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
}

.card__media {
  position: relative;
  aspect-ratio: 3 / 4;
  overflow: hidden;
  background: var(--stone);
}

.card__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: opacity 0.35s ease, transform 0.5s ease;
}

.card__img--back {
  opacity: 0;
}

.card__media:hover .card__img--front {
  opacity: 0;
}

.card__media:hover .card__img--back {
  opacity: 1;
  transform: scale(1.03);
}

.card__tag {
  position: absolute;
  top: 12px;
  left: 12px;
  background: var(--ink);
  color: var(--paper);
  font-size: 0.66rem;
  font-weight: 700;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  padding: 5px 10px;
}

.card__tag--sale {
  background: var(--accent);
}

.card__add {
  position: absolute;
  left: 10px;
  right: 10px;
  bottom: 10px;
  background: var(--paper);
  border: 1px solid var(--ink);
  padding: 10px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.card__media:hover .card__add {
  opacity: 1;
  transform: translateY(0);
}

.card__sizes {
  position: absolute;
  left: 10px;
  right: 10px;
  bottom: 10px;
  background: var(--paper);
  border: 1px solid var(--ink);
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  padding: 10px;
}

.card__size {
  flex: 1 1 auto;
  min-width: 34px;
  background: transparent;
  border: 1px solid var(--line);
  padding: 6px 4px;
  font-size: 0.72rem;
  font-weight: 600;
  transition: border-color 0.15s ease, background 0.15s ease;
}

.card__size:hover {
  border-color: var(--ink);
  background: var(--stone);
}

.card__info {
  padding-top: 14px;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 12px;
}

.card__name {
  font-family: var(--font-body);
  font-weight: 600;
  font-size: 0.92rem;
}

.card__price {
  display: flex;
  gap: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  white-space: nowrap;
}

.card__price--was {
  color: var(--taupe);
  text-decoration: line-through;
  font-weight: 400;
}

.card__price--sale {
  color: var(--accent);
}

@media (hover: none) {
  .card__img--back {
    display: none;
  }

  .card__add {
    opacity: 1;
    transform: none;
    position: static;
    margin-top: 8px;
  }

  .card__sizes {
    position: static;
    margin-top: 8px;
  }
}
</style>
