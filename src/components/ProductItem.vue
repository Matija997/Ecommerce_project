<template>
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <div>
      <strong>{{ product.name }}</strong> - ${{ product.price }}
    </div>
    <button @click="$emit('add-to-cart')">Add to cart</button>
  </div>
</template>

<script>
export default {
  props: {
    product: Object
  }
}
</script>
