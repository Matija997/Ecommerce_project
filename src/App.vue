<template>
  <div id="app">
    <NavBar />
    <div>
      <Cart :cartItems="cart" @remove="removeFromCart" />
      <ProductList :products="products" @add-to-cart="addToCart" />
    </div>
  </div>
</template>


<script>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'
import ProductList from './components/ProductList.vue'
import Cart from './components/Cart.vue'

export default {
  components: { NavBar, ProductList, Cart },
  setup() {
    const products = ref([
      { id: 1, name: 'T-shirt', price: 20 },
      { id: 2, name: 'Jeans', price: 50 },
      { id: 3, name: 'Sneakers', price: 80 }
    ])

    const cart = ref([])

    function addToCart(product) {
      const item = cart.value.find(i => i.id === product.id)
      if (item) {
        item.quantity++
      } else {
        cart.value.push({ ...product, quantity: 1 })
      }
    }

    function removeFromCart(productId) {
      cart.value = cart.value.filter(item => item.id !== productId)
    }

    return { products, cart, addToCart, removeFromCart }
  }
}
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
</style>
