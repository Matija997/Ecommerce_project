<script setup>
import { ref, computed } from 'vue'
import ProductCard from '../components/ProductCard.vue'
import { useProducts } from '../store/useProducts'

const { getByCategory } = useProducts()

const props = defineProps({
  category: { type: String, required: true },
  title: { type: String, required: true }
})

const sort = ref('featured')
const filter = ref('all')
const subtype = ref('all')

const base = computed(() => getByCategory(props.category))

const filtered = computed(() => {
  let list = base.value
  if (filter.value === 'new') list = list.filter((p) => p.tag === 'New')
  if (filter.value === 'sale') list = list.filter((p) => p.salePrice)
  if (subtype.value !== 'all') list = list.filter((p) => p.subtype === subtype.value)
  return list
})

const sorted = computed(() => {
  const list = [...filtered.value]
  if (sort.value === 'price-asc') {
    list.sort((a, b) => (a.salePrice || a.price) - (b.salePrice || b.price))
  } else if (sort.value === 'price-desc') {
    list.sort((a, b) => (b.salePrice || b.price) - (a.salePrice || a.price))
  }
  return list
})
</script>

<template>
  <div class="category">
    <header class="category__head container">
      <span class="eyebrow">Collection</span>
      <h1 class="category__title">{{ title }}</h1>
      <p class="category__count">{{ sorted.length }} items</p>
    </header>

    <div class="container category__bar">
      <div class="category__filters">
        <button
          v-for="opt in [
            { key: 'all', label: 'All' },
            { key: 'new', label: 'New' },
            { key: 'sale', label: 'Sale' }
          ]"
          :key="opt.key"
          class="category__chip"
          :class="{ 'category__chip--active': filter === opt.key }"
          @click="filter = opt.key"
        >
          {{ opt.label }}
        </button>
      </div>

      <div class="category__selects">
        <label class="category__sort">
          Category
          <select v-model="subtype">
            <option value="all">All Categories</option>
            <optgroup label="Clothing">
              <option value="tshirt">T-Shirts</option>
              <option value="jacket">Jacket</option>
              <option value="denim">Denim</option>
            </optgroup>
            <optgroup label="Accessories">
              <option value="glasses">Glasses</option>
              <option value="hats">Hats</option>
              <option value="bags">Bags</option>
            </optgroup>
          </select>
        </label>

        <label class="category__sort">
          Sort by
          <select v-model="sort">
            <option value="featured">Featured</option>
            <option value="price-asc">Price: Low to High</option>
            <option value="price-desc">Price: High to Low</option>
          </select>
        </label>
      </div>
    </div>

    <section class="container category__grid">
      <ProductCard v-for="product in sorted" :key="product.id" :product="product" />

      <p v-if="sorted.length === 0" class="category__empty">
        No items match this filter yet.
      </p>
    </section>
  </div>
</template>

<style scoped>
.category__head {
  padding: 48px 32px 20px;
}

.category__title {
  font-size: clamp(2.4rem, 5vw, 3.4rem);
  margin: 8px 0 8px;
}

.category__count {
  color: var(--taupe);
  font-size: 0.85rem;
}

.category__bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 32px;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  margin-bottom: 40px;
  flex-wrap: wrap;
  gap: 14px;
}

.category__filters {
  display: flex;
  gap: 10px;
}

.category__selects {
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
}

.category__chip {
  border: 1px solid var(--line);
  background: transparent;
  padding: 8px 16px;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  transition: border-color 0.15s ease, background 0.15s ease;
}

.category__chip--active {
  border-color: var(--ink);
  background: var(--ink);
  color: var(--paper);
}

.category__sort {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--taupe);
  letter-spacing: var(--tracking);
  text-transform: uppercase;
}

.category__sort select {
  font-family: var(--font-body);
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--ink);
  border: 1px solid var(--line);
  background: var(--white);
  padding: 6px 10px;
  text-transform: none;
  letter-spacing: normal;
}

.category__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 28px;
  padding: 0 32px 100px;
}

.category__empty {
  grid-column: 1 / -1;
  text-align: center;
  color: var(--taupe);
  padding: 60px 0;
}

@media (max-width: 960px) {
  .category__grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 560px) {
  .category__bar {
    flex-direction: column;
    align-items: flex-start;
  }

  .category__selects {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
}
</style>
