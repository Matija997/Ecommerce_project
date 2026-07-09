import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CategoryPage from '../views/CategoryPage.vue'
import Sale from '../views/Sale.vue'
import About from '../views/About.vue'
import NotFound from '../views/NotFound.vue'

const routes = [
  { path: '/', name: 'home', component: Home },
  {
    path: '/man',
    name: 'man',
    component: CategoryPage,
    props: { category: 'man', title: 'Man' }
  },
  {
    path: '/woman',
    name: 'woman',
    component: CategoryPage,
    props: { category: 'woman', title: 'Woman' }
  },
  { path: '/sale', name: 'sale', component: Sale },
  { path: '/about', name: 'about', component: About },
  { path: '/:pathMatch(.*)*', name: 'not-found', component: NotFound }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  }
})

export default router
