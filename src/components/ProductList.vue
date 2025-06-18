<template>
  <div>
    <h2>Products</h2>
    <div v-for="product in products" :key="product.id" style="border: 1px solid #ddd; margin-bottom: 10px; padding: 10px;">
      <ProductItem :product="product" @add-to-cart="$emit('add-to-cart', product)" />
    </div>
  </div>
</template>

<script>
import ProductItem from './ProductItem.vue'

export default {
  components: { ProductItem },
  props: {
    products: Array
  }
}
</script>
