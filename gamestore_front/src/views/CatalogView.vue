<script setup>
import {onMounted, ref} from "vue";

import {useAuthStore} from "@/stores/AuthStore.js";
import {useGameStore} from "@/stores/GameStore.js";
import {useRouter} from "vue-router";
import {getGames} from "@/api/game.js";

import VLoader from "@/components/VLoader.vue";
import Footer from "@/components/Footer.vue";
import Header from "@/components/Header.vue";

const authStore = useAuthStore();
const router = useRouter()

let games = ref([]);
let showLoader = ref(false);

const getAllGames = async () => {
    try {
        showLoader.value = true;
        games.value = await getGames();
    } catch (e) {
        console.log(e.response);
    } finally {
        showLoader.value = false;
    }
}

const goToGamePage = (id) => {
    router.push(`/game/${id}`)
}

const logout = () => {
    authStore.logout()
    router.push('/login')
}

onMounted(async () => {
    await getAllGames();
    if (authStore.authError) {
        logout()
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
      <div v-else class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-start width-lim" style="--kobweb-arrange-spaced-by: 30px;">
       <span class="silk-span-text" style="font-size: 32px; font-weight: 700;">Каталог</span>
       <div class="silk-simple-grid" style="--silk-simple-grid-col-count-zero: 3; --silk-simple-grid-col-count-sm: 3; --silk-simple-grid-col-count-md: 3; --silk-simple-grid-col-count-lg: 3; --silk-simple-grid-col-count-xl: 3; width: 100%;">

         <div v-for="(game, index) in games" :key="index" @click="goToGamePage(game.id)"
              class="game-card kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-center-horiz" style="height: 490px; width: 370px; --kobweb-arrange-spaced-by: 18px;">
           <div class="kobweb-box kobweb-align-top-start" style="width: 100%;">
             <img :src="game.image" alt="" style="width: 100%; aspect-ratio: 0.87 / 1; clip-path: inset(0% round 12px); object-fit: cover"/>
             <div class="kobweb-align-top-end-self kobweb-box kobweb-align-top-start" style="clip-path: inset(0% round 5px); background: rgba(0, 0, 0, 0.5); font-size: 14px; font-weight: 600; padding: 5px 10px; margin: 16px">
              <span class="silk-span-text" style="opacity: 1;">{{game.rating}}</span>
             </div>
           </div>
           <span class="silk-span-text" style="font-size: 22px; font-weight: 500;">{{game.name}}</span>
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
.loader {
    margin-top: 50px;
}
</style>
