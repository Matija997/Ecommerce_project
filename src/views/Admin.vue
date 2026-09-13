<script setup>
import { ref, computed } from 'vue'
import { useStore } from '../store/useStore'
import AdminProducts from '../components/AdminProducts.vue'
import AdminUsers from '../components/AdminUsers.vue'
import AdminMessages from '../components/AdminMessages.vue'
import AdminOrders from '../components/AdminOrders.vue'

const { state } = useStore()
const isAdmin = state.user?.role === 'admin'

const TITLES = {
  products: 'Product Management',
  users: 'User Management',
  messages: 'Contact Messages',
  orders: 'Orders'
}

const activeTab = ref('products')
const title = computed(() => TITLES[activeTab.value])
</script>

<template>
  <div class="admin-page container">
    <span class="eyebrow">Admin</span>
    <h1 class="admin-page__title">{{ title }}</h1>

    <div v-if="isAdmin" class="admin-page__tabs">
      <button
        class="admin-page__tab"
        :class="{ 'admin-page__tab--active': activeTab === 'products' }"
        @click="activeTab = 'products'"
      >
        Products
      </button>
      <button
        class="admin-page__tab"
        :class="{ 'admin-page__tab--active': activeTab === 'users' }"
        @click="activeTab = 'users'"
      >
        Users
      </button>
      <button
        class="admin-page__tab"
        :class="{ 'admin-page__tab--active': activeTab === 'orders' }"
        @click="activeTab = 'orders'"
      >
        Orders
      </button>
      <button
        class="admin-page__tab"
        :class="{ 'admin-page__tab--active': activeTab === 'messages' }"
        @click="activeTab = 'messages'"
      >
        Messages
      </button>
    </div>

    <AdminProducts v-if="activeTab === 'products' || !isAdmin" />
    <AdminUsers v-else-if="activeTab === 'users'" />
    <AdminOrders v-else-if="activeTab === 'orders'" />
    <AdminMessages v-else-if="activeTab === 'messages'" />
  </div>
</template>

<style scoped>
.admin-page {
  padding: 48px 32px 100px;
}

.admin-page__title {
  font-size: clamp(1.8rem, 3.5vw, 2.4rem);
  margin: 8px 0 24px;
}

.admin-page__tabs {
  display: flex;
  gap: 8px;
  border-bottom: 1px solid var(--line);
  margin-bottom: 32px;
}

.admin-page__tab {
  background: none;
  border: none;
  padding: 10px 4px;
  margin-right: 24px;
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: var(--tracking);
  text-transform: uppercase;
  color: var(--taupe);
  border-bottom: 2px solid transparent;
  cursor: pointer;
}

.admin-page__tab--active {
  color: var(--ink);
  border-bottom-color: var(--ink);
}
</style>
