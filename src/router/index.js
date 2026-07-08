import { createRouter, createWebHistory } from 'vue-router'

import Home from '../pages/Home.vue'
import Men from '../pages/Men.vue'
import Women from '../pages/Woman.vue'
import Sale from '../pages/Sale.vue'
import About from '../pages/About.vue'
import Profile from '../pages/Profile.vue'
import Clothing from '../pages/men/Clothing.vue'
import Footwear from '../pages/men/Footwear.vue'
import Accessories from '../pages/men/Accessories.vue'
import ProductPage from '../pages/Product.vue'
import Admin from '../pages/Admin.vue'


const routes = [
  { path: '/', component: Home },
  { path: '/men', component: Men },
  { path: '/men/clothing', component: Clothing },
  { path: '/men/footwear', component: Footwear },
  { path: '/men/accessories', component: Accessories },
  { path: '/women', component: Women },
  { path: '/sale', component: Sale },
  { path: '/about', component: About },
  { path: '/men/clothing/:productName', component: ProductPage, props: true },
  { path: '/profile', component: Profile, meta: { requiresAuth: true }},
  { path:'/admin', component:Admin, meta:{ requiresAdmin:true }}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
router.beforeEach((to, from, next) => {
  const token =
    localStorage.getItem('token') ||
    sessionStorage.getItem('token')

  const user =
    JSON.parse(
      localStorage.getItem('user') ||
      sessionStorage.getItem('user')
    )


  // Protected pages
  if (to.meta.requiresAuth && !token) {
    next('/')
    return
  }


  // Admin only pages
  if (to.meta.requiresAdmin) {

    if (!token) {
      next('/')
      return
    }

    if (!user || user.role !== 'admin') {
      next('/')
      return
    }
  }


  next()
})
export default router
