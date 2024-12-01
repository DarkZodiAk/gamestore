import {ref} from 'vue'
import {defineStore} from 'pinia'
import {getCartCount} from "@/api/cart.js";

export const useGameStore = defineStore('game', () => {
    const cartCount = ref(0);

    const updateCountInCart = async () => {
        try {
            cartCount.value = await getCartCount();
        } catch {
            console.log(e.response);
        }
    }
    return {
        cartCount,
        updateCountInCart,
    };
})
