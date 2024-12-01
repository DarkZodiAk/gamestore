import { createRouter, createWebHistory } from 'vue-router'

import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import CatalogView from "@/views/CatalogView.vue";
import CartView from "@/views/CartView.vue";
import WishlistView from "@/views/WishlistView.vue";
import GameView from "@/views/GameView.vue";

import {useAuthStore} from "@/stores/AuthStore.js";


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/login',
            name: 'login',
            component: LoginView,
            meta: {requiresAuth: false},
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterView,
            meta: {requiresAuth: false},
        },
        {
            path: '/',
            name: 'catalog',
            component: CatalogView,
            meta: {requiresAuth: true},
        },
        {
            path: '/cart',
            name: 'cart',
            component: CartView,
            meta: {requiresAuth: true},
        },
        {
            path: '/wishlist',
            name: 'wishlist',
            component: WishlistView,
            meta: {requiresAuth: true},
        },
        {
            path: '/game/:id',
            name: 'game',
            component: GameView,
            meta: {requiresAuth: true},
        }
    ]
})

router.beforeEach((to, from) => {
    const authStore = useAuthStore();
    // instead of having to check every route record with
    // to.matched.some(record => record.meta.requiresAuth)
    if (to.meta.requiresAuth && !authStore.accessToken) {
        // this route requires auth, check if logged in
        // if not, redirect to login page.
        return {
            path: '/login',
            // save the location we were at to come back later
            query: {redirect: to.fullPath},
        }
    }
})


export default router
