<script setup>
import { onMounted } from 'vue'
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
import MarqueeBar from './components/MarqueeBar.vue'
import SearchOverlay from './components/SearchOverlay.vue'
import LoginModal from './components/LoginModal.vue'
import CartDrawer from './components/CartDrawer.vue'
import { useProducts } from './store/useProducts'

const { fetchProducts } = useProducts()

onMounted(() => {
  fetchProducts()
})
</script>

<template>
  <MarqueeBar />
  <AppHeader />

  <main class="main">
    <router-view v-slot="{ Component, route }">
      <transition name="page-fade" mode="out-in">
        <component :is="Component" :key="route.path" />
      </transition>
    </router-view>
  </main>

  <AppFooter />

  <SearchOverlay />
  <LoginModal />
  <CartDrawer />
</template>

<style scoped>
.main {
  flex: 1;
}
</style>
