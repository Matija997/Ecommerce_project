<template>
  <div class="shop-page">

    <!-- TOP BAR -->
    <div class="top-controls">
      <button @click="showFilters = true">☰ Filters</button>
      <button @click="showSort = true">⇅ Sort</button>

      <!-- ACTIVE FILTERS -->
      <div class="active-filters" v-if="activeFilters.length">
        <span v-for="(f, index) in activeFilters" :key="index" class="active-filter">
          {{ f.label }} <button @click="removeFilter(f)">×</button>
        </span>
      </div>
    </div>

    <!-- OVERLAY -->
    <div class="overlay" v-if="showFilters || showSort" @click="closePanels"></div>

    <!-- FILTER PANEL -->
    <aside class="side-panel" :class="{ open: showFilters }">
      <h3>Filters</h3>

      <div class="filter-group">
        <h4>Category</h4>
        <label v-for="c in categories" :key="c.value">
          <input type="checkbox" v-model="filters.category" :value="c.value">
          {{ c.label }} ({{ countByCategory(c.value) }})
        </label>
      </div>

      <div class="filter-group">
        <h4>Brand</h4>
        <label v-for="b in brands" :key="b.value">
          <input type="checkbox" v-model="filters.brand" :value="b.value">
          {{ b.label }} ({{ countByBrand(b.value) }})
        </label>
      </div>

      <div class="filter-group">
        <h4>Gender</h4>
        <label v-for="g in genders" :key="g.value">
          <input type="checkbox" v-model="filters.gender" :value="g.value">
          {{ g.label }} ({{ countByGender(g.value) }})
        </label>
      </div>

      <div class="filter-group">
        <h4>Size</h4>
        <label v-for="s in sizes" :key="s.value">
          <input type="checkbox" v-model="filters.size" :value="s.value">
          {{ s.label }} ({{ countBySize(s.value) }})
        </label>
      </div>

      <button class="apply-btn" @click="closePanels">Apply</button>
    </aside>

    <!-- SORT PANEL -->
    <aside class="side-panel" :class="{ open: showSort }">
      <h3>Sort by</h3>

      <label>
        <input type="radio" v-model="sortBy" value="price-asc">
        Price: Low → High
      </label>

      <label>
        <input type="radio" v-model="sortBy" value="price-desc">
        Price: High → Low
      </label>

      <label>
        <input type="radio" v-model="sortBy" value="name">
        Name (A-Z)
      </label>

      <button class="apply-btn" @click="closePanels">Apply</button>
    </aside>

    <!-- PRODUCTS -->
    <section class="products">
      <router-link
        v-for="product in filteredProducts"
        :key="product.id"
        :to="`/men/clothing/${product.name.toLowerCase().replace(/\s+/g,'-')}`"
        style="color: inherit; text-decoration: none;"
        >
        <div class="product-card">
            <img :src="product.image" />
            <h4>{{ product.name }}</h4>
            <p>${{ product.price }}</p>
        </div>
        </router-link>
    </section>

  </div>
</template>

<script>
import nikeTshirt from "@/assets/NikeT-shirt.jpg"

