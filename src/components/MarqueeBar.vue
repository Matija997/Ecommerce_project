<script setup>
import { computed } from 'vue'

const items = [
  'FREE SHIPPING OVER $120',
  'NEW DROP — WEEK 27',
  'EASY 30-DAY RETURNS',
  'SALE UP TO 40% OFF'
]
const REPEATS = 6
const repeatedItems = computed(() =>
  Array.from({ length: REPEATS }, () => items).flat()
)
</script>

<template>
  <div class="marquee" aria-hidden="true">
    <div class="marquee__track">
      <span class="marquee__group">
        <span
          v-for="(item, i) in repeatedItems"
          :key="'a' + i"
          class="marquee__item"
        >
          {{ item }}
        </span>
      </span>
      <span class="marquee__group">
        <span
          v-for="(item, i) in repeatedItems"
          :key="'b' + i"
          class="marquee__item"
        >
          {{ item }}
        </span>
      </span>
    </div>
  </div>
</template>

<style scoped>
.marquee {
  background: var(--ink);
  color: var(--paper);
  overflow: hidden;
  white-space: nowrap;
  height: 34px;
  display: flex;
  align-items: center;
}

.marquee__track {
  display: flex;
  width: max-content;
  animation: scroll 100s linear infinite;
}

.marquee__group {
  display: flex;
  flex-shrink: 0;
}

.marquee__item {
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: var(--tracking-wide);
  padding: 0 28px;
  position: relative;
}

.marquee__item::after {
  content: '/';
  position: absolute;
  right: 0;
  color: var(--accent);
}

@keyframes scroll {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(-50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .marquee__track {
    animation: none;
  }
}
</style>
