import {$authHost} from "@/api/index.js";

export const getCart = async () => {
    const cart = await $authHost.get('basket')
    return cart.data
}

export const getCartCount = async () => {
    const cart = await $authHost.get('basket/count')
    return cart.data
}

export const addToCart = async (game_id) => {
    return await $authHost.post('basket', {game: game_id})
}

export const deleteGameFromCart = async (game_id) => {
    return await $authHost.delete(`basket/remove_game/${game_id}`)
}

export const clearCart = async () => {
    return await $authHost.delete(`tasks/basket/clear`)
}
