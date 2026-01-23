<template>
  <div id="app">
    <NavBar @open-login="showLoginModal = true" />
    <router-view />
    <LoginModal v-if="showLoginModal" @close="showLoginModal = false" />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import LoginModal from './components/LoginForm.vue'

export default {
  components: { NavBar, LoginModal },
  data() {
    return {
      showLoginModal: false
    }
  }
}
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
</style>
