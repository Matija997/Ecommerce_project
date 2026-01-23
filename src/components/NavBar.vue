<script setup>
import { ref } from 'vue'
import LoginModal from './LoginForm.vue'
import SignupModal from './SignUpForm.vue'

const showLoginModal = ref(false)
const showSignupModal = ref(false)

function openLoginModal() {
  showLoginModal.value = true
  showSignupModal.value = false
}

function openSignupModal() {
  showLoginModal.value = false
  showSignupModal.value = true
}

function closeModals() {
  showLoginModal.value = false
  showSignupModal.value = false
}
</script>

<template>
  <nav class="navbar">
    <div class="nav-left">
      <ul class="nav-links">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/men">Men</router-link></li>
        <li><router-link to="/women">Women</router-link></li>
        <li><router-link to="/sale">Sale</router-link></li>
        <li><router-link to="/about">About</router-link></li>
      </ul>
    </div>

    <div class="nav-right">
      <button class="icon-button" title="Search">
        <i class="fas fa-search"></i>
      </button>

      <a href="#" class="nav-link" @click.prevent="openLoginModal">
        Login
      </a>

      <router-link to="/cart" class="nav-link" title="Cart">
        <i class="fas fa-shopping-cart"></i>
      </router-link>

      <button class="icon-button" title="Menu">
        <i class="fa-solid fa-bars"></i>
      </button>
    </div>
  </nav>

  <LoginModal
    v-if="showLoginModal"
    @close="closeModals"
    @signup="openSignupModal"
  />

  <SignupModal
    v-if="showSignupModal"
    @close="closeModals"
    @switch-to-login="openLoginModal"
  />
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  color: #333;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 20px;
  z-index: 1000;
}

.nav-left {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}

.nav-right {
  margin-left: auto;
  display: flex;
  align-items: center;
}

.nav-links {
  list-style: none;
  display: flex;
  margin: 0;
}

.nav-links li {
  margin-right: 20px;
}

.nav-links a,
.nav-link, .icon-button {
  color: #333;
  text-decoration: none;
  font-size: 15px;
  padding: 10px;
  border-radius: 20px;
}
.nav-links a:hover,
.nav-link:hover, .icon-button:hover {
  background-color: rgba(158, 157, 157, 0.3);
  transition: background-color 0.3s ease;
}

.nav-links a.router-link-active {
  color: red;
}

.icon-button {
  background: none;
  border: none;
  color: #333;
  font-size: 18px;
  cursor: pointer;
}
</style>
