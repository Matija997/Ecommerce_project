<script setup>
import { ref, onMounted,  onBeforeUnmount} from 'vue'
import { useRouter } from 'vue-router'
import LoginModal from './LoginForm.vue'
import SignupModal from './SignUpForm.vue'
import CartModal from './Cart.vue'


const router = useRouter()
const showLoginModal = ref(false)
const showSignupModal = ref(false)
const showCartModal = ref(false)
const loginMessage = ref('')
const loginEmail = ref('')
const isLoggedIn = ref(false)
const user = ref(null)
const showProfileMenu = ref(false)
const profileWrapper = ref(null)
const cartItems = ref([
  { id: 1, name: 'T-Shirt', price: 20, quantity: 2 },
  { id: 2, name: 'Jeans', price: 50, quantity: 1 }
])

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
  loginMessage.value = ''
}

function handleSignupSuccess(payload) {
  showSignupModal.value = false
  showLoginModal.value = true
  loginMessage.value = payload.message
  loginEmail.value = payload.email
}

function handleLoginSuccess(loggedUser) {
  isLoggedIn.value = true
  user.value = loggedUser
}

onMounted(() => {
  const token = localStorage.getItem('token') || sessionStorage.getItem('token')
  const storedUser = localStorage.getItem('user') || sessionStorage.getItem('user')

  if (token && storedUser) {
    isLoggedIn.value = true
    user.value = JSON.parse(storedUser)
  }
  document.addEventListener('click', handleClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})
function toggleProfileMenu() {
  showProfileMenu.value = !showProfileMenu.value
}
function handleClickOutside(event) {
  if (profileWrapper.value && !profileWrapper.value.contains(event.target)) {
    showProfileMenu.value = false
  }
}
function goToProfile() {
  showProfileMenu.value = false
  router.push('/profile')
}
function logout() {
  localStorage.clear()
  sessionStorage.clear()
  isLoggedIn.value = false
  user.value = null
  showProfileMenu.value = false
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

      <a v-if="!isLoggedIn" href="#" class="nav-link" @click.prevent="openLoginModal">
        Login
      </a>
      <div v-else class="profile-wrapper" ref="profileWrapper">
        <button class="icon-button" @click="toggleProfileMenu">
          <i class="fas fa-user"></i>
        </button>

        <div v-if="showProfileMenu" class="profile-dropdown">
          <button @click="goToProfile">My Profile</button>
          <button @click="logout">Logout</button>
        </div>
      </div>

      <button class="icon-button" title="Cart" @click="showCartModal = true">
        <i class="fas fa-shopping-cart"></i>
      </button>
    </div>
  </nav>

  <LoginModal
    v-if="showLoginModal"
    @close="closeModals"
    :successMessage="loginMessage"
    :prefillEmail="loginEmail"
    @login-success="handleLoginSuccess"
    @signup="openSignupModal"
  />

  <SignupModal
    v-if="showSignupModal"
    @close="closeModals"
    @signup-success="handleSignupSuccess"
    @switch-to-login="openLoginModal"
  />

  <CartModal
    v-if="showCartModal"
    :cartItems="cartItems"
    @close="showCartModal = false"
    @remove="removeFromCart"
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

.profile-wrapper {
  position: relative;
}

.profile-dropdown {
  position: absolute;
  top: 45px;
  right: 0;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.15);
  min-width: 140px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  z-index: 3000;
}

.profile-dropdown button {
  background: none;
  border: none;
  padding: 10px 14px;
  text-align: left;
  cursor: pointer;
  font-size: 14px;
}

.profile-dropdown button:hover {
  background-color: #f2f2f2;
}

</style>
