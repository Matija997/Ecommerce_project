import { createRouter, createWebHistory } from 'vue-router'

import Home from '../pages/Home.vue'
import Men from '../pages/Men.vue'
import Women from '../pages/Woman.vue'
import Sale from '../pages/Sale.vue'
import About from '../pages/About.vue'
import Profile from '../pages/Profile.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/men', component: Men },
  { path: '/women', component: Women },
  { path: '/sale', component: Sale },
  { path: '/about', component: About },
  { path: '/profile', component: Profile, meta: { requiresAuth: true }}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token') || sessionStorage.getItem('token')
  
  if (to.meta.requiresAuth && !token) {
    next('/')
  } else {
    next()
  }
})

export default router
