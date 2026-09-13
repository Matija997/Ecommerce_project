import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CategoryPage from '../views/CategoryPage.vue'
import Sale from '../views/Sale.vue'
import About from '../views/About.vue'
import ProductPage from '../views/ProductPage.vue'
import Checkout from '../views/Checkout.vue'
import Admin from '../views/Admin.vue'
import NotFound from '../views/NotFound.vue'
import { useStore } from '../store/useStore'

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
  { path: '/product/:id', name: 'product', component: ProductPage },
  { path: '/checkout', name: 'checkout', component: Checkout },
  {
    path: '/admin',
    name: 'admin',
    component: Admin,
    beforeEnter: (to, from, next) => {
      const { state } = useStore()
      next(['admin', 'editor'].includes(state.user?.role) ? true : '/')
    }
  },
  { path: '/:pathMatch(.*)*', name: 'not-found', component: NotFound }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to) {
    if (to.hash) {
      return { el: to.hash, top: 96, behavior: 'smooth' }
    }
    return { top: 0 }
  }
})

export default router
