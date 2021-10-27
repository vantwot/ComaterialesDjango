import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';
import LogIn from './components/login.vue'
import SignUp from './components/SignUp.vue'
import Home from './components/Home.vue'
import Contacto from './components/Contacto.vue'
import Carrito from './components/Carrito.vue'
import Productos from './components/Productos.vue'
import Producto from './components/Producto.vue'


const routes = [{
        path: '/',
        name: 'root',
        component: App
    },
    {
        path: '/user/logIn',
        name: "logIn",
        component: LogIn
    },
    {
        path: '/user/signUp',
        name: "signUp",
        component: SignUp
    },
    {
        path: '/user/home',
        name: "home",
        component: Home
    },
    {
        path: '/carrito',
        name: "carrito",
        component: Carrito
    },
    {
        path: '/contacto',
        name: "contacto",
        component: Contacto
    },
    {
        path: '/productos',
        name: "productos",
        component: Productos
    },
    {
<<<<<<< HEAD
        path: '/:producto/:id_producto/',
=======
        path: '/producto/:id',
>>>>>>> 7aa28de52e45f2f8918244c2ff4dc0e16a9246d3
        name : "producto",
        component: Producto
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;