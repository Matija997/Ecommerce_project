<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>Shopping Cart</h2>

      <div v-if="cartItems.length === 0">Cart is empty.</div>

      <ul v-else>
        <li v-for="item in cartItems" :key="item.id">
          {{ item.name }} - ${{ item.price }} x {{ item.quantity }}
          <button @click="$emit('remove', item.id)">Remove</button>
        </li>
      </ul>

      <div v-if="cartItems.length > 0" style="margin-top:10px;font-weight:bold;">
        Total: ${{ total }}
      </div>

      <button class="close-btn" @click="$emit('close')">×</button>
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

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 3000;
}
.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  width: 350px;
  position: relative;
}
.close-btn {
  position: absolute;
  top: 8px;
  right: 10px;
  border: none;
  background: transparent;
  font-size: 22px;
  cursor: pointer;
}
</style>
