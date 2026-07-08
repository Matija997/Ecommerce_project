<template>
  <div class="product-page" v-if="product">
    <h2>{{ product.name }}</h2>
    <img :src="product.image" alt="" />
    <p>Price: ${{ product.price }}</p>
    <p>Sizes: {{ product.size.join(', ') }}</p>
  </div>

  <div v-else>
    <p>Product not found.</p>
  </div>
</template>

<script>
import { products } from "@/data/products.js"

export default {
  props: ['productName'],
  data() {
    return {
      product: null
    }
  },
  mounted() {
    this.loadProduct()
  },
  watch: {
    '$route.params.productName': 'loadProduct'
  },
  methods: {
    loadProduct() {
      const slug = this.$route.params.productName.toLowerCase()
      this.product = products.find(p => 
        p.name.toLowerCase().replace(/\s+/g,'-') === slug
      )
    }
  }
}
</script>

<style scoped>
.product-page {
  padding: 100px 20px 20px 20px;
  text-align: center;
}
.product-page img {
  max-width: 400px;
  width: 100%;
  object-fit: contain;
  margin: 20px 0;
}
</style>
