<script setup>
import ProductCard from '../components/ProductCard.vue'
import { products } from '../data/products'

const featured = products.filter((p) => p.tag === 'New').slice(0, 4)
</script>

<template>
  <div class="home">
    <!-- Hero -->
    <section class="hero container">
      <div class="hero__copy">
        <span class="eyebrow">Week 27 — New Arrivals</span>
        <h1 class="hero__title">
          Dress for<br />
          the day<br />
          you have.
        </h1>
        <p class="hero__sub">
          Considered basics and statement outerwear, cut for real movement
          and built to outlast a season.
        </p>
        <div class="hero__ctas">
          <router-link to="/man" class="btn">Shop Man</router-link>
          <router-link to="/woman" class="btn btn-outline">Shop Woman</router-link>
        </div>
      </div>
      <div class="hero__media">
        <img src="https://picsum.photos/seed/friso-hero/900/1100" alt="Latest FRISO collection" />
      </div>
    </section>

    <!-- Category split -->
    <section class="split">
      <router-link to="/man" class="split__panel">
        <img src="https://picsum.photos/seed/friso-cat-man/800/1000" alt="Man category" />
        <span class="split__label">Man</span>
      </router-link>
      <router-link to="/woman" class="split__panel">
        <img src="https://picsum.photos/seed/friso-cat-woman/800/1000" alt="Woman category" />
        <span class="split__label">Woman</span>
      </router-link>
      <router-link to="/sale" class="split__panel split__panel--accent">
        <img src="https://picsum.photos/seed/friso-cat-sale/800/1000" alt="Sale category" />
        <span class="split__label">Sale</span>
      </router-link>
    </section>

    <!-- Featured -->
    <section class="container featured">
      <div class="featured__head">
        <div>
          <span class="eyebrow">Just landed</span>
          <h2 class="featured__title">New this week</h2>
        </div>
        <router-link to="/man" class="featured__all">View all →</router-link>
      </div>

      <div class="featured__grid">
        <ProductCard v-for="product in featured" :key="product.id" :product="product" />
      </div>
    </section>

    <!-- Statement -->
    <section class="statement container">
      <p>
        No trend cycles. No filler drops. Just clothes we'd wear on
        <span class="statement__accent">repeat</span>.
      </p>
    </section>
  </div>
</template>

<style scoped>
.hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  gap: 48px;
  padding-top: 56px;
  padding-bottom: 64px;
}

.hero__title {
  font-size: clamp(2.6rem, 6vw, 4.6rem);
  margin: 14px 0 22px;
}

.hero__sub {
  max-width: 40ch;
  color: var(--taupe);
  font-size: 1.02rem;
  margin-bottom: 30px;
}

.hero__ctas {
  display: flex;
  gap: 14px;
}

.hero__media img {
  width: 100%;
  aspect-ratio: 4 / 5;
  object-fit: cover;
}

.split {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.split__panel {
  position: relative;
  aspect-ratio: 4 / 5;
  overflow: hidden;
  display: block;
}

.split__panel img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.split__panel:hover img {
  transform: scale(1.05);
}

.split__label {
  position: absolute;
  left: 20px;
  bottom: 20px;
  color: var(--white);
  font-family: var(--font-display);
  font-size: 1.6rem;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.35);
}

.split__panel--accent .split__label {
  color: var(--white);
}

.split__panel--accent::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 40%, rgba(178, 58, 46, 0.55));
  pointer-events: none;
}

.featured {
  padding: 88px 32px 40px;
}

.featured__head {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 32px;
}

.featured__title {
  font-size: 1.8rem;
  margin-top: 6px;
}

.featured__all {
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
}

.featured__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 28px;
}

.statement {
  padding: 40px 32px 100px;
  text-align: center;
}

.statement p {
  font-family: var(--font-display);
  font-size: clamp(1.6rem, 4vw, 2.6rem);
  max-width: 18ch;
  margin: 0 auto;
  line-height: 1.15;
}

.statement__accent {
  color: var(--accent);
}

@media (max-width: 960px) {
  .hero {
    grid-template-columns: 1fr;
  }

  .featured__grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .split {
    grid-template-columns: 1fr;
  }
}
</style>
