import { createRouter, createWebHistory } from 'vue-router'

import Home from '../pages/Home.vue'
import Men from '../pages/Men.vue'
import Women from '../pages/Woman.vue'
import Kids from '../pages/Kids.vue'
import About from '../pages/About.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/men', component: Men },
  { path: '/women', component: Women },
  { path: '/kids', component: Kids },
  { path: '/about', component: About }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
