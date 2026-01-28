<template>
  <div class="shop-page">

    <!-- TOP BAR -->
    <div class="top-controls">
      <button @click="showFilters = true">☰ Filters</button>
      <button @click="showSort = true">⇅ Sort</button>
    </div>

    <!-- OVERLAY -->
    <div class="overlay" v-if="showFilters || showSort" @click="closePanels"></div>

    <!-- FILTER PANEL -->
    <aside class="side-panel" :class="{ open: showFilters }">
      <h3>Filters</h3>

      <div class="filter-group">
        <h4>Category</h4>
        <label><input type="checkbox" v-model="filters.category" value="tshirt"> T-Shirt</label>
        <label><input type="checkbox" v-model="filters.category" value="jacket"> Jacket</label>
        <label><input type="checkbox" v-model="filters.category" value="jeans"> Jeans</label>
      </div>

      <div class="filter-group">
        <h4>Brand</h4>
        <label><input type="checkbox" v-model="filters.brand" value="nike"> Nike</label>
        <label><input type="checkbox" v-model="filters.brand" value="adidas"> Adidas</label>
        <label><input type="checkbox" v-model="filters.brand" value="puma"> Puma</label>
      </div>

      <div class="filter-group">
        <h4>Gender</h4>
        <label><input type="checkbox" v-model="filters.gender" value="men"> Men</label>
        <label><input type="checkbox" v-model="filters.gender" value="unisex"> Unisex</label>
        <label><input type="checkbox" v-model="filters.gender" value="women"> Women</label>
      </div>

      <div class="filter-group">
        <h4>Size</h4>
        <label><input type="checkbox" v-model="filters.size" value="S"> S</label>
        <label><input type="checkbox" v-model="filters.size" value="M"> M</label>
        <label><input type="checkbox" v-model="filters.size" value="L"> L</label>
        <label><input type="checkbox" v-model="filters.size" value="XL"> XL</label>
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
      <div class="product-card" v-for="product in filteredProducts" :key="product.id">
        <img :src="product.image" />
        <h4>{{ product.name }}</h4>
        <p>${{ product.price }}</p>
        <small>Size: {{ product.size }}</small>
      </div>
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
        { id: 1, name: "Nike T-Shirt", category: "tshirt", brand: "nike", gender: "men", size: "M", price: 29, image: nikeTshirt },
        { id: 2, name: "Adidas Jacket", category: "jacket", brand: "adidas", gender: "men", size: "L", price: 99, image: "https://via.placeholder.com/200" },
        { id: 3, name: "Puma Jeans", category: "jeans", brand: "puma", gender: "unisex", size: "XL", price: 59, image: "https://via.placeholder.com/200" },
        { id: 4, name: "Nike Hoodie", category: "jacket", brand: "nike", gender: "unisex", size: "M", price: 79, image: "https://via.placeholder.com/200" },
        { id: 5, name: "Adidas T-Shirt", category: "tshirt", brand: "adidas", gender: "men", size: "S", price: 25, image: "https://via.placeholder.com/200" },
        { id: 6, name: "Puma Jacket", category: "jacket", brand: "puma", gender: "men", size: "L", price: 120, image: "https://via.placeholder.com/200" },
        { id: 7, name: "Nike Jeans", category: "jeans", brand: "nike", gender: "unisex", size: "M", price: 65, image: "https://via.placeholder.com/200" },
        { id: 8, name: "Adidas Hoodie", category: "jacket", brand: "adidas", gender: "unisex", size: "XL", price: 89, image: "https://via.placeholder.com/200" }
      ]
    }
  },

  computed: {
    filteredProducts() {
      let list = this.products.filter(p => {
        const catOk = !this.filters.category.length || this.filters.category.includes(p.category)
        const brandOk = !this.filters.brand.length || this.filters.brand.includes(p.brand)
        const genderOk = !this.filters.gender.length || this.filters.gender.includes(p.gender)
        const sizeOk = !this.filters.size.length || this.filters.size.includes(p.size)
        return catOk && brandOk && genderOk && sizeOk
      })

      if (this.sortBy === "price-asc") {
        list.sort((a, b) => a.price - b.price)
      }
      if (this.sortBy === "price-desc") {
        list.sort((a, b) => b.price - a.price)
      }
      if (this.sortBy === "name") {
        list.sort((a, b) => a.name.localeCompare(b.name))
      }

      return list
    }
  },

  methods: {
    closePanels() {
      this.showFilters = false
      this.showSort = false
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
  justify-content: flex-start;
  gap: 10px;
  padding: 10px 20px;
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
.side-panel h3 {
  text-align: center;
}
.side-panel.open {
  left: 0;
}

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
  margin-left: 10px;
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
