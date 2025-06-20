import { createRouter, createWebHistory } from 'vue-router'

import Home from '../pages/Home.vue'
import Men from '../pages/Men.vue'
import Women from '../pages/Woman.vue'
import Sale from '../pages/Sale.vue'
import About from '../pages/About.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/men', component: Men },
  { path: '/women', component: Women },
  { path: '/sale', component: Sale },
  { path: '/about', component: About }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
