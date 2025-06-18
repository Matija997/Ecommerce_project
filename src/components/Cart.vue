<template>
  <div style="border: 1px solid #aaa; padding: 10px; margin-bottom: 20px;">
    <h2>Shopping Cart</h2>
    <div v-if="cartItems.length === 0">Cart is empty.</div>
    <ul v-else>
      <li v-for="item in cartItems" :key="item.id" style="margin-bottom: 5px;">
        {{ item.name }} - ${{ item.price }} x {{ item.quantity }} = ${{ item.price * item.quantity }}
        <button @click="$emit('remove', item.id)" style="margin-left: 10px;">Remove</button>
      </li>
    </ul>
    <div v-if="cartItems.length > 0" style="margin-top: 10px; font-weight: bold;">
      Total: ${{ total }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    cartItems: Array
  },
  computed: {
    total() {
      return this.cartItems.reduce((sum, item) => sum + item.price * item.quantity, 0)
    }
  }
}
</script>
