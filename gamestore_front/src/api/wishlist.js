import {$authHost} from "@/api/index.js";

export const getWishlist = async () => {
    const wishlist = await $authHost.get('wishlist')
    return wishlist.data
}

export const addToWishlist = async (game_id) => {
    return await $authHost.post('wishlist', {game: game_id})
}

export const deleteGameFromWishlist = async (game_id) => {
    return await $authHost.delete(`wishlist/remove_game/${game_id}`)
}
