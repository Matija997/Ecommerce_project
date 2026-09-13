<script setup>
import AdminProducts from '../components/AdminProducts.vue'
</script>

<template>
  <div class="admin-page container">
    <span class="eyebrow">Admin</span>
    <h1 class="admin-page__title">Product Management</h1>
    <AdminProducts />
  </div>
</template>

<style scoped>
.admin-page {
  padding: 48px 32px 100px;
}

.admin-page__title {
  font-size: clamp(1.8rem, 3.5vw, 2.4rem);
  margin: 8px 0 32px;
}
</style>
