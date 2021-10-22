import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Product from '../views/Product.vue'
import LogIn from '../views/LogIn.vue'
import Contactenos from '../views/Contactenos.vue'
import Ofertas from '../views/Ofertas.vue'
import SignUp from '../views/SignUp.vue'
import Cart from '../views/Cart.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  { // el link el producto
    path: '/:product_slug',
    name: 'Product',
    component: Product
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/contactenos',
    name: 'Contactenos',
    component: Contactenos
  },
  {
    path: '/ofertas',
    name: 'Ofertas',
    component: Ofertas
  },  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
