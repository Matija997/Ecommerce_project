import { createRouter, createWebHistory } from 'vue-router'

import Home from '../pages/Home.vue'
import Clothing from '../pages/Clothing.vue'
import Footwear from '../pages/Footwear.vue'
import Sale from '../pages/Sale.vue'
import About from '../pages/About.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/clothing', component: Clothing },
  { path: '/footwear', component: Footwear },
  { path: '/sale', component: Sale },
  { path: '/about', component: About }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