export default {
  data() {
    return {
      showFilters: false,
      showSort: false,
      sortBy: "",

      filters: {
        category: [],
        brand: [],
        gender: ["men", "unisex"],
        size: []
      },

      products: [
        { id: 1, name: "Nike T-Shirt", category: "tshirt", brand: "nike", gender: "men", size: ["S","M","L"], price: 29, image: nikeTshirt },
        { id: 2, name: "Adidas Jacket", category: "jacket", brand: "adidas", gender: "men", size: ["L","XL"], price: 99, image: "https://via.placeholder.com/200" },
        { id: 3, name: "Puma Jeans", category: "jeans", brand: "puma", gender: "unisex", size: ["M","L","XL"], price: 59, image: "https://via.placeholder.com/200" },
        { id: 4, name: "Nike Hoodie", category: "jacket", brand: "nike", gender: "unisex", size: ["M","L"], price: 79, image: "https://via.placeholder.com/200" },
        { id: 5, name: "Adidas T-Shirt", category: "tshirt", brand: "adidas", gender: "men", size: ["S","M"], price: 25, image: "https://via.placeholder.com/200" },
        { id: 6, name: "Puma Jacket", category: "jacket", brand: "puma", gender: "men", size: ["L","XL"], price: 120, image: "https://via.placeholder.com/200" },
        { id: 7, name: "Nike Jeans", category: "jeans", brand: "nike", gender: "unisex", size: ["M","L"], price: 65, image: "https://via.placeholder.com/200" },
        { id: 8, name: "Adidas Hoodie", category: "jacket", brand: "adidas", gender: "unisex", size: ["XL"], price: 89, image: "https://via.placeholder.com/200" }
      ],

      categories: [
        { value: "tshirt", label: "T-Shirt" },
        { value: "jacket", label: "Jacket" },
        { value: "jeans", label: "Jeans" }
      ],
      brands: [
        { value: "nike", label: "Nike" },
        { value: "adidas", label: "Adidas" },
        { value: "puma", label: "Puma" }
      ],
      genders: [
        { value: "men", label: "Men" },
        { value: "unisex", label: "Unisex" },
        { value: "women", label: "Women" }
      ],
      sizes: [
        { value: "S", label: "S" },
        { value: "M", label: "M" },
        { value: "L", label: "L" },
        { value: "XL", label: "XL" }
      ]
    }
  },

  computed: {
    filteredProducts() {
      let list = this.products.filter(p => {
        const catOk = !this.filters.category.length || this.filters.category.includes(p.category)
        const brandOk = !this.filters.brand.length || this.filters.brand.includes(p.brand)
        const genderOk = !this.filters.gender.length || this.filters.gender.includes(p.gender)
        const sizeOk = !this.filters.size.length || p.size.some(s => this.filters.size.includes(s))
        return catOk && brandOk && genderOk && sizeOk
      })

      if (this.sortBy === "price-asc") list.sort((a,b)=>a.price-b.price)
      if (this.sortBy === "price-desc") list.sort((a,b)=>b.price-a.price)
      if (this.sortBy === "name") list.sort((a,b)=>a.name.localeCompare(b.name))

      return list
    },

    activeFilters() {
      const arr = []
      this.filters.category.forEach(c => arr.push({ type: 'category', value: c, label: this.categories.find(x=>x.value===c)?.label || c }))
      this.filters.brand.forEach(b => arr.push({ type: 'brand', value: b, label: this.brands.find(x=>x.value===b)?.label || b }))
      this.filters.gender.forEach(g => arr.push({ type: 'gender', value: g, label: this.genders.find(x=>x.value===g)?.label || g }))
      this.filters.size.forEach(s => arr.push({ type: 'size', value: s, label: s }))
      return arr
    }
  },

  methods: {
    closePanels() {
      this.showFilters = false
      this.showSort = false
    },
    removeFilter(f) {
      this.filters[f.type] = this.filters[f.type].filter(v => v !== f.value)
    },

    // ✅ Counts considering other filters & multiple sizes
    countByCategory(value) {
      return this.products.filter(p => {
        const brandOk = !this.filters.brand.length || this.filters.brand.includes(p.brand)
        const genderOk = !this.filters.gender.length || this.filters.gender.includes(p.gender)
        const sizeOk = !this.filters.size.length || p.size.some(s => this.filters.size.includes(s))
        return p.category === value && brandOk && genderOk && sizeOk
      }).length
    },
    countByBrand(value) {
      return this.products.filter(p => {
        const categoryOk = !this.filters.category.length || this.filters.category.includes(p.category)
        const genderOk = !this.filters.gender.length || this.filters.gender.includes(p.gender)
        const sizeOk = !this.filters.size.length || p.size.some(s => this.filters.size.includes(s))
        return p.brand === value && categoryOk && genderOk && sizeOk
      }).length
    },
    countByGender(value) {
      return this.products.filter(p => {
        const categoryOk = !this.filters.category.length || this.filters.category.includes(p.category)
        const brandOk = !this.filters.brand.length || this.filters.brand.includes(p.brand)
        const sizeOk = !this.filters.size.length || p.size.some(s => this.filters.size.includes(s))
        return p.gender === value && categoryOk && brandOk && sizeOk
      }).length
    },
    countBySize(value) {
      return this.products.filter(p => {
        const categoryOk = !this.filters.category.length || this.filters.category.includes(p.category)
        const brandOk = !this.filters.brand.length || this.filters.brand.includes(p.brand)
        const genderOk = !this.filters.gender.length || this.filters.gender.includes(p.gender)
        return p.size.includes(value) && categoryOk && brandOk && genderOk
      }).length
    }
  }
}
</script>

<style scoped>
.shop-page {
  padding: 100px;
  padding-top: 60px;
}

/* TOP BAR */
.top-controls {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 20px;
}
.active-filters {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-left: 10px;
}
.active-filter {
  background: #eee;
  padding: 2px 5px;
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: small;
}
.active-filter button {
  background: transparent;
  border: none;
  cursor: pointer;
}

/* OVERLAY */
.overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.4);
  z-index: 9;
}

/* SIDE PANEL */
.side-panel {
  position: fixed;
  top: 0;
  left: -300px;
  width: 300px;
  height: 100vh;
  background: #fff;
  z-index: 10;
  transition: left 0.3s ease;
  overflow-y: auto;
}
.side-panel.open { left: 0; }
.side-panel h3 { text-align: center; }

.filter-group {
  margin-bottom: 10px;
  margin-left: 10px;
}
.filter-group label, .side-panel label {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 5px 0;
  cursor: pointer;
}

.apply-btn {
  width: 90%;
  margin: 20px auto 0;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* PRODUCTS */
.products {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  padding: 20px;
}
.product-card {
  border: 1px solid #ccc;
  padding: 10px;
  text-align: center;
  border-radius: 8px;
}
.product-card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
}
</style>
