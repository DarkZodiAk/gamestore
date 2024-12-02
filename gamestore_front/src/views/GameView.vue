<script setup>
import {computed, onMounted, ref} from "vue";
import {useAuthStore} from "@/stores/AuthStore.js";
import {useGameStore} from "@/stores/GameStore.js";
import {useRoute, useRouter} from "vue-router";
import {getGameById} from "@/api/game.js";
import {addToCart, deleteGameFromCart, getCart} from "@/api/cart.js";
import {addToWishlist, deleteGameFromWishlist, getWishlist} from "@/api/wishlist.js";

import Footer from "@/components/Footer.vue";
import Header from "@/components/Header.vue";
import Tag from "@/components/Tag.vue";
import { Bookmark } from "lucide-vue-next";

const authStore = useAuthStore();
const gameStore = useGameStore();
const router = useRouter();
const route = useRoute();
const id = computed(() => route.params.id);

let game = ref({});
let showLoader = ref(false);
let tags = ref([]);
let desc_p = ref([]);
let in_cart = ref(false);
let in_wishlist = ref(false);

const getGame = async () => {
    try {
        showLoader.value = true;
        game.value = await getGameById(id.value);
        tags.value = game.value.tags.split(/\r\n|\n|\r/);
        desc_p.value = game.value.description.split(/\r\n|\n|\r/);
        await checkCart();
        await checkWishlist();
    } catch (e) {
        console.log(e.response);
    } finally {
        showLoader.value = false;
    }
}

const checkCart = async () => {
    const cart = (await getCart()).map(val => val.game.toString());
    in_cart.value = cart.includes(id.value);
    await gameStore.updateCountInCart();
}

const checkWishlist = async () => {
    const wishlist = (await getWishlist()).map(val => val.game.toString());
    in_wishlist.value = wishlist.includes(id.value);
}

const addCart = async () => {
    try {
        await addToCart(id.value);
        await checkCart();
    } catch (e) {
        console.log(e.response);
    }
}

const removeCart = async () => {
    try {
        await deleteGameFromCart(id.value);
        await checkCart();
    } catch (e) {
        console.log(e.response);
    }
}

const addWishlist = async () => {
    try {
        await addToWishlist(id.value);
        await checkWishlist();
    } catch (e) {
        console.log(e.response);
    }
}

const removeWishlist = async () => {
    try {
        await deleteGameFromWishlist(id.value);
        await checkWishlist();
    } catch (e) {
        console.log(e.response);
    }
}

const logout = () => {
    authStore.logout();
    router.push('/login');
}


onMounted(async () => {
    await getGame();
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
          <div class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-start width-lim" style="--kobweb-arrange-spaced-by: 36px;">
           <span class="silk-span-text" style="font-size: 34px; font-weight: 700;">{{game.name}}</span>
           <div class="kobweb-row kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-top" style="--kobweb-arrange-spaced-by: 50px;">
            <div class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-start" style="width: 280px; --kobweb-arrange-spaced-by: 16px;">
             <img :src="game.image" alt="" style="width: 100%; aspect-ratio: 0.87 / 1; clip-path: inset(0% round 12px); object-fit: cover"/>
             <div class="kobweb-row kobweb-arrange-space-between kobweb-align-center-vert" style="width: 100%;">
              <span class="silk-span-text" style="font-size: 22px; font-weight: 700;">{{game.price}}&nbsp;₽</span>

               <button @click="in_cart ? removeCart() : addCart()"
                       :class="in_cart ? 'outlined-button' : 'primary-button'" type="button">
                 <span class="silk-span-text" style="font-size: 16px; line-height: 1.5;">{{in_cart ? 'В корзине' : 'В корзину'}}</span>
               </button>
             </div>

             <button @click="in_wishlist ? removeWishlist() : addWishlist()"
                     class="wish-button" type="button" :style="{'color': in_wishlist ? '#FFFFFF' : '#999999'}">
               <div class="kobweb-row kobweb-align-center-vert align-center-hor">
                 <Bookmark class="icon" :style="{'fill': in_wishlist ? '#FFFFFF' : 'none'}"/>
                 <span class="silk-span-text" style="font-size: 18px;">{{in_wishlist ? 'В списке желаемого' : 'В список желаемого'}}</span>
               </div>
             </button>

            </div>
            <div class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-start" style="width: 849px; --kobweb-arrange-spaced-by: 20px;">
             <div class="kobweb-row kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-top" style="--kobweb-arrange-spaced-by: 8px;">
              <Tag :value="game.rating" is_rating="true"/>
              <Tag v-for="tag in tags" :value="tag"/>
             </div>
             <div class="kobweb-row kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-top" style="--kobweb-arrange-spaced-by: 25px;">
              <div class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-start" style="--kobweb-arrange-spaced-by: 10px;">
                <span class="silk-span-text feat">Жанр</span>
                <span class="silk-span-text feat">Язык</span>
                <span class="silk-span-text feat">Дата выхода</span>
                <span class="silk-span-text feat">Издатель</span>
                <span class="silk-span-text feat">Разработчик</span>
                <span class="silk-span-text feat">Особенности</span>
              </div>
              <div class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-start" style="--kobweb-arrange-spaced-by: 10px;">
                <span class="silk-span-text feat_val">{{game.genre}}</span>
                <span class="silk-span-text feat_val">{{game.language}}</span>
                <span class="silk-span-text feat_val">{{game.release_date}}</span>
                <span class="silk-span-text feat_val">{{game.publisher}}</span>
                <span class="silk-span-text feat_val">{{game.developer}}</span>
                <span class="silk-span-text feat_val">{{game.features}}</span>
              </div>
             </div>
             <div class="kobweb-col kobweb-arrange-top kobweb-align-start">
              <p v-for="desc in desc_p"><span class="silk-span-text" style="font-size: 18px; font-weight: 400; color: rgb(255, 255, 255);">{{desc}}</span><br><br></p>
             </div>
            </div>
           </div>
          </div>
        </div>
       <Footer/>
      </div>
    </div>
  </div>
</template>

<style scoped>

.wish-button {
    background: #141414;
    padding: 16px 24px;
    text-align: center;
    font-weight: 500;
    outline: 0;
    font-size: 16px;
    transition: .2s;
    cursor: pointer;
    width: 100%;
    border: 1px solid rgb(38, 38, 38);
    border-radius: 8px;
    --kobweb-arrange-spaced-by: 8px;
}

.feat {
    font-size: 16px;
    font-weight: 400;
    color: rgb(153, 153, 153)
}

.feat_val {
    font-size: 16px;
    font-weight: 400;
    color: rgb(255, 255, 255)
}

</style>
