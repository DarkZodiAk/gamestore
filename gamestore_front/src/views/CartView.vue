<script setup>
import {onMounted, ref} from "vue";
import {useGameStore} from "@/stores/GameStore.js";
import {useAuthStore} from "@/stores/AuthStore.js";
import {clearCart, deleteGameFromCart, getCart} from "@/api/cart.js";
import {useRouter} from "vue-router";
import {getGames} from "@/api/game.js";

import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import AlertDialog from "@/components/AlertDialog.vue";
import { CircleSlash2 } from 'lucide-vue-next';
import VLoader from "@/components/VLoader.vue";

const authStore = useAuthStore();
const gameStore = useGameStore();
const router = useRouter();

let games = ref([])
let showLoader = ref(false);
let isDialogVisible = ref(false)
let total = ref(0);

const getCartGames = async () => {
    try {
        showLoader.value = true;
        total.value = 0
        const cart = (await getCart()).map(val => val.game);
        const game = await getGames()
        games.value = game.filter(val => cart.includes(val.id))
        games.value.forEach(val => {
            total.value += parseInt(val.price)
        })

        await gameStore.updateCountInCart();
    } catch (e) {
        console.log(e.response);
    } finally {
        showLoader.value = false;
    }
}

const removeCart = async (id) => {
    try {
        await deleteGameFromCart(id);
        await getCartGames();
    } catch (e) {
        console.log(e.response);
    }
}

const checkout = async () => {
    try {
        await clearCart();
        isDialogVisible.value = true;
        await getCartGames();
    } catch (e) {
        console.log(e.response);
    }
}

const goToGamePage = (id) => {
    router.push(`/game/${id}`)
}

const logout = () => {
    authStore.logout();
    router.push('/login');
}


onMounted(async () => {
    await getCartGames();
    if (authStore.authError) {
        logout();
    }
})
</script>

<template>
  <div id="root" style="width: 100%; height: 100%;" class="silk-colors_dark">
    <div class="silk-surface silk-smooth-color kobweb-box kobweb-align-top-start" style="min-height: 100vh;">
      <div class="kobweb-col kobweb-arrange-space-between kobweb-align-start" style="width: 100%; height: 100%;">
       <div class="kobweb-col kobweb-arrange-top kobweb-align-center-horiz" style="width: 100%; height: 100%;">
        <Header/>
        <VLoader class="loader" v-if="showLoader"></VLoader>
        <div v-else class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-start width-lim" style="--kobweb-arrange-spaced-by: 40px;">
         <span class="silk-span-text" style="font-size: 32px; font-weight: 700;">Корзина</span>

         <div v-if="games.length !== 0" class="kobweb-row kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-top" style="width: 1180px; --kobweb-arrange-spaced-by: 50px;">
          <div class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-start" style="clip-path: inset(0% round 20px); background: rgb(15, 15, 15); padding: 40px; --kobweb-arrange-spaced-by: 36px;">

            <div v-for="(game, index) in games" :key="index" @click="goToGamePage(game.id)"
                 class="cart-game kobweb-row kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-top" style="width: 743px; height: 122px; --kobweb-arrange-spaced-by: 18px;">
              <img :src="game.image" alt="" style="width: 220px; height: 100%; clip-path: inset(0% round 12px); object-fit: cover"/>
              <div class="kobweb-col kobweb-arrange-space-between kobweb-align-end" style="flex-grow: 1; height: 100%;">
                <div class="kobweb-row kobweb-arrange-space-between kobweb-align-center-vert" style="width: 100%;">
                  <span class="silk-span-text" style="font-size: 20px; font-weight: 400; flex-grow: 1; padding: 0px 10px 0px 0px;">{{game.name}}</span><span class="silk-span-text" style="font-size: 22px; font-weight: 700;">{{game.price}}&nbsp;₽</span>
                </div>
                <span @click.stop="removeCart(game.id)" class="silk-span-text" style="font-size: 18px; font-weight: 600; color: rgb(153, 153, 153);">Удалить</span>
              </div>
            </div>
          </div>

          <div class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-start" style="flex-grow: 1; --kobweb-arrange-spaced-by: 20px;">
           <div class="kobweb-row kobweb-arrange-space-between kobweb-align-center-vert" style="width: 100%;">
            <span class="silk-span-text" style="font-size: 27px; font-weight: 600;">Итого</span><span class="silk-span-text" style="font-size: 27px; font-weight: 600;">{{total}}&nbsp;₽</span>
           </div>
            <button class="primary-button" style="width: 100%" type="button" @click="checkout">
              <span class="silk-span-text" style="font-size: 16px; line-height: 1.5; width: 100%;">Оплатить</span>
            </button>
          </div>
         </div>

         <div v-else class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-center-horiz" style="width: 1180px; --kobweb-arrange-spaced-by: 30px;">
           <CircleSlash2 style="height: 79px; width: 79px"/>
           <span class="silk-span-text" style="font-size: 32px; font-weight: 700;">Ваша корзина пуста</span>
         </div>

        </div>
       </div>
       <Footer/>
      </div>
    </div>
    <AlertDialog
      v-if="isDialogVisible"
      message="Спасибо за покупку!"
      :visible="isDialogVisible"
      @onDismiss="isDialogVisible = false"
    />
  </div>
</template>

<style scoped>
.cart-game {
    cursor: pointer;
}
</style>
