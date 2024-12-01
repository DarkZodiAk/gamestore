import {$authHost} from "@/api/index.js";

export const getGames = async () => {
    const games = await $authHost.get('games')
    return games.data
}

export const getGameById = async (id) => {
    const game = await $authHost.get(`games/${id}`)
    return game.data
}
