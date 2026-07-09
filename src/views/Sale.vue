<script setup>
import ProductCard from '../components/ProductCard.vue'
import { getOnSale } from '../data/products'

const saleItems = getOnSale()
</script>

<template>
  <div class="sale">
    <section class="sale__banner">
      <div class="sale__ribbon">
        <span v-for="n in 8" :key="n">Up to 40% off —</span>
      </div>
      <div class="container sale__banner-copy">
        <span class="eyebrow" style="color: #f1ded9;">Limited time</span>
        <h1 class="sale__title">The Sale</h1>
        <p class="sale__sub">
          Season-end favorites, marked down while sizes last.
        </p>
      </div>
    </section>

    <section class="container sale__grid">
      <ProductCard v-for="product in saleItems" :key="product.id" :product="product" />
    </section>
  </div>
</template>

<style scoped>
.sale__banner {
  position: relative;
  background: var(--ink);
  color: var(--white);
  overflow: hidden;
  padding: 60px 0 46px;
}

.sale__ribbon {
  position: absolute;
  top: 18px;
  left: -10%;
  width: 120%;
  display: flex;
  gap: 24px;
  transform: rotate(-2deg);
  color: var(--accent);
  font-family: var(--font-display);
  font-size: 1rem;
  letter-spacing: 0.04em;
  white-space: nowrap;
  opacity: 0.85;
}

.sale__banner-copy {
  position: relative;
  padding-top: 30px;
}

.sale__title {
  font-size: clamp(2.6rem, 6vw, 4rem);
  margin: 10px 0 12px;
}

.sale__sub {
  color: #cfc9bc;
  max-width: 40ch;
}

.sale__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 28px;
  padding: 56px 32px 100px;
}

@media (max-width: 960px) {
  .sale__grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
